# Run the application
from app import create_app # appパッケージからcraete_app関数をインポートする

app = create_app() # create_app関数を呼び出してFlaskアプリケーションのインスタンスを作成する

if __name__ == '__main__': # Check if main
    app.run(host='0.0.0.0', port=5000, debug=True) # 実際にはFlask.run()を呼んでいる。 ()の場合はデフォルト127.0.0.1:5000で起動する
