# 静的ホスト

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

# Fast API のインスタンス
app = FastAPI()

# staticフォルダ内のファイルを静的コンテンツとして配信
app.mount("/www", StaticFiles(directory="/www"))

# ルートアクセス時にindex.htmlにリダイレクト
@app.get("/")
async def root_handler():
    return RedirectResponse("/www/index.html")

# ASGI サーバを起動
if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=80)
