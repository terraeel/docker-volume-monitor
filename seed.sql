DROP TABLE if exists volumes;
CREATE TABLE volumes (
    id INTEGER PRIMARY KEY,
    DATETIME DEFAULT (STRFTIME('%d-%m-%Y   %H:%M', 'NOW','localtime')),
	  name TEXT NOT NULL,
	  mountpoint TEXT NOT NULL,
	  size INTEGER
);