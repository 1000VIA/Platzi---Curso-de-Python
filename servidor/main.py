from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
    return '<h4>Hello word, this is my firs server in python</h4>'

if __name__ == '__main__':
    app.run()