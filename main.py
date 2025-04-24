from fastapi import FastAPI, HTTPException, Depends
from models import ItemRequest
from service import AdminItemService, UserItemService

app = FastAPI()

# 🔹 Custom Exception moved here
class ItemNotFoundException(HTTPException):
    def __init__(self, item_id: int):
        super().__init__(status_code=404, detail=f"Item with ID {item_id} not found")

# 🔹 Role simulation (switch role to 'user' or 'admin' here)
# Global instances
admin_service = AdminItemService()
user_service = UserItemService()

def get_service(role: str = "admin"):
    if role == "admin":
        return admin_service
    else:
        return user_service


@app.post("/items")
def create_item(item: ItemRequest, service=Depends(get_service)):
    try:
        return service.create_item(item)
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))

@app.get("/items/{item_id}")
def get_item(item_id: int, service=Depends(get_service)):
    item = service.get_item(item_id)
    if not item:
        raise ItemNotFoundException(item_id)
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemRequest, service=Depends(get_service)):
    try:
        updated_item = service.update_item(item_id, item)
        if not updated_item:
            raise ItemNotFoundException(item_id)
        return updated_item
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))

@app.delete("/items/{item_id}")
def delete_item(item_id: int, service=Depends(get_service)):
    try:
        deleted = service.delete_item(item_id)
        if not deleted:
            raise ItemNotFoundException(item_id)
        return {"detail": "Item deleted"}
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    
@app.get("/")
def read_root():
    return {"message": "FastAPI CRUD is running!"}

