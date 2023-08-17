from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<h4>Hello, World!</h4>'


@app.route('/about')
def about():
    return '<h4>about page, World!</h4>'


if __name__ == '__main__':
    app.run(debug=True)
