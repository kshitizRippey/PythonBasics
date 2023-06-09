CREATE TABLE IF NOT EXISTS user
(
    id       integer PRIMARY KEY AUTOINCREMENT,
    username text unique,
    password text
);
