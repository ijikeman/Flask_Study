from flask import Flask

def create_app():
    app = Flask(__name__) # Flaskアプリケーションのインスタンスを作成する

    from app.blueprints.main import main # app/blueprints/main.pyからmainをインポートする
    from app.blueprints.auth import auth # app/blueprints/auth.pyからauthをインポートする
    from app.blueprints.dashboard import dashboard # app/blueprints/dashboard.pyからdashboardをインポートする
    
    app.register_blueprint(main) # FlaskアプリケーションにmainのBlueprintを登録する
    app.register_blueprint(auth) # FlaskアプリケーションにauthのBlueprintを登録する
    app.register_blueprint(dashboard) # FlaskアプリケーションにdashboardのBlueprintを登録する
    
    return app # Flaskアプリケーションのインスタンスを返す
