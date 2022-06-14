# ベースイメージの指定
FROM python:3.10.5

# 作業フォルダの指定
WORKDIR /

# プログラムと依存関係パッケージファイルをコピー
COPY main.py requirements.txt /

# 依存関係パッケージをインストール
RUN pip install -r /requirements.txt

# 開放ポートを明示
EXPOSE 80

# アプリを実行
ENTRYPOINT [ "python3", "main.py" ]
