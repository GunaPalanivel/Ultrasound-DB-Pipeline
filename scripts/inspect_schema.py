# scripts/inspect_schema.py

import sqlite3
import os

DB_PATH = "data/ultrasound_db.sqlite"
OUTPUT_PATH = "output/schema_relationships.txt"

def inspect_schema(db_path):
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"[ERROR] SQLite DB not found: {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall() if not row[0].startswith('sqlite_')]

    schema_info = {}

    for table in tables:
        print(f"[INFO] Inspecting table: {table}")
        cursor.execute(f"PRAGMA table_info({table});")
        columns = cursor.fetchall()

        cursor.execute(f"PRAGMA foreign_key_list({table});")
        foreign_keys = cursor.fetchall()

        schema_info[table] = {
            "columns": columns,
            "foreign_keys": foreign_keys
        }

    conn.close()
    return schema_info

def write_relationships(schema_info, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for table, info in schema_info.items():
            f.write(f"Table: {table}\n")
            f.write("  Columns:\n")
            for col in info["columns"]:
                col_id, name, dtype, notnull, default, pk = col
                f.write(f"    - {name} ({dtype}) {'[PK]' if pk else ''}\n")

            if info["foreign_keys"]:
                f.write("  Foreign Keys:\n")
                for fk in info["foreign_keys"]:
                    _, _, ref_table, from_col, to_col, *_ = fk
                    f.write(f"    - {from_col} → {ref_table}.{to_col}\n")
            else:
                f.write("  Foreign Keys: None\n")

            f.write("\n")

    print(f"[SUCCESS] Relationships written to: {output_path}")

if __name__ == "__main__":
    schema = inspect_schema(DB_PATH)
    write_relationships(schema, OUTPUT_PATH)
