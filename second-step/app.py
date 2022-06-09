from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()

app.mount("/www", StaticFiles(directory="www"))

@app.get("/")
async def redirect_typer():
    return RedirectResponse("/www/index.html")

@app.get("/hello")
async def hello():
	return {
		"message": "Hello, world!"
	}

class Item(BaseModel):
	name: str

@app.post("/item")
async def test(item: Item):
	return item

