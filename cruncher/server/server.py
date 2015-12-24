__author__ = 'haraldfw'

import time
import sqlite3

from flask import Flask, request, redirect
from flask.globals import g
from flask.helpers import url_for, flash
from flask.templating import render_template

from model import getformula

DATABASE = 'cruncher.db'
DEBUG = True
SECRET_KEY = 'devkey'

app = Flask(__name__)
app.config.from_object(__name__)
app.config["APPLICATION_ROOT"] = "cruncher/"

@app.route('/')
def show_entries():
    games = g.db.execute('SELECT id, formula_id, timeended FROM game '
                         'ORDER BY timeended DESC LIMIT 5').fetchall()
    recentgames = []
    for row in games:
        formulaname = g.db.execute(
            'SELECT name, id FROM formula WHERE id = (?)',
            [row[1]]).fetchall()[0][0]
        recentgames.append({
            'id': row[0],
            'formulaid': row[1],
            'formulaname': formulaname,
            'timeended': row[2]
        })
    formulas = g.db.execute('SELECT id, name FROM formula').fetchall()
    topformulas = []
    for row in formulas:
        topformulas.append({
            'id': row[0],
            'name': row[1],
            'uses': len(g.db.execute('SELECT formula_id FROM game WHERE '
                                     'formula_id = (?)', [row[0]]).fetchall())
        })
    topformulas = sorted(topformulas, key=lambda k: k['uses'], reverse=True)[:5]
    return render_template('home.html', recentgames=recentgames,
                           topformulas=topformulas)


@app.route('/game/list')
def show_gamelist():
    result = g.db.execute(
        'SELECT id, timestarted, timeended, formula_id FROM game').fetchall()
    games = [dict(id=row[0], timestarted=row[1], timeended=row[2],
                  formulaid=row[3], formulaname=getformulaname(row[3]))
             for row in result]
    return render_template('game/list/list.html', games=games)


def getformulaname(formulaid):
    result = g.db.execute('SELECT name, id FROM formula WHERE id IS (?)',
                          [formulaid]).fetchall()
    if result and result[0]:
        return result[0][0]
    return "NA"


@app.route('/player/list')
def show_playerlist():
    cur = g.db.execute(
        'SELECT username, id FROM player ORDER BY username DESC')
    players = []
    for row in cur.fetchall():
        games = getgames(row[1])
        wins = getwins(row[1])
        players.append({
            'name': row[0],
            'games': games,
            'wins': wins,
            'winpercentage': str(
                round((float(wins) / float(games)) * 100, 1)) + '%'
            if games > 0 else 0
        })
    return render_template('player/list/list.html', players=players)


def getgames(playerid):
    return len(g.db.execute('SELECT player_id FROM player_game '
                            'WHERE player_id = (?)', [playerid]).fetchall())


def getwins(playerid):
    return len(g.db.execute('SELECT winner_id FROM game_winners '
                            'WHERE winner_id = (?)', [playerid]).fetchall())


@app.route('/player/profile/<playername>')
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


@app.route('/formula/list')
def show_formulalist():
    result = g.db.execute(
        'SELECT name, description, id FROM formula').fetchall()
    formulas = [dict(name=row[0], description=(row[1] if len(row[1]) < 75 else
                                               (row[1][:72] + '...')),
                     id=row[2],
                     statcount=getstatcount(row[2])) for row in result]
    return render_template('formula/list/list.html', formulas=formulas)


@app.route('/formula/def/<formulaid>')
def show_formula(formulaid):
    result = g.db.execute(
        'SELECT id, name, description FROM formula WHERE id IS (?)',
        [formulaid]).fetchall()
    if not result:
        return render_template('404.html')
    statrows = g.db.execute('SELECT * FROM stat WHERE stat.partofgame IS (?)',
                            [result[0][0]]).fetchall()
    formula = getformula(result[0], statrows)
    return render_template('formula/def/def.html', formula=formula)


def getstatcount(formulaid):
    return g.db.execute(
        'SELECT COUNT(id) FROM stat WHERE stat.partofgame IS (?)',
        [formulaid]).fetchall()[0][0]


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
    app.run(host='0.0.0.0')
