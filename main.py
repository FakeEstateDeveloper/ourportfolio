from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Item Model
class Item(BaseModel):
    ToDo: str                   # No default means required

items = []

# Index Page
@app.get("/index", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "items": items      # Sends items to html
        }
    )

# GET
# ====
# Shows all items up to limit
# '/items'
@app.get("/items", response_model=list[Item])
def list_items(limit: int=10):
    return items[0:limit]

# Get item from list
# '/items/item_id'
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    raise HTTPException(status_code=404, detail=f"Item {item_id} was not found")

# POST
# ====
# Add item to list
# '/item'
@app.post("/item")
def create_item(item: Item):
    items.append(item)
    return items