# 目的
* Flaskの基本を学ぶ

# 構築順
1. run.py
```
__init__.pyに記載されているFlaskインスタンスを作成し
app.run() = Flask.run()でサーバを起動している
```
2. app/__init__.py
```
Flaskをインスタンスとして作成して返す
```
3. app/routes.py
```
/hello URLエンドポイントを作成し、どの関数へ処理を飛ばすかを定義
```
4. app/view.py
```
def hello():で/helloにアクセスしたときの処理を記載
```

# 起動方法
```
python3 -m venv .venv
source .venv/bin/activate
python3 install -r requirements.txt
pytyon3 run.py
```

# アクセス方法
```
curl http://localhost:5000/hello
Hello, World!
```
