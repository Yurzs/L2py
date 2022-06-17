#! /usr/bin/env python3

import argparse
import glob
import json
import re

from mysql.connector import connect

from src.utils.common import JsonEncoder


def convert_sql_to_json(file_path: str):
    with connect(host="localhost", user="root", password="1234", database="L2py") as connection:
        with open(file_path) as sql_query_file:
            query = sql_query_file.read()
            table_search = re.findall(
                "CREATE TABLE (?:IF NOT EXISTS )?`?(?P<table_name>[\w]+)`?", query
            )
            table_name = table_search[0]
            with connection.cursor() as cursor:
                for statement in query.split(";"):
                    statement = statement.strip()
                    if len(statement) > 0:
                        cursor.execute(statement + ";")
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {table_name};")
                row_headers = [x[0] for x in cursor.description]
                rows = list(cursor.fetchall())
                data = []
                print(len(rows))
                for row in rows:
                    data.append(dict(zip(row_headers, row)))
                return json.dumps(data, cls=JsonEncoder, indent=4)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--file-path")
    parser.add_argument("--folder-path")

    args = parser.parse_args()
    if args.file_path:
        with open(args.file_path.replace(".sql", ".json"), "w") as json_file:
            json_file.write(convert_sql_to_json(args.file_path))
    elif args.folder_path:
        for file_path in glob.glob(f"{args.folder_path}/*.sql"):
            print(file_path)
            with open(file_path.replace(".sql", ".json"), "w") as json_file:
                json_file.write(convert_sql_to_json(file_path))
    else:
        print("No action specified")


if __name__ == "__main__":
    main()
