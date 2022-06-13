from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

# データモデル
class ItemDataModel(BaseModel):
	data: str

app = FastAPI()
db = MongoClient('mongo', 27017).sample_db

@app.get("/")
async def health():
	return "ok"

@app.get("/items")
async def list_items():
	posts = {}
	for post in db.posts.find():
		posts[str(post['id'])] = post['data']
	return posts

@app.get("/items/{item_id}")
async def get_item(item_id: str):
	item = db.posts.find_one({"id": item_id})
	return {
		'id': item['id'],
		'data': item['data']
	}

@app.post("/items/{item_id}")
async def post_item(item_id: str, item: ItemDataModel):
	post = {
		'id': item_id,
		'data': item.data
	}
	post_id = db.posts.insert_one(post).inserted_id
	return {
		'message': 'ok'
	}

@app.put("/items/{item_id}")
async def put_item(item_id: str, item: ItemDataModel):
	return post_item(item_id, item)

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
	return db.posts.delete_one({"id": item_id})

