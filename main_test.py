from flask import Flask

app = Flask(__name__)

@app.route ('/')
def hello():
    return '<html><body><h1>test</h1></body></html>'

if __name__ == '__main__':
    app.run() 
