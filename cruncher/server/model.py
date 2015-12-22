__author__ = 'haraldfw'


def getstat(row):
    return {
        'id': row[0],
        'partofgame': row[1],
        'statname': row[2],
        'startvalue': row[3],
        'cap_low': row[4],
        'cap_top': row[5],
        'increment': row[6],
        'largeincrement': row[7]
    }


def getformula(row, statrows):
    stats = []
    for statrow in statrows:
        stats.append(getstat(statrow))
    return {
        'id': row[0],
        'name': row[1],
        'description': row[2],
        'stats': stats
    }


def getgame(row, formula, players, winners, playerstats):
    return {
        'id': row[0],
        'formula': formula,
        'timestarted': row[2],
        'timeended': row[3],
        'windescription': row[4],
        'players': players,
        'winners': winners,
        'playerstats': playerstats
    }


def getplayer(row):
    return {
        'id': row[0],
        'username': row[1],
        'email': row[2],
        'joined': row[3],
    }
