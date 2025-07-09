from fastapi import FastAPI, Query, Path
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Run Lab3.py (uvicorn Lab3:app --reload)
# Go to (http://127.0.0.1:8000)

# Mount static folder for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Root: HTML with 15 links
@app.get("/", response_class=HTMLResponse)
def read_root():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>FastAPI Routes</title>
      <link rel="stylesheet" href="/static/styles.css" />
    </head>
    <body>
      <div class="header">
        <h1>FastAPI Routes</h1>
      </div>
      <nav class="nav">
        <div><a href="/items/?q=test&limit=3" target="_blank">GET /items/</a><div class="link-description">Query items</div></div>
        <div><a href="/items/123" target="_blank">GET /items/123</a><div class="link-description">Item by ID</div></div>
        <div><a href="/users/?skip=0&limit=5&active=true" target="_blank">GET /users/</a><div class="link-description">Paginated users</div></div>
        <div><a href="/search/?term=fastapi" target="_blank">GET /search/</a><div class="link-description">Search by term</div></div>
        <div><a href="/users/7/items/abc" target="_blank">GET /users/{user_id}/items/{item_id}</a><div class="link-description">User item</div></div>
        <div><a href="/products/" target="_blank">GET /products/</a><div class="link-description">Optional category</div></div>
        <div><a href="/flags/?enabled=true" target="_blank">GET /flags/</a><div class="link-description">Boolean param</div></div>
        <div><a href="/orders/1001?detailed=true" target="_blank">GET /orders/{order_id}</a><div class="link-description">Order detail</div></div>
        <div><a href="/tags/?tags=red&tags=blue" target="_blank">GET /tags/</a><div class="link-description">Tag list</div></div>
        <div><a href="/events/?date=2025-06-18" target="_blank">GET /events/</a><div class="link-description">Event by date</div></div>
        <div><a href="/items/123" target="_blank">PUT /items/{item_id}</a><div class="link-description">Update item (JSON required)</div></div>
        <div><a href="/users/7" target="_blank">PUT /users/{user_id}</a><div class="link-description">Update user</div></div>
        <div><a href="/partial-item/42" target="_blank">PUT /partial-item/{item_id}</a><div class="link-description">Partial update</div></div>
        <div><a href="/orders/1001" target="_blank">PUT /orders/{order_id}</a><div class="link-description">Update order</div></div>
        <div><a href="/events/55" target="_blank">PUT /events/{event_id}</a><div class="link-description">Update event</div></div>
      </nav>
    </body>
    </html>
    """
    return html

# Route 1: GET with query params
@app.get("/items/")
def get_items(q: Optional[str] = None, limit: int = 10):
    return {"query": q, "limit": limit}

# Route 2: GET with path param
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

# Route 3: GET multiple query params
@app.get("/users/")
def get_users(skip: int = 0, limit: int = 10, active: bool = True):
    return {"skip": skip, "limit": limit, "active": active}

# Route 4: GET required query
@app.get("/search/")
def search(term: str):
    return {"term": term}

# Route 5: GET multiple path params
@app.get("/users/{user_id}/items/{item_id}")
def get_user_item(user_id: int, item_id: str):
    return {"user_id": user_id, "item_id": item_id}

# Route 6: GET optional query param
@app.get("/products/")
def get_products(category: Optional[str] = None):
    return {"category": category or "all"}

# Route 7: GET boolean query param
@app.get("/flags/")
def get_flags(enabled: bool = True):
    return {"enabled": enabled}

# Route 8: GET with path + query param
@app.get("/orders/{order_id}")
def get_order(order_id: int, detailed: bool = False):
    return {"order_id": order_id, "detailed": detailed}

# Route 9: GET with list query
@app.get("/tags/")
def get_tags(tags: Optional[List[str]] = Query(None)):
    return {"tags": tags}

# Route 10: GET with date param (as string for simplicity)
@app.get("/events/")
def get_events(date: Optional[str] = None):
    return {"date": date or "today"}

# Route 11: PUT with body
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}

# Route 12: PUT user info
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"user_id": user_id, "user": user}

# Route 13: PUT partial item
class PartialItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None

@app.put("/partial-item/{item_id}")
def partial_update(item_id: int, item: PartialItem):
    return {"item_id": item_id, "updated_fields": item.dict(exclude_unset=True)}

# Route 14: PUT update order
class OrderStatus(BaseModel):
    status: str

@app.put("/orders/{order_id}")
def update_order(order_id: int, status: OrderStatus):
    return {"order_id": order_id, "new_status": status.status}

# Route 15: PUT update event
class Event(BaseModel):
    name: str
    location: str
    attendees: int

@app.put("/events/{event_id}")
def update_event(event_id: int, event: Event):
    return {"event_id": event_id, "event": event}
