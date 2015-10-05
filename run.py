from flask import Flask

app = Flask(__name__)

@app.route('/')
def create_error():
    return 'a %s' % a

if __name__ == '__main__':
    app.run(debug=True)
