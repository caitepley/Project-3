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
