# from forte.data.multi_pack import MultiPack
import sqlite3
import json
from nlpviewer_backend.utils import gen_hash
import uuid

def add_pack(name, textPack, ontology, packID):
	"""
	textPack must be a string of json
	ontology must be a string of json
	"""
	con = sqlite3.connect('db.sqlite3')
	sqlite3.register_adapter(uuid.UUID, lambda u: u.hex)
	cursor = con.cursor()
	textPack = json.dumps(textPack)
	ontology = json.dumps(ontology)

	cursor.execute("INSERT INTO nlpviewer_backend_document(textPack, ontology, packID, name) \
	            VALUES(?,?,?,?)",(textPack, ontology, uuid.UUID(int=packID), name))
	con.commit()
	con.close()

def add_multipack(name, textPack, ontology, packID):
	"""
	textPack must be a string of json
	ontology must be a string of json
	"""
	con = sqlite3.connect('db.sqlite3')
	sqlite3.register_adapter(uuid.UUID, lambda u: u.hex)
	cursor = con.cursor()
	textPack = json.dumps(textPack)
	ontology = json.dumps(ontology)
	idHash = gen_hash(name)
	cursor.execute("INSERT INTO nlpviewer_backend_crossdoc(textPack, ontology, packID, name, idHash) \
            VALUES(?,?,?,?,?)",(textPack, ontology, uuid.UUID(int=packID), name, idHash))
	con.commit()
	con.close()
	return idHash


# def forte_add_multipack(input_pack: MultiPack):
# 	add_multipack(input_pack.pack_name, input_pack)
