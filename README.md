# FastAPI CRUD POC with Validation, Inheritance, Role-Based Access, and Payload Handling

This project is a **Proof of Concept (POC)** showcasing a **FastAPI CRUD application** with the following features:

- CRUD operations (Create, Read, Update, Delete)
- Data validation using **Pydantic**
- Custom Exception Handling
- Role-based access control using **Inheritance**
- Unit Testing with **PyTest**
- External **Payload handling** using **Python requests** and **JSON files**

---

API will be available at: http://127.0.0.1:8000

Swagger UI for API testing: http://127.0.0.1:8000/docs

Method | Endpoint | Description
POST | /items | Create a new item
GET | /items/{id} | Get item by ID
PUT | /items/{id} | Update item by ID
DELETE | /items/{id} | Delete item by ID
GET | / | Health check endpoint

Features Explained
🔹 Validation (models.py)
Ensures name is not empty.

Ensures price is positive.

🔹 Inheritance (service.py)
BaseService: Shared logic.

AdminItemService: Full CRUD access.

UserItemService: Read-only access, restricted from creating, updating, deleting.

🔹 Exception
Returns 404 with a message if an item is not found.




