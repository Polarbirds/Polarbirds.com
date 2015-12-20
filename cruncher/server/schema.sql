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
  id   INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE stat (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  statname   TEXT  NOT NULL,
  startvalue FLOAT NOT NULL,
  cap_low    FLOAT NOT NULL,
  cap_top    FLOAT NOT NULL,
  increment  FLOAT NOT NULL
);

CREATE TABLE player (
  email    TEXT PRIMARY KEY NOT NULL,
  password TEXT             NOT NULL, -- Temporary!!
  name     TEXT             NOT NULL,
  joined   DATE             NOT NULL
);

CREATE TABLE gamedef_stat (
  game_id REFERENCES gamedef (id),
  stat_id REFERENCES stat (id),
  value FLOAT NOT NULL
);

CREATE TABLE game_winners (
  winner_email REFERENCES player (email),
  game_id REFERENCES gamematch (id)
);

CREATE TABLE player_game (
  player_email REFERENCES player (email),
  game_id REFERENCES gamematch (id)
);
