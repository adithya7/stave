# from forte.data.multi_pack import MultiPack
import sqlite3
import json
from nlpviewer_backend.utils import gen_hash
import uuid


def add_pack(name, textPack, ontology, packID, rewrite=False):
    """
	textPack must be a string of json
	ontology must be a string of json
	"""
    con = sqlite3.connect("db.sqlite3")
    sqlite3.register_adapter(uuid.UUID, lambda u: u.hex)
    cursor = con.cursor()
    textPack = json.dumps(textPack)
    ontology = json.dumps(ontology)

    # check if the document is already in the db
    result = cursor.execute(
        "SELECT * FROM nlpviewer_backend_document WHERE packID=:id",
        {"id": uuid.UUID(int=packID)},
    )
    if result.fetchone() is not None:
        if rewrite:
            print("warning! rewriting pack %s in the db" % name)
        else:
            print("pack %s already present in db, skipping" % name)
            con.close()
            return

    cursor.execute(
        "INSERT OR REPLACE INTO nlpviewer_backend_document(textPack, ontology, packID, name) \
	            VALUES(?,?,?,?)",
        (textPack, ontology, uuid.UUID(int=packID), name),
    )
    con.commit()
    con.close()


def add_multipack(name, textPack, ontology, packID, rewrite=False):
    """
	textPack must be a string of json
	ontology must be a string of json
	"""
    con = sqlite3.connect("db.sqlite3")
    sqlite3.register_adapter(uuid.UUID, lambda u: u.hex)
    cursor = con.cursor()
    textPack = json.dumps(textPack)
    ontology = json.dumps(ontology)
    idHash = gen_hash(name)

    result = cursor.execute(
        "SELECT * FROM nlpviewer_backend_crossdoc WHERE packID=:id",
        {"id": uuid.UUID(int=packID)},
    )
    if result.fetchone() is not None:
        if rewrite:
            print("warning! rewriting multipack %s in the db" % name)
        else:
            print("multipack %s already present in db, skipping" % name)
            con.close()
            return

    cursor.execute(
        "INSERT OR REPLACE INTO nlpviewer_backend_crossdoc(textPack, ontology, packID, name, idHash) \
            VALUES(?,?,?,?,?)",
        (textPack, ontology, uuid.UUID(int=packID), name, idHash),
    )
    con.commit()
    con.close()
    return idHash
