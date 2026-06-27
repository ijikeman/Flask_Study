from flask import Blueprint
from app.view import hello

api = Blueprint('api', __name__) # Blueprintのインスタンスを作成する
# BlueprintはFlaskでルート機能を分割して管理するための仕組みで、複数のルートをまとめて登録することができる

api.add_url_rule('/hello', 'hello', hello, methods=['GET']) # /helloエンドポイントを定義する
# 以下のようにview.pyに分けて書かずに`1つのファイルに書くこともできる`
# @api.route('/hello', methods=['GET']) # /helloエンドポイントを定義する
# def hello():
#     return 'Hello, World!' # /helloエンドポイントにアクセスしたときに返すレスポンスを定義する
