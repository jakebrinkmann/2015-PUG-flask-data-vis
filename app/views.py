from flask import render_template
from app import app

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/<username>')
@app.route('/index/<username>')
def index(username):
    user = {'nickname': username}
    return render_template('index.html',
                           title='Home',
                           user=user)
