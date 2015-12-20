import sqlite3
from contextlib import closing

from flask import Flask, jsonify, make_response, request, redirect
from flask.globals import g
from flask.helpers import url_for, flash
from flask.templating import render_template

DATABASE = 'D:\\dev\\repos\\Polarbirds.com\\cruncher\\cruncher.db'
DEBUG = True
SECRET_KEY = 'devkey'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def show_entries():
    cur = g.db.execute('SELECT email, name FROM player ORDER BY email DESC')
    entries = [dict(email=row[0], name=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    email = request.form['email']
    if email and name:
        g.db.execute('INSERT INTO player (email, password, name, joined) VALUES (?, ?, ?, ?)',
                     [email, 'badpw', name, '1995-12-12 12:55'])
        g.db.commit()
        flash('New entry was successfully posted')
    else:
        flash('Please fill both fields')
    return redirect(url_for('show_entries'))


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


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
