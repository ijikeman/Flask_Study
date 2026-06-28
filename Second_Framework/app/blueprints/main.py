# FlaskクラスのBlueprintをインポートする
from flask import Blueprint

main = Blueprint('main', __name__) # Blueprintのインスタンスを作成する

@main.route('/')
def home():
    """ホームページ"""
    return{'message': 'Welcome to Flask App!'}, 200 # /エンドポイントにアクセスしたときに返すレスポンスを定義する

@main.route('/about')
def about():
    """アバウトページ"""
    return {'message': 'This is the about page.'}, 200 # /aboutエンドポイントにアクセスしたときに返すレスポンスを定義する
