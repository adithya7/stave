"""
Update database with new packs and multi packs
"""

from argparse import ArgumentParser
from pathlib import Path
import json

from database_update import add_pack, add_multipack

if __name__ == "__main__":
    parser = ArgumentParser(description="add new packs/multipacks")
    parser.add_argument("--pack-json", type=Path, help="directory with packs")
    parser.add_argument("--multi-json", type=Path, help="directory with multipacks")
    parser.add_argument("--pack-onto", default="initial_data/pack_ontology.json")
    parser.add_argument("--multi-onto", default="initial_data/multi_ontology.json")

    args = parser.parse_args()

    with open(args.pack_onto, "r") as rf:
        pack_onto = json.load(rf)

    for pack in args.pack_json.iterdir():
        with open(pack, "r") as rf:
            textPack = json.load(rf)
        packID = textPack["py/state"]["_meta"]["py/state"]["_pack_id"]
        packName = textPack["py/state"]["_meta"]["py/state"]["pack_name"]
        print(packID)
        add_pack(packName, textPack, pack_onto, packID)

    with open(args.multi_onto, "r") as rf:
        multi_onto = json.load(rf)

    for multi in args.multi_json.iterdir():
        with open(multi, "r") as rf:
            textPack = json.load(rf)
        packID = textPack["py/state"]["_meta"]["py/state"]["_pack_id"]
        packName = textPack["py/state"]["_meta"]["py/state"]["pack_name"]
        add_multipack(packName, textPack, multi_onto, packID)
