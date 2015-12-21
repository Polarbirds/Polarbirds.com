import time

__author__ = 'haraldfw'

import sqlite3

from flask import Flask, jsonify, make_response, request, redirect
from flask.globals import g
from flask.helpers import url_for, flash
from flask.templating import render_template

DATABASE = 'cruncher.db'
DEBUG = True
SECRET_KEY = 'devkey'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def show_entries():
    cur = g.db.execute('SELECT email, username, joined FROM player ORDER BY username DESC')
    entries = [dict(email=row[0], name=row[1], joined=row[2]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/playerprofile/<playername>')
def show_player(playername):
    cur = g.db.execute('SELECT username FROM player')
    if not cur.fetchall():
        return render_template('playerprofile/404.html')
    cur = g.db.execute('SELECT username FROM player WHERE username IS (?)', [playername])
    entries = [dict(email=row[0]) for row in cur.fetchall()]
    return render_template('playerprofile/profile.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    email = request.form['email']
    if email and name:
        addplayer(email, 'pw', name, time.strftime('%Y-%m-%d %H:%M'))
        flash('New entry was successfully posted')
    else:
        flash('Please fill both fields')
    return redirect(url_for('show_entries'))


def addplayer(email, password, name, joined):
    g.db.execute('INSERT INTO player (email, username, joined) VALUES (?, ?, ?, ?)',
                 [email, password, name, joined])
    g.db.commit()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
