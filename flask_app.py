# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# create the engine
engine = create_engine("sqlite:///Resources/project_3.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
print(dir(Base.classes))
col_mapping = Base.classes.col_mapping
creator_id = Base.classes.creator_id
creator_type_id = Base.classes.creator_type_id
creator_type_item = Base.classes.creator_type_item
dewey = Base.classes.dewey
ins_mapping = Base.classes.ins_mapping
item_codes = Base.classes.item_codes
items = Base.classes.items
lang_item = Base.classes.lang_item
languages_id = Base.classes.languages_id
place_id = Base.classes.place_id
place_item = Base.classes.place_item
pub_mapping = Base.classes.pub_mapping
subject_id = Base.classes.subject_id
subject_item = Base.classes.subject_item


# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    #List all available api routes.
    return (
        f"Available Routes:<br/>"
        f"<a href=\"/api/v1.0/col_mapping\">/api/v1.0/col_mapping</a><br/>"
        f"<a href=\"/api/v1.0/creator_id\">/api/v1.0/creator_id</a><br/>"
        f"<a href=\"/api/v1.0/creator_type_id\">/api/v1.0/creator_type_id</a><br/>"
        f"<a href=\"/api/v1.0/creator_type_item\">/api/v1.0/creator_type_item</a><br/>"
        f"<a href=\"/api/v1.0/dewey\">/api/v1.0/dewey</a><br/>"
        f"<a href=\"/api/v1.0/ins_mapping\">/api/v1.0/ins_mapping</a><br/>"
        f"<a href=\"/api/v1.0/item_codes\">/api/v1.0/item_codes</a><br/>"
        f"<a href=\"/api/v1.0/items\">/api/v1.0/items</a><br/>"
        f"<a href=\"/api/v1.0/lang_item\">/api/v1.0/lang_item</a><br/>"
        f"<a href=\"/api/v1.0/languages_id\">/api/v1.0/languages_id</a><br/>"
        f"<a href=\"/api/v1.0/place_id\">/api/v1.0/place_id</a><br/>"
        f"<a href=\"/api/v1.0/place_item\">/api/v1.0/place_item</a><br/>"
        f"<a href=\"/api/v1.0/pub_mapping\">/api/v1.0/pub_mapping</a><br/>"
        f"<a href=\"/api/v1.0/subject_id\">/api/v1.0/subject_id</a><br/>"
        f"<a href=\"/api/v1.0/subject_item\">/api/v1.0/subject_item</a><br/>"
    )


@app.route("/api/v1.0/col_mapping")
def col_mapp():
    
    # Return all collection values
    results = session.query(col_mapping.col, col_mapping.collection).all()

    # Create a dictionary from the row data and append to a list 
    all_col = []
    for c, coll in results:
        col_dict = {}
        col_dict["col"] = c
        col_dict["collection"] = coll
        all_col.append(col_dict)

    return jsonify(all_col)

@app.route("/api/v1.0/creator_id")
def creator():
    
    # Return all collection values
    results = session.query(creator_id.creator, creator_id.creator_id).all()

    # Create a dictionary from the row data and append to a list 
    all_creator = []
    for c, c_id in results:
        creator_dict = {}
        creator_dict["creator"] = c
        creator_dict["creator_id"] = c_id
        all_creator.append(creator_dict)

    return jsonify(all_creator)

@app.route("/api/v1.0/creator_type_id")
def creator_type():
    
    # Return all collection values
    results = session.query(creator_type_id.type,creator_type_id.creator_type_id).all()

    # Create a dictionary from the row data and append to a list 
    all_type = []
    for t, type_id in results:
        creator_dict = {}
        creator_dict["type"] = t
        creator_dict["creator_type_id"] = type_id
        all_type.append(creator_dict)

    return jsonify(all_type)

@app.route("/api/v1.0/creator_type_item")
def type_item():
    
    # Return all collection values
    results = session.query(creator_type_item.item_id, creator_type_item.creator_type_id, creator_type_item.creator_id).all()

    # Create a dictionary from the row data and append to a list 
    all = []
    for i_id, creator_type, creator in results:
        item_dict = {}
        item_dict["item_id"] = i_id
        item_dict["creator_type_id"] = creator_type
        item_dict["creator_id"] = creator

    return jsonify(all)

@app.route("/api/v1.0/dewey")
def dew():
    
    # Return all collection values
    results = session.query(dewey.dewey_dec_code, dewey.genre).all()

    # Create a dictionary from the row data and append to a list 
    for d, g in results:
        dewey_dict = {}
        dewey_dict["Dewey Decimal Code"] = d
        dewey_dict["genre"] = g
        all_dewey.append(dewey_dict)

    return jsonify(all_dewey)
@app.route("/api/v1.0/ins_mapping")
def ins():
    
    # Return all collection values
    results = session.query(ins_mapping.ins_key, ins_mapping.institution).all()

    # Create a dictionary from the row data and append to a list 
    all_ins = []
    for ins_k, ins in results:
        ins_dict = {}
        ins_dict["ins_key"] = ins_k
        ins_dict["institution"] = ins
        all_ins.append(ins_dict)

    return jsonify(all_ins)

@app.route("/api/v1.0/item_codes")
def codes():
    
    # Return all collection values
    results = session.query(item_codes.item_code, item_codes.item).all()

    # Create a dictionary from the row data and append to a list 
    all_item = []
    for code, i in results:
        item_dict = {}
        item_dict["item code"] = code
        item_dict["item"] = i
        all_item.append(item_dict)

    return jsonify(all_item)

@app.route("/api/v1.0/items")
def get_item():
    
    # Return all collection values
    results = session.query(items.title, items.col, items.wdl_url, items.ins_key, items.pub_key, items.dewey_dec_code, items.type_id,items.date,items.item_id).all()

    # Create a dictionary from the row data and append to a list 
    all_item = []
    for t, c, wdl, ins, pub, dewey_dec, type, d, i in results:
        item_dict = {}
        item_dict["title"] = t
        item_dict["col"] = c
        item_dict["wdl_url"] = wdl
        item_dict["ins_key"] = ins
        item_dict["pub_key"] = pub
        item_dict["dewey_dec_code"] = dewey_dec
        item_dict["type_id"] = type
        item_dict["date"] = d
        item_dict["item_id"] = i

        all_item.append(item_dict)

    return jsonify(all_item)

@app.route("/api/v1.0/lang_item")
def lang_it():
    
    # Return all collection values
    results = session.query(lang_item.item_id, lang_item.lang_id).all()

    # Create a dictionary from the row data and append to a list 
    all_lang = []
    for i_id, l_id in results:
        col_dict = {}
        col_dict["item_id"] = i_id
        col_dict["lang_id"] = l_id
        all_lang.append(col_dict)

    return jsonify(all_lang)

@app.route("/api/v1.0/languages_id")
def langs_id():
    
    # Return all collection values
    results = session.query(languages_id.lang, languages_id.lang_id).all()

    # Create a dictionary from the row data and append to a list 
    all_lang = []
    for l, l_id in results:
        lang_dict = {}
        lang_dict["lang"] = l
        lang_dict["lang_id"] = l_id
        all_lang.append(lang_dict)

    return jsonify(all_lang)

@app.route("/api/v1.0/place_id")
def get_place_id():
    
    # Return all collection values
    results = session.query(place_id.place, place_id.place_id).all()

    # Create a dictionary from the row data and append to a list
    all_place = []
    for p, p_id in results:
        place_dict = {}
        place_dict["place"] = p
        place_dict["place_id"] = p_id
        all_place.append(place_dict)

    return jsonify(all_place)

@app.route("/api/v1.0/place_item")
def get_place_item():
    
    # Return all collection values
    results = session.query(place_item.item_id, place_item.place_id).all()

    # Create a dictionary from the row data and append to a list 
    all = []
    for item, place in results:
        dict = {}
        dict["item_id"] = item
        dict["place_id"] = place
        all.append(dict)

    return jsonify(all)

@app.route("/api/v1.0/pub_mapping")
def pub():
    
    # Return all collection values
    results = session.query(pub_mapping.pub_key, pub_mapping.publisher).all()

    # Create a dictionary from the row data and append to a list 
    all = []
    for pub_key, pub in results:
        dict = {}
        dict["pub_key"] = pub_key
        dict["publisher"] = pub
        all.append(dict)

    return jsonify(all)

@app.route("/api/v1.0/subject_id")
def sub_id():
    
    # Return all collection values
    results = session.query(subject_id.subject, subject_id.subject_id).all()

    # Create a dictionary from the row data and append to a list  
    all = []
    for sub, subj_id in results:
        dict = {}
        dict["subject"] = sub
        dict["collection"] = subj_id
        all.append(dict)

    return jsonify(all)

@app.route("/api/v1.0/subject_item")
def sb_item():
    
    # Return all collection values
    results = session.query(subject_item.item_id, subject_item.subject_id).all()

    # Create a dictionary from the row data and append to a list 
    all = []
    for item, subject in results:
        dict = {}
        dict["item_id"] = item
        dict["subject_id"] = subject
        all.append(dict)

    return jsonify(all)



# close the session
session.close()  


if __name__ == '__main__':
    app.run(debug=True)
