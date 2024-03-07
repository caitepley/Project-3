CREATE TABLE Items(
	item_id INT PRIMARY KEY,
title VARCHAR(500),
collection_id integer,
description VARCHAR(1000),
physical_description VARCHAR(1000),
url VARCHAR(100),
institution_id integer,
creator_id integer,
publisher_id integer,
dewey_dec_code integer,
type_id integer,
place_id integer,
lang_id integer,
date DATE
);

CREATE TABLE Collection (
    collection_id INT PRIMARY KEY,
    collection VARCHAR(100)

);

CREATE TABLE Institution(
	institution_id INT PRIMARY KEY ,
	institution VARCHAR(100)
);

CREATE TABLE Creator(
	creator_id INT PRIMARY KEY ,
	creator_name VARCHAR(50),
	type VARCHAR(50)
);

CREATE TABLE Publisher(
	publisher_id INT PRIMARY KEY ,
	publisher VARCHAR(100)
);

CREATE TABLE Dewey(
	dewey_dec_code INT PRIMARY KEY ,
	genre VARCHAR(50)
);

CREATE TABLE Subject(
	subject_id INT PRIMARY KEY ,
	subject VARCHAR(50),
	item_id INT
);

CREATE TABLE Type (
	type_id INT PRIMARY KEY ,
	type VARCHAR(50)
);

CREATE TABLE Place (
	place_id INT PRIMARY KEY ,
	place VARCHAR(50)
);

CREATE TABLE Language (
	lang_id INT PRIMARY KEY ,
	lang VARCHAR(30)
);

ALTER TABLE Items
ADD CONSTRAINT fk_collection_id
FOREIGN KEY (collection_id) REFERENCES Collection(collection_id);

ALTER TABLE Items
ADD CONSTRAINT fk_institution_id
FOREIGN KEY (institution_id) REFERENCES Institution(institution_id);

ALTER TABLE Items
ADD CONSTRAINT fk_creator_id
FOREIGN KEY (creator_id) REFERENCES Creator(creator_id);

ALTER TABLE Items
ADD CONSTRAINT fk_publisher_id
FOREIGN KEY (publisher_id) REFERENCES Publisher(publisher_id);

ALTER TABLE Items
ADD CONSTRAINT fk_dewey_dec_code
FOREIGN KEY (dewey_dec_code) REFERENCES Dewey(dewey_dec_code);

ALTER TABLE Items
ADD CONSTRAINT fk_type_id
FOREIGN KEY (type_id) REFERENCES Type(type_id);

ALTER TABLE Items
ADD CONSTRAINT fk_place_id
FOREIGN KEY (place_id) REFERENCES Place(place_id);

ALTER TABLE Items
ADD CONSTRAINT fk_lang_id
FOREIGN KEY (lang_id) REFERENCES Language(lang_id);

-- Drop Subject table
DROP TABLE IF EXISTS Subject;

CREATE TABLE Subject (
    subject_id INT PRIMARY KEY,
    item_id INT,
    subject VARCHAR(50),
    FOREIGN KEY (item_id) REFERENCES Items(item_id)
);
