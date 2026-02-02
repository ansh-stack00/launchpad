import sqlite3
import traceback
from typing import Dict, Any
from autogen_core.tools import FunctionTool

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = str(BASE_DIR / "sales.db")


def extract_schema(db_path: str) -> Dict[str, Any]:

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    schema = {}

    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name;
    """)

    tables = cursor.fetchall()

    for (table,) in tables:
        cursor.execute(f"PRAGMA table_info({table});")
        cols = cursor.fetchall()

        schema[table] = [
            {
                "column": c[1],
                "type": c[2],
                "nullable": not bool(c[3]),
                "primary_key": bool(c[5])
            }
            for c in cols
        ]

    conn.close()
    return schema


def _is_read_only_sql(sql: str) -> bool:
    return sql.strip().lower().startswith(("select", "with"))

def schema_aware_query(
    db_path: str,
    sql: str,
    max_rows: int
) -> Dict[str, Any]:

    try:

        if not _is_read_only_sql(sql):
            return {"error": "Only SELECT/WITH queries allowed"}

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(sql)

        rows = cursor.fetchmany(min(max_rows, 10))
        columns = [d[0] for d in cursor.description]

        conn.close()

        return {
            "query": sql,
            "columns": columns,
            "rows": rows
        }

    except Exception:
        return {"error": traceback.format_exc()}

schema_query_tool = FunctionTool(
    schema_aware_query,
    name="schema_aware_query",
    description="Run read-only SQL on SQLite",
)

extract_schema_tool = FunctionTool(
    extract_schema,
    name="extract_schema",
    description="Extract DB schema",
)
