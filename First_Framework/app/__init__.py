from flask import Flask

def create_app():
    app = Flask(__name__) # Flaskアプリケーションのインスタンスを作成する

    from app.routes import api # app.routesモジュールからapiブループリントをインポートする
    app.register_blueprint(api) # apiブループリントをFlaskアプリケーションに登録する

    return app
