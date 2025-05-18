import sqlite3

conn = sqlite3.connect("data/ultrasound_db.sqlite")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("[INFO] Tables in DB:")
for table in tables:
    print("-", table[0])
    
for table in tables:
    table_name = table[0]
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    print(f"[INFO] Columns in table {table_name}:")
    for column in columns:
        print("  -", column)
