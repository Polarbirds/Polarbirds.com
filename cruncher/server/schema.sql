DROP TABLE IF EXISTS gamematch;
DROP TABLE IF EXISTS player;

CREATE TABLE gamematch (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  FOREIGN KEY (gamedef_id) REFERENCES gamedef (id),
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
  PRIMARY KEY (game_id, stat_id),
  FOREIGN KEY (game_id) REFERENCES gamedef (id),
  FOREIGN KEY (stat_id) REFERENCES stat (id),
  value FLOAT NOT NULL
);

CREATE TABLE game_winnerrs (
  PRIMARY KEY (winner_email, game_id),
  FOREIGN KEY (winner_email) REFERENCES player (email),
  FOREIGN KEY (game_id) REFERENCES gamematch (id)
);

CREATE TABLE player_game (
  PRIMARY KEY (player_email, game_id),
  FOREIGN KEY (player_email) REFERENCES player (email),
  FOREIGN KEY (game_id) REFERENCES gamematch (id)
);
