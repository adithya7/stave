import sqlite3
import json
from utils import gen_hash
def add_pack(name, textPack, ontology, packID):
	"""
	pack must be a string of json
	"""
	con = sqlite3.connect('simple-backend/db.sqlite3')
	cursor = con.cursor()
	textPack = json.dumps(textPack)
	ontology = json.dumps(ontology)

	
	cursor.execute("INSERT INTO nlpviewer_backend_document(textPack, ontology, packID, name) \
	            VALUES(?,?,?,?)",(textPack, ontology, packID, name))

def add_multipack(name, textPack, ontology, packID, idHash):
	con = sqlite3.connect('simple-backend/db.sqlite3')
	cursor = con.cursor()
	textPack = json.dumps(textPack)
	ontology = json.dumps(ontology)
	idHash = gen_hash(name)
	cursor.execute("INSERT INTO nlpviewer_backend_crossdoc(textPack, ontology, packID, name, idHash) \
            VALUES(?,?,?,?)",(textPack, ontology, packID, name, idHash))


