
from flask import Flask, render_template,send_from_directory
from flask import jsonify
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "hello"

if __name__ == '__main__':
    from waitress import serve
    print("Ready at localhost:9090")
    serve(app, host="0.0.0.0", port=9090, threads=100)


    