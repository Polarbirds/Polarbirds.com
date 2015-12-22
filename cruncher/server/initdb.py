__author__ = 'haraldfw'

from contextlib import closing
from server import connect_db, app


def addtestdata(db):
    addplayer(db, 'Harald', 'haraldfw@tihlde.org', '2012-12-12 12:55')
    addplayer(db, 'Gard', 'gardste@tihlde.org', '2013-03-01 13:12')
    addplayer(db, 'Trym', 'trymrt@tihlde.org', '2009-04-20 01:40')
    addplayer(db, 'Kristian', 'krishna@derp.com', '2000-06-18 15:15')

    addformula(db, 'Munchkin', 'Game definition for the game munchkin')
    addstat(db, 1, 'Level', 1, 1, 10, 1, 2)
    addstat(db, 1, 'Combat', 1, -1000, 1000, 1, 10)

    addformula(db, 'Epic munchkin', 'The epic version of the game munchkin')
    addstat(db, 2, 'Level', 1, 1, 20, 1, 5)
    addstat(db, 2, 'Combat', 1, -1000, 1000, 1, 10)
    addstat(db, 2, 'Gear', 1, 0, 1000, 1, 10)

    addgame(db, 1, '2015-04-04 23:24', '2015-04-05 04:02', 'She won')
    addgame(db, 1, '2015-04-04 22:23', '2015-04-05 02:45', 'He won')
    addgame(db, 1, '2015-04-04 22:23', '2015-04-05 02:45', 'He won')

    addplayertogame(db, 2, 1)
    addplayertogame(db, 1, 1)
    addwinner(db, 2, 1)

    addplayertogame(db, 2, 2)
    addplayertogame(db, 1, 2)
    addwinner(db, 1, 2)

    addplayertogame(db, 1, 3)
    addplayertogame(db, 2, 3)
    addplayertogame(db, 3, 3)
    addplayertogame(db, 4, 3)
    addwinner(db, 1, 3)




def addwinner(db, winner_id, game_id):
    db.execute('INSERT INTO game_winners (winner_id, game_id) VALUES (?, ?)',
               [winner_id, game_id])


def addplayertogame(db, player_id, game_id):
    db.execute('INSERT INTO player_game (player_id, game_id) VALUES (?, ?)',
               [player_id, game_id])


def addgame(db, formula_id, timestarted, timeended, windescription):
    db.execute('INSERT INTO game (formula_id, timestarted, timeended, '
               'windescription) VALUES (?, ?, ?, ?)',
               [formula_id, timestarted, timeended, windescription])


def addformula(db, name, desc):
    db.execute('INSERT INTO formula (name, description) VALUES (?, ?)',
               [name, desc])


def addstat(db, partofgame, statname, startvalue, cap_low, cap_top, increment,
            largeincrement):
    db.execute('INSERT INTO stat (partofgame, statname, startvalue, cap_low, '
               + 'cap_top, increment, largeincrement) VALUES '
               + '(?, ?, ?, ?, ?, ?, ?)',
               [partofgame, statname, startvalue, cap_low, cap_top, increment,
                largeincrement])


def addplayer(db, username, email, joined):
    db.execute('INSERT INTO player (username, email, joined) VALUES (?, ?, ?)',
               [username, email, joined])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        addtestdata(db)
        db.commit()


init_db()
