ALTER TABLE items
ADD CONSTRAINT fk_pub_key_items
FOREIGN KEY (pub_key)
REFERENCES pub_mapping(pub_key);

ALTER TABLE items
ADD CONSTRAINT fk_ins_key_items
FOREIGN KEY (ins_key)
REFERENCES ins_mapping(ins_key);

ALTER TABLE items
ADD CONSTRAINT fk_dewey_dec_code_items
FOREIGN KEY (dewey_dec_code)
REFERENCES dewey(dewey_dec_code);

ALTER TABLE subject_item
ADD CONSTRAINT fk_item_id_subject_item
FOREIGN KEY (item_id)
REFERENCES items(item_id);

ALTER TABLE place_item
ADD CONSTRAINT fk_item_id_place_item
FOREIGN KEY (item_id)
REFERENCES items(item_id);

ALTER TABLE lang_item
ADD CONSTRAINT fk_item_id_lang_item
FOREIGN KEY (item_id)
REFERENCES items(item_id);

ALTER TABLE creator_type_item
ADD CONSTRAINT fk_item_id_creator_type_item
FOREIGN KEY (item_id)
REFERENCES items(item_id);

ALTER TABLE creator_type_item
ADD CONSTRAINT fk_creator_type_item_item_id
FOREIGN KEY (creator_type_id)
REFERENCES creator_type_id(creator_type_id);

ALTER TABLE creator_type_item
ADD CONSTRAINT fk_creator_type_item_item_id2
FOREIGN KEY (creator_id)
REFERENCES creator_id(creator_id);

ALTER TABLE items
ADD CONSTRAINT fk_col_id_items
FOREIGN KEY (col)
REFERENCES col_mapping(col_id);

ALTER TABLE items
ADD CONSTRAINT fk_type_items
FOREIGN KEY (type_id)
REFERENCES item_codes(item);

ALTER TABLE lang_item
ADD CONSTRAINT fk_lang_item_id
FOREIGN KEY (lang_id)
REFERENCES languages_id(lang_id);

ALTER TABLE place_item
ADD CONSTRAINT fk_place_id_item
FOREIGN KEY (place_id)
REFERENCES place_id(place_id);

ALTER TABLE subject_item
ADD CONSTRAINT fk_subject_id_item
FOREIGN KEY (subject_id)
REFERENCES subject_id(subject_id);