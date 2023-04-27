from flask import Flask, escape

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


@app.route("/about/")  # trailing slash
def about():
    return "<h2>About me</h2>"


@app.route("/example/", methods=['GET', 'POST'])
def example():
    return "<h3>Example</h3>"


@app.route("/stocks/")
def stocks():
    return "<h4>Stocks</h4>"


@app.route("/hello/<name>/")
def hello(name):
    # escape is used to prevent XSS attacks
    return f"<h5>Hello, {escape(name)}!</h5>"


@app.route("/blog/<int:postID>/")
def show_blog(postID):
    return f"Blog Number: #{escape(postID)}"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
