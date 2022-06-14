# ベースイメージを指定
FROM python:3.10.5-apline

# 作業フォルダを指定
WORKDIR /

# app/をルートにコピー
COPY app/ /

# 依存関係パッケージをインストール
RUN pip install -r requirements.txt

# 開放ポートを明示
EXPOSE 80

# プログラムを実行
ENTRYPOINT [ "python3", "main.py" ]
