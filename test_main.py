from fastapi.testclient import TestClient
from main import app
from service import AdminItemService, UserItemService
from models import ItemRequest

client = TestClient(app)

# Test 1: Valid item creation
def test_create_item():
    response = client.post("/items", json={"name": "Phone", "price": 500})
    assert response.status_code == 200
    assert response.json()["name"] == "Phone"

# Test 2: Valid item retrieval
def test_get_item():
    # Ensure item is created first and get its ID
    create_response = client.post("/items", json={"name": "Laptop", "price": 1000})
    item_id = create_response.json()["id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["id"] == item_id


# Test 3: Item not found
def test_get_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item with ID 999 not found"

# Test 4: Invalid price (negative)
def test_create_item_invalid_price():
    response = client.post("/items", json={"name": "Invalid", "price": -10})
    assert response.status_code == 422
    assert "Price must be positive" in response.json()["detail"][0]["msg"]

def test_create_item_empty_name():
    response = client.post("/items", json={"name": "  ", "price": 100})
    assert response.status_code == 422
    assert "Name cannot be empty" in response.json()["detail"][0]["msg"]

# Test 6: Role-based - user cannot create
def test_user_cannot_create_item():
    service = UserItemService()
    try:
        service.create_item(ItemRequest(name="User Item", price=100))
    except PermissionError as e:
        assert str(e) == "Users cannot create items."
