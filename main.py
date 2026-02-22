from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json
from pathlib import Path

DATA_FILE = Path("items.json")

# Load existing items
if DATA_FILE.exists():
    with open(DATA_FILE) as f:
        items = json.load(f)
else:
    items = []

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Item Model
class Item(BaseModel):
    ToDo: str                                               # No default means required

# Index Page
@app.get("/index", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "items": items                                  # Sends items to html
        }
    )

# Add item to list
# '/item'
@app.post("/item")
def create_item(item: Item):
    items.append(item.dict())
    with open(DATA_FILE, "w") as file:
        json.dump(items, file)

# Shows all items
# '/items'
@app.get("/items")
def list_items():
    return items

# Get item from list
# '/items/item_id'
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    raise HTTPException(status_code=404, detail=f"Item {item_id} was not found")