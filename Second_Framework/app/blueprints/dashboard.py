from flask import Blueprint

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard') # Blueprintのインスタンスを作成する Path='/dashboard'

@dashboard.route('/')
def index():
    """ダッシュボードのホームページ"""
    return {'message': 'Dashboard Home', 'section': 'dashboard'}, 200 # /dashboardエンドポイントにアクセスしたときに返すレスポンスを定義する

@dashboard.route('/profile')
def profile():
    """プロフィールページ"""
    return {'message': 'User Profile', 'section': 'dashboard'}, 200 # /dashboard/profileエンドポイントにアクセスしたときに返すレスポンスを定義する

@dashboard.route('/settings')
def settings():
    """設定ページ"""
    return {'message': 'Settings', 'section': 'dashboard'}, 200 # /dashboard/settingsエンドポイントにアクセスしたときに返すレスポンスを定義する
