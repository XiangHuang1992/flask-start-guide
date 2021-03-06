from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('add.html')


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/add')
def add():
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
    