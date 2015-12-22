from model import getformula

__author__ = 'haraldfw'

import time
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
    cur = g.db.execute(
        'SELECT username FROM player ORDER BY username DESC')
    entries = [dict(name=row[0]) for row in
               cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/playerprofile/<playername>')
def show_player(playername):
    result = g.db.execute(
        'SELECT id, joined FROM player WHERE username IS (?)',
        [playername]).fetchall()
    if not result:
        return render_template('404.html')
    stats = {
        'name': playername,
        'id': result[0][0],
        'joined': result[0][1],
    }
    return render_template('player/profile/profile.html', entries=stats)


@app.route('/formula/<formulaid>')
def show_formula(formulaid):
    result = g.db.execute(
        'SELECT * FROM formula WHERE id IS (?)',
        [formulaid]).fetchall()
    if not result:
        return render_template('404.html')
    statrows = g.db.execute('SELECT * FROM stat WHERE stat.partofgame IS (?)',
                            [result[0]]).fetchall()
    formula = getformula(result, statrows)
    return render_template('player/profile/profile.html', entries=formula)


@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    email = request.form['email']
    if email and name:
        addplayer(email, name, time.strftime('%Y-%m-%d %H:%M'))
        flash('New entry was successfully posted')
    else:
        flash('Please fill both fields')
    return redirect(url_for('show_entries'))


def addplayer(email, name, joined):
    g.db.execute(
        'INSERT INTO player (email, username, joined) VALUES (?, ?, ?)',
        [email, name, joined])
    g.db.commit()


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


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
