import os
import sqlite3

def load_sql_to_sqlite(sql_file_path: str, sqlite_db_path: str):
    """
    Loads an SQL dump file and executes it to create a SQLite database.

    Args:
        sql_file_path (str): Path to the SQL dump file.
        sqlite_db_path (str): Desired output path for the SQLite DB file.
    """
    if not os.path.exists(sql_file_path):
        raise FileNotFoundError(f"SQL file not found: {sql_file_path}")

    print("[INFO] Reading SQL dump...")
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        sql_script = f.read()

    print("[INFO] Connecting to SQLite DB...")
    conn = sqlite3.connect(sqlite_db_path)
    cursor = conn.cursor()

    try:
        print("[INFO] Executing SQL script...")
        try:
            cursor.executescript(sql_script)
        except sqlite3.DatabaseError as e:
            print(f"[ERROR] Failed to execute SQL dump: {e}")
            return
        conn.commit()
        print(f"[SUCCESS] Database created at: {sqlite_db_path}")
    except sqlite3.Error as e:
        print(f"[ERROR] General SQLite error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    SQL_FILE = "data/ultrasound_db.sql"
    SQLITE_DB = "data/ultrasound_db.sqlite"
    load_sql_to_sqlite(SQL_FILE, SQLITE_DB)
