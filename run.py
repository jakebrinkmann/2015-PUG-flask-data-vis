from flask import Flask, url_for

app = Flask(__name__)

@app.route('/proj')
def projects():
    return '<h1>Project Page</h1><p><ul><li>PUG Data Visualization</li></ul></p>'


@app.route('/')
def hello_world():
    return '<a href="'+ url_for('projects') +'">Projects Page</a>'

if __name__ == '__main__':
    app.run()
