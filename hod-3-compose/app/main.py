# 簡易APIサーバ

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

class ItemDataModel(BaseModel):
	data: str

class MessageDataModel(BaseModel):
	message: str

app = FastAPI()
db = MongoClient('mongo', 27017).sample_db

# webサーバの動作確認
@app.get('/', response_model=MessageDataModel)
async def health():
	return MessageDataModel(message="ok")

# 登録されているアイテムのリストを取得する
@app.get('/items', response_model=dict())
async def list_items():
	posts = {}
	for post in db.posts.find():
		posts[str(post['id'])] = post['data']
	return posts

# アイテムを取得する
@app.get('/items/{item_id}')
async def read_item(item_id: str):
	item = db.posts.find_one({'id': item_id})
	return {
		'id': item['id'],
		'data': item['data']
	}

# アイテムを追加する
@app.post('/items/{item_id}', response_model=MessageDataModel)
async def create_item(item_id: str, item: ItemDataModel):
	post = {
		'id': item_id,
		'data': item.data
	}
	post_id = db.posts.insert_one(post).inserted_id
	return MessageDataModel(message="create ok")

# アイテムを更新する
@app.put('/items/{item_id}', response_model=MessageDataModel)
async def pudate_item(item_id: str, item: ItemDataModel):
	db.posts.update_one({'id': item_id}, {'$set': {'data': item.data}})
	return MessageDataModel(message="update ok")

# アイテムを削除する
@app.delete('/items/{item_id}', response_model=MessageDataModel)
async def delete_item(item_id: str):
	db.posts.delete_one({'id': item_id})
	return MessageDataModel(message="delete ok")

# ASGI サーバを起動
if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=80)
