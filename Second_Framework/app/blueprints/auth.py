from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth') # Blueprintのインスタンスを作成する Path='/auth'

@auth.route('/login', methods=['GET', 'POST']) # ログインページのルートを定義する
def login():
    """ログインページ"""
    # /auth/loginエンドポイントにアクセスした時に返すレスポンスを定義する
    # レスポンスに{'message': 'Login page', 'section': 'auth'}を返すことで、処理元がauthからのリクエストであることを示すことができる
    return {'message': 'Login page', 'section': 'auth'}, 200

@auth.route('/register', methods=['GET', 'POST']) # 登録ページのルートを定義する
def register():
    """登録ページ"""
    # /auth/registerエンドポイントにアクセスした時に返すレスポンスを定義する
    # レスポンスに{'message': 'Register page', 'section': 'auth'}を返すことで、処理元がauthからのリクエストであることを示すことができる
    return {'message': 'Register page', 'section': 'auth'}, 200

@auth.route('/logout') # GETメソッドのみを許可するログアウトページのルートを定義する
def logout():
    """ログアウトページ"""
    # /auth/logoutエンドポイントにアクセスした時に返すレスポンスを定義する
    # レスポンスに{'message': 'Logout page', 'section': 'auth'}を返すことで、処理元がauthからのリクエストであることを示すことができる
    return {'message': 'Logout page', 'section': 'auth'}, 200
