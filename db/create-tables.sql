CREATE TABLE IF NOT EXISTS Users (
	id int(11) AUTO_INCREMENT,
	Username varchar(255) NOT NULL,
	Level int NOT NULL,
	Score int NOT NULL,
	Gametime time NOT NULL,
	PRIMARY KEY (id)
);