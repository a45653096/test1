from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello Flask'

@app.route('/test')
def test():
    return 'jojoojjojjojjojoj'


if __name__ == '__main__':
    app.run()
