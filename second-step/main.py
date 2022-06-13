from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

# データモデル
class ItemDataModel(BaseModel):
	data: str

app = FastAPI()
db = MongoClient('mongo', '27017').sample_db

@app.get("/")
async def hello():
	return {
		"message", "hello"
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

@app.get("/items")
async def list_items():
	posts = {}
	for post in db.posts.find():
		posts[str(post['id'])] = post['data']
	return posts
