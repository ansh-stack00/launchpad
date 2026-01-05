import sqlite3

def load_schema(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    schema = {}

    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name NOT LIKE 'sqlite_%';
    """)

    tables = cursor.fetchall()

    for (table,) in tables:
        cursor.execute(f"PRAGMA table_info({table});")
        columns = cursor.fetchall()
        schema[table] = [
            {
                "column": col[1],
                "type": col[2],
                "nullable": not col[3]
            }
            for col in columns
        ]

    conn.close()
    print("schema loaded succesfully..")
    return schema

load_schema("lms.db")