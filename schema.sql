DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS col_mapping;
DROP TABLE IF EXISTS creator_id;
DROP TABLE IF EXISTS creator_type_id;
DROP TABLE IF EXISTS creator_type_item;
DROP TABLE IF EXISTS dewey;
DROP TABLE IF EXISTS ins_mapping;
DROP TABLE IF EXISTS item_codes;
DROP TABLE IF EXISTS lang_item;
DROP TABLE IF EXISTS languages_id;
DROP TABLE IF EXISTS place_id;
DROP TABLE IF EXISTS place_item;
DROP TABLE IF EXISTS pub_mapping;
DROP TABLE IF EXISTS subject_id;
DROP TABLE IF EXISTS subject_item;



CREATE TABLE col_mapping (
	col_id varchar(10) PRIMARY KEY,
	collection VARCHAR(1000)
);

CREATE TABLE creator_id (
    creator VARCHAR(1000),
	creator_id int PRIMARY KEY
);

CREATE TABLE creator_type_id (
    type VARCHAR(1000),
	creator_type_id int PRIMARY KEY
);

CREATE TABLE creator_type_item (
    item_id int,
	creator_type_id int,
	creator_id int,
	PRIMARY KEY (item_id,creator_id,creator_type_id)
);

CREATE TABLE dewey(
	dewey_dec_code VARCHAR(15) PRIMARY KEY,
	genre VARCHAR(200)
);

CREATE TABLE ins_mapping (
	ins_key VARCHAR(10) PRIMARY KEY,
	institution VARCHAR(1000)
);

CREATE TABLE item_codes(
	item_type VARCHAR(10),
	item VARCHAR(100) PRIMARY KEY
);

CREATE TABLE lang_item (
    item_id int,
	lang_id INT,
	PRIMARY KEY(item_id,lang_id)
);


CREATE TABLE languages_id (
    lang VARCHAR(1000),
	lang_id INT PRIMARY KEY
);

CREATE TABLE place_id (
    place VARCHAR(1000),
	place_id INT PRIMARY KEY
);

CREATE TABLE place_item (
    item_id int,
	place_id INT,
	PRIMARY KEY(item_id, place_id)
);


CREATE TABLE pub_mapping (
	pub_key varchar(10) PRIMARY KEY,
	publisher VARCHAR(1000)
);

CREATE TABLE subject_id (
    subject VARCHAR(1000),
	subject_id INT PRIMARY KEY
);

CREATE TABLE subject_item (
    item_id int,
	subject_id int,
	PRIMARY KEY (item_id, subject_id)
);

CREATE TABLE items(
	title VARCHAR(1000),
	col VARCHAR(1000),
	wdl_url VARCHAR(1000),
	ins_key VARCHAR(300),
	pub_key VARCHAR(300),
	dewey_dec_code VARCHAR(15),
	type_id VARCHAR(10),
	date VARCHAR(100),
	item_id INT PRIMARY KEY
);

SELECT * FROM items;
SELECT * FROM col_mapping;
SELECT * FROM creator_id;
SELECT * FROM creator_type_id;
SELECT * FROM creator_type_item;
SELECT * FROM dewey;
SELECT * FROM ins_mapping;
SELECT * FROM item_codes;
SELECT * FROM lang_item;
SELECT * FROM languages_id;
SELECT * FROM place_id;
SELECT * FROM place_item;
SELECT * FROM pub_mapping;
SELECT * FROM subject_id;
SELECT * FROM subject_item;

