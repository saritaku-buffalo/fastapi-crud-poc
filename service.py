class BaseService:
    def __init__(self):
        self.items = {}
        self.counter = 1

    def get_item(self, item_id):
        return self.items.get(item_id)

    def list_items(self):
        return list(self.items.values())

# Admin service: full access
class AdminItemService(BaseService):
    def create_item(self, item_data):
        item_id = self.counter
        self.items[item_id] = {"id": item_id, "name": item_data.name, "price": item_data.price}
        self.counter += 1
        return self.items[item_id]

    def update_item(self, item_id, item_data):
        if item_id in self.items:
            self.items[item_id].update({"name": item_data.name, "price": item_data.price})
            return self.items[item_id]
        return None

    def delete_item(self, item_id):
        if item_id in self.items:
            return self.items.pop(item_id)
        return None

# User service: read-only
class UserItemService(BaseService):
    def create_item(self, item_data):
        raise PermissionError("Users cannot create items.")

    def update_item(self, item_id, item_data):
        raise PermissionError("Users cannot update items.")

    def delete_item(self, item_id):
        raise PermissionError("Users cannot delete items.")
