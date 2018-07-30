from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username':'Miguel'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'Beautiful day in the neighborhood!'},
        {
            'author':{'username':'Susan'},
            'body': 'Movies are fun if theres popcorn.'}
        ]
    return render_template('index.html', title='Home', user = user, posts = posts)
