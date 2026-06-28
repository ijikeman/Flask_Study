# 目的

Factory パターンと Blueprint を使用したモジュール化されたアプリケーション構成を学ぶ

# Blueprint ルーティング設計パターン

## パターン A：各 Blueprint 内にルーティング定義（推奨）
```
app/blueprints/main.py       → main blueprint + main のルート定義
app/blueprints/auth.py       → auth blueprint + auth のルート定義
app/blueprints/dashboard.py  → dashboard blueprint + dashboard のルート定義
```

**メリット**
- 機能ごとにファイルが独立している
- 大規模プロジェクトへの拡張が容易
- Flask の標準的なベストプラクティス

**デメリット**
- ファイル数が増えて管理が複雑

---

## パターン B：app/routes.py に統一管理
```
app/routes.py → 全ての blueprint 定義 + 全ての route 定義を一元管理
```

**メリット**
- 全ルーティングをロジックが一ヶ所に集約されている
- シンプルで学習しやすい

**デメリット**
- routes.py が肥大化する
- 規模が大きくなると管理が困難

# ディレクトリ構成
```
app/
  blueprints/
  ├── __init__.py
  ├── main.py
  ├── auth.py
  └── dashboard.py
run.py
```

# 実装

## ステップ 1：app/blueprints/main.py を実装

### 内容
```python
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    """ホームページ"""
    return {'message': 'Welcome to Flask App!'}, 200

@main.route('/about')
def about():
    """アバウトページ"""
    return {'message': 'About page'}, 200
```

### ポイント
- `url_prefix` を指定しない → ルートが `/` から始まる
- `/` と `/about` の 2 つのエンドポイント

---

## ステップ 2：app/__init__.py の create_app() を作成

### 内容
```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.blueprints.main import main

    app.register_blueprint(main)

    return app
```

### ポイント
- `main` blueprint をインポート
- `app.register_blueprint()` で blueprint を登録

## ステップ 2-2：テスト

起動コマンド：
```bash
cd /config/workspace/git/Flask_Study/Second_Framework
python3 run.py
```

テスト対象のエンドポイント：

### Main Blueprint
- `http://localhost:5000/` → 200 OK (Home)
- `http://localhost:5000/about` → 200 OK (About)

## ステップ 3：app/blueprints/auth.py を実装

### 内容
```python
from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """ログインページ"""
    return {'message': 'Login page', 'section': 'auth'}, 200

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """登録ページ"""
    return {'message': 'Register page', 'section': 'auth'}, 200

@auth.route('/logout')
def logout():
    """ログアウトページ"""
    return {'message': 'Logout page', 'section': 'auth'}, 200
```

### ポイント
- `url_prefix='/auth'` を指定 → すべてのルートが `/auth` から始まる
- `/auth/login`, `/auth/register`, `/auth/logout` の 3 つのエンドポイント
- `methods` パラメータで許可する HTTP メソッドを指定

---

## ステップ 4：app/__init__.py の create_app() を修正

### 内容
```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.blueprints.main import main
    from app.blueprints.auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
```

### ポイント
- `auth` blueprint をインポート
- `app.register_blueprint()` で blueprint を登録
- 登録順序は任意


## ステップ 4-2：テスト

起動コマンド：
```bash
cd /config/workspace/git/Flask_Study/Second_Framework
python3 run.py
```

テスト対象のエンドポイント：

### Auth Blueprint
- `http://localhost:5000/auth/login` → 200 OK (Login)
- `http://localhost:5000/auth/register` → 200 OK (Register)
- `http://localhost:5000/auth/logout` → 200 OK (Logout)


---

## ステップ 5：app/blueprints/dashboard.py を実装

### 内容
```python
from flask import Blueprint

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.route('/')
def index():
    """ダッシュボードトップ"""
    return {'message': 'Dashboard Home', 'section': 'dashboard'}, 200

@dashboard.route('/profile')
def profile():
    """プロフィールページ"""
    return {'message': 'User Profile', 'section': 'dashboard'}, 200

@dashboard.route('/settings')
def settings():
    """設定ページ"""
    return {'message': 'Settings', 'section': 'dashboard'}, 200
```

### ポイント
- `url_prefix='/dashboard'` を指定 → すべてのルートが `/dashboard` から始まる
- `/dashboard/`, `/dashboard/profile`, `/dashboard/settings` の 3 つのエンドポイント

---

## ステップ 6：app/__init__.py の create_app() を再修正（全 blueprint 登録）

### 内容
```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.blueprints.main import main
    from app.blueprints.auth import auth
    from app.blueprints.dashboard import dashboard

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(dashboard)

    return app
```

### ポイント
- 3 つの blueprint すべてをインポート
- 3 つの blueprint すべてを登録
- これで全機能が統合される

---

## ステップ 6-2：テスト

起動コマンド：
```bash
cd /config/workspace/git/Flask_Study/Second_Framework
python3 run.py
```

テスト対象のエンドポイント：

### Dashboard Blueprint
- `http://localhost:5000/dashboard/` → 200 OK (Dashboard Home)
- `http://localhost:5000/dashboard/profile` → 200 OK (Profile)
- `http://localhost:5000/dashboard/settings` → 200 OK (Settings)

---

## まとめ

このプロジェクトで学んだこと：
- **App Factory パターン**：`create_app()` でアプリケーションを再利用可能なファクトリとして定義
- **Blueprint パターン**：機能ごとに blueprint を分割し、モジュール化
- **url_prefix**：blueprint の共通パスプレフィックスを設定
- **方法の選択**：HTTP メソッドを指定して、GET/POST などを制御
- **スケーラビリティ**：大規模プロジェクトにも対応できる構成
