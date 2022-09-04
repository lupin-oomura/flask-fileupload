from flask import Flask , render_template, request


app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello World</h1>'


#from werkzeug.utils import secure_filename

@app.route('/uploads')
def upload_file():

    return render_template('render.html')




if __name__ == '__main__':
    app.run(debug=True)


