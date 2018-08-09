"""
A Journal Web App built with Flask
Author: Zachary Collins
Date: August, 2018
"""

from flask import (Flask, g, render_template, flash, redirect, url_for,
                   abort)

import forms
import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'auoesh.bouoastuh.43,uoausoehuosth3ououea.auoub!'


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DB
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


@app.route('/')
def index():
    """The Homepage of the app, shows all posts"""

    posts = models.Post.select()
    return render_template('index.html', posts=posts)


@app.route('/entries')
def entries():
    """Shows all of the journal entries"""

    posts = models.Post.select()
    return render_template('index.html', posts=posts)


@app.route('/details/<int:post_id>')
def view_post(post_id):
    """Views a specific journal post"""

    posts = models.Post.select().where(models.Post.id == post_id)
    if posts.count() == 0:
        abort(404)
    return render_template('detail.html', posts=posts)


@app.route('/details/<int:post_id>/edit', methods=('GET', 'POST'))
def edit_post(post_id):
    """allows the user to edit a specific post"""

    form = forms.PostForm()
    posts = models.Post.select().where(models.Post.id == post_id)
    if posts.count() == 0:
        abort(404)
    elif form.validate_on_submit():
        models.Post.create(title=form.title.data,
                           date=form.date.data,
                           time_spent=form.time_spent.data,
                           details=form.details.data,
                           remember=form.remember.data)
        models.Post.get(models.Post.id == post_id).delete_instance()
        return redirect(url_for('index'))
    return render_template('edit.html', posts=posts, form=form)


@app.route('/details/<int:post_id>/delete', methods=('GET', 'POST'))
def delete_post(post_id):
    """Allows the user to see delete a specific post"""

    posts = models.Post.select().where(models.Post.id == post_id)
    if posts.count() == 0:
        abort(404)
    models.Post.get(models.Post.id == post_id).delete_instance()
    return redirect(url_for('index'))


@app.route('/new_post', methods=('GET', 'POST'))
def post():
    """Prompts the form, allowing a user to create a new post"""

    form = forms.PostForm()
    if form.validate_on_submit():
        models.Post.create(title=form.title.data,
                           date=form.date.data,
                           time_spent=form.time_spent.data,
                           details=form.details.data,
                           remember=form.remember.data)
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)

