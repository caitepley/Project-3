import sqlite3
import pandas as pd

from pathlib import Path

database_path = "Resources/project_3.sqlite"
Path(database_path).touch()

conn = sqlite3.connect(database_path)
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS col_mapping''')
c.execute('''DROP TABLE IF EXISTS creator_id''')
c.execute('''DROP TABLE IF EXISTS creator_type_id''')
c.execute('''DROP TABLE IF EXISTS creator_type_item''')
c.execute('''DROP TABLE IF EXISTS dewey''')
c.execute('''DROP TABLE IF EXISTS ins_mapping''')
c.execute('''DROP TABLE IF EXISTS item_codes''')
c.execute('''DROP TABLE IF EXISTS items''')
c.execute('''DROP TABLE IF EXISTS lang_item''')
c.execute('''DROP TABLE IF EXISTS languages_id''')
c.execute('''DROP TABLE IF EXISTS place_id''')
c.execute('''DROP TABLE IF EXISTS place_item''')
c.execute('''DROP TABLE IF EXISTS pub_mapping''')
c.execute('''DROP TABLE IF EXISTS subject_id''')
c.execute('''DROP TABLE IF EXISTS subject_item''')

c.execute('''CREATE TABLE col_mapping ( col varchar(10) PRIMARY KEY,
	collection VARCHAR(1000))''')

csv_col_mapping = pd.read_csv("Resources/col_mapping_new.csv")
csv_col_mapping.to_sql("col_mapping", conn, if_exists='append', index=False)


c.execute('''CREATE TABLE creator_id ( creator VARCHAR(1000),
	creator_id int PRIMARY KEY)''')

csv_creator_id = pd.read_csv("Resources/creator_id.csv")
csv_creator_id.to_sql("creator_id", conn, if_exists='append', index=False)


c.execute('''CREATE TABLE creator_type_id (type VARCHAR(1000),
	creator_type_id int PRIMARY KEY)''')

csv_creator_type_id = pd.read_csv("Resources/creator_type_id.csv")
csv_creator_type_id.to_sql("creator_type_id", conn, if_exists='append', index=False)


c.execute('''CREATE TABLE creator_type_item (item_id int,
	creator_type_id int,
	creator_id int,
	PRIMARY KEY (item_id,creator_id,creator_type_id))''')

csv_creator_type_item = pd.read_csv("Resources/creator_type_item.csv")
csv_creator_type_item.to_sql("creator_type_item", conn, if_exists='append', index=False)

c.execute('''CREATE TABLE dewey (dewey_dec_code VARCHAR(15) PRIMARY KEY,
	genre VARCHAR(200))''')

csv_dewey = pd.read_csv("Resources/dewey.csv")
csv_dewey.to_sql("dewey", conn, if_exists='append', index=False)


c.execute('''CREATE TABLE ins_mapping (ins_key VARCHAR(10) PRIMARY KEY,
	institution VARCHAR(1000))''')

csv_ins_mapping = pd.read_csv("Resources/ins_mapping_new.csv")
csv_ins_mapping.to_sql("ins_mapping", conn, if_exists='append', index=False)


c.execute('''CREATE TABLE item_codes (item_code VARCHAR(10),
	item VARCHAR(100)  PRIMARY KEY)''')

csv_item_codes = pd.read_csv("Resources/item_codes_new.csv")
csv_item_codes.to_sql("item_codes", conn, if_exists='append', index=False)


c.execute('''CREATE TABLE items ( title VARCHAR(1000),
	col VARCHAR(1000),
	wdl_url VARCHAR(1000),
	ins_key VARCHAR(300),
	pub_key VARCHAR(300),
	dewey_dec_code VARCHAR(15),
	type_id VARCHAR(10),
	date VARCHAR(100),
	item_id INT PRIMARY KEY)''')

csv_items = pd.read_csv("Resources/items_csv.csv")
csv_items.to_sql("items", conn, if_exists='append', index=False)


c.execute('''CREATE TABLE lang_item (item_id int,
	lang_id INT,
	PRIMARY KEY(item_id,lang_id))''')

csv_lang_item = pd.read_csv("Resources/lang_item.csv")
csv_lang_item.to_sql("lang_item", conn, if_exists='append', index=False)


c.execute('''CREATE TABLE languages_id (lang VARCHAR(1000)PRIMARY KEY ,
	lang_id INT )''')

csv_languages_id = pd.read_csv("Resources/languages_id.csv")
csv_languages_id.to_sql("languages_id", conn, if_exists='append', index=False)


c.execute('''CREATE TABLE place_id (place VARCHAR(1000)PRIMARY KEY ,
	place_id INT )''')

csv_place_id = pd.read_csv("Resources/place_id.csv")
csv_place_id.to_sql("place_id", conn, if_exists='append', index=False)


c.execute('''CREATE TABLE place_item (item_id int,
	place_id INT,
	PRIMARY KEY(item_id, place_id))''')

csv_place_item = pd.read_csv("Resources/place_item.csv")
csv_place_item.to_sql("place_item", conn, if_exists='append', index=False)

c.execute('''CREATE TABLE pub_mapping (pub_key varchar(10) PRIMARY KEY,
	publisher VARCHAR(1000))''')

csv_pub_mapping = pd.read_csv("Resources/pub_mapping_new.csv")
csv_pub_mapping.to_sql("pub_mapping", conn, if_exists='append', index=False)


c.execute('''CREATE TABLE subject_id (subject VARCHAR(1000),
	subject_id INT PRIMARY KEY)''')

csv_subject_id = pd.read_csv("Resources/subject_id.csv")
csv_subject_id.to_sql("subject_id", conn, if_exists='append', index=False)


c.execute('''CREATE TABLE subject_item (item_id int,
	subject_id int,
	PRIMARY KEY (item_id, subject_id))''')

csv_subject_item = pd.read_csv("Resources/subject_item.csv")
csv_subject_item.to_sql("subject_item", conn, if_exists='append', index=False)


conn.close()