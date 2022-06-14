# ベースイメージを指定
FROM python:3.10.5

# 作業フォルダを指定
WORKDIR /

# プログラムと依存関係パッケージファイルをコピー
COPY main.py requirements.txt /

# 依存関係パッケージをインストール
RUN pip install -r /requirements.txt

# 開放ポートを明示
EXPOSE 80

# プログラムを実行
ENTRYPOINT [ "python3", "main.py" ]
