from fastapi import FastAPI, HTTPException
from models import ItemRequest
from service import ItemService

app = FastAPI()
service = ItemService()

@app.post("/items")
def create_item(item: ItemRequest):
    return service.create_item(item)

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemRequest):
    updated_item = service.update_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    deleted = service.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}
