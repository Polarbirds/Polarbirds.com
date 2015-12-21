DROP TABLE IF EXISTS player_game_stat;
DROP TABLE IF EXISTS player_game;
DROP TABLE IF EXISTS game_winners;
DROP TABLE IF EXISTS gamedef_stat;
DROP TABLE IF EXISTS gamematch;
DROP TABLE IF EXISTS gamedef;
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS stat;

CREATE TABLE gamematch (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  gamedef_id REFERENCES gamedef (id),
  timestarted    DATE NOT NULL,
  timeended      DATE NOT NULL,
  windescription TEXT NOT NULL
);

CREATE TABLE gamedef (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  name        TEXT NOT NULL,
  description TEXT
);

CREATE TABLE stat (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  partofgame REFERENCES gamedef (id),
  statname       TEXT  NOT NULL,
  startvalue     FLOAT NOT NULL,
  cap_low        FLOAT NOT NULL,
  cap_top        FLOAT NOT NULL,
  increment      FLOAT NOT NULL,
  largeincrement FLOAT NOT NULL
);

CREATE TABLE player (
  id       INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  email    TEXT        NOT NULL,
  joined   DATE        NOT NULL
);

CREATE TABLE game_winners (
  winner_id REFERENCES player (id),
  game_id REFERENCES gamematch (id),
  PRIMARY KEY (winner_id, game_id)
);

CREATE TABLE player_game (
  player_id REFERENCES player (id),
  game_id REFERENCES gamematch (id),
  PRIMARY KEY (player_id, game_id)
);

CREATE TABLE player_game_stat (
  player_id REFERENCES player (id),
  game_id REFERENCES gamematch (id),
  statname TEXT  NOT NULL,
  number   FLOAT NOT NULL,
  PRIMARY KEY (player_id, game_id, statname)
);
