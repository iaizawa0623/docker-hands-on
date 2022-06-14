# ベースイメージの指定
FROM ubuntu

# 作業フォルダの指定
WORKDIR /

# 実行環境を構築
RUN apt update -y && apt install python3 -y

# プログラムをコピー
COPY app.py index.html /

# アプリを実行
ENTRYPOINT [ "python3", "/app.py" ]
