from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'testtest'

@app.route('/test')
def hogehoge():
    return 'Now here.'

if __name__ == '__main__':
    app.run()
