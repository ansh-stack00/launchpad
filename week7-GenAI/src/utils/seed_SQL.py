import sqlite3
from pathlib import Path
from pathlib import Path

PROJECT_ROOT = Path.cwd()
# print(PROJECT_ROOT)

def seed_lms(db_path="lms.db"):
    conn = sqlite3.connect(db_path)

    with open(PROJECT_ROOT/"seedDB.sql", "r") as f:
        conn.executescript(f.read())

    conn.close()
    print("LMS database seeded")

seed_lms()