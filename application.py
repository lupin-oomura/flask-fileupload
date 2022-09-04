from flask import Flask , render_template, request


app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello World</h1>'


from werkzeug.utils import secure_filename
    	
@app.route('/uploads', methods=['POST', 'GET'])
def upload_file():

    return render_template('uploads.html')

    if request.method == 'POST':
        f = request.files["the_file"]
        #任意の階層をフルパスで指定(macの場合。任意のユーザー名は変更してください。)
        f.save('files/' + secure_filename(f.filename))
        #アップロードしてサーバーにファイルが保存されたらfinishedを表示
        return render_template('finished.html')
    else:
        #GETでアクセスされた時、uploadsを表示
        return render_template('uploads.html')
