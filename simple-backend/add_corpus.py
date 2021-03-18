"""
Update database with new packs and multi packs
"""

from argparse import ArgumentParser
from pathlib import Path
import json

from database_update import add_pack, add_multipack

if __name__ == "__main__":
    parser = ArgumentParser(description="add new packs/multipacks")
    parser.add_argument("dir", type=Path, help="directory with /multi and /packs")
    parser.add_argument("--pack-onto", default="initial_data/pack_ontology.json")
    parser.add_argument("--multi-onto", default="initial_data/multi_ontology.json")
    parser.add_argument("--rewrite", action="store_true")

    args = parser.parse_args()

    with open(args.pack_onto, "r") as rf:
        pack_onto = json.load(rf)

    pack_dir = args.dir / "packs"
    for pack in pack_dir.iterdir():
        with open(pack, "r") as rf:
            textPack = json.load(rf)
        packID = textPack["py/state"]["_meta"]["py/state"]["_pack_id"]
        packName = textPack["py/state"]["_meta"]["py/state"]["pack_name"]
        print("adding datapack: %s" % packName)
        add_pack(packName, textPack, pack_onto, packID, rewrite=args.rewrite)

    with open(args.multi_onto, "r") as rf:
        multi_onto = json.load(rf)

    multipack_dir = args.dir / "multi"
    for multi in multipack_dir.iterdir():
        with open(multi, "r") as rf:
            textPack = json.load(rf)
        packID = textPack["py/state"]["_meta"]["py/state"]["_pack_id"]
        packName = textPack["py/state"]["_meta"]["py/state"]["pack_name"]
        print("adding multipack: %s" % packName)
        add_multipack(packName, textPack, multi_onto, packID, rewrite=args.rewrite)
