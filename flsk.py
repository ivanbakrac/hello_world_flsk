from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def hello_world(name):
    return "Hello {}".format(name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)



# or localhost:8081
