#! /usr/bin/env python3

import argparse
import glob
import json
from xml.etree.ElementTree import fromstring

from xmljson import parker

from utils.common import JsonEncoder


def convert_file_xml_to_json(file_path: str):
    with open(file_path) as xml_file:
        xml_data = fromstring(xml_file.read())
        return json.dumps(parker.data(xml_data), cls=JsonEncoder, indent=4)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--file-path")
    parser.add_argument("--folder-path")

    args = parser.parse_args()
    if args.file_path:
        with open(args.file_path.replace("xml", "json"), "w") as json_file:
            json_file.write(convert_file_xml_to_json(args.file_path))
    elif args.folder_path:
        for file_path in glob.glob(f"{args.folder_path}/*.xml"):
            print(file_path)
            with open(file_path.replace("xml", "json"), "w") as json_file:
                json_file.write(convert_file_xml_to_json(file_path))


if __name__ == "__main__":
    main()
