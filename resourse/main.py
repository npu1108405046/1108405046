from flask import Flask
app = Flask(__name__)

@app.route('/<int:userid>')
def hello(userid):
    return 'Hello world id = {}'.format(userid)

@app.route('/test1')
def test():
    return "test1"

if __name__ == '__main__':
    app.debug = True
    app.run("127.0.0.1",port=8000)