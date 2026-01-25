import sqlite3
import traceback
from autogen_core.tools import FunctionTool

def load_schema(db_path: str) -> dict:
    
    try:
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
            columns = cursor.fetchall()

            schema[table] = [
                {
                    "column": col[1],          
                    "type": col[2],             
                    "nullable": not bool(col[3])  
                }
                for col in columns
            ]

        conn.close()
        return schema

    except Exception:
        return {"error": traceback.format_exc()}


def _is_safe_sql(sql: str) -> bool:
    s = sql.strip().lower()
    return s.startswith("select") or s.startswith("with")

def list_tables(db_path: str) -> str:
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name NOT LIKE 'sqlite_%'
            ORDER BY name;
        """)
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()

        if not tables:
            return "No tables found."
        return "Tables:\n" + "\n".join(tables)

    except Exception:
        return f"Error:\n{traceback.format_exc()}"


def describe_table(db_path: str, table_name: str) -> str:
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(f"PRAGMA table_info({table_name});")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return f"No schema found (table may not exist): {table_name}"

        headers = ["cid", "name", "type", "notnull", "default", "pk"]
        lines = []
        lines.append(" | ".join(headers))
        lines.append("-" * 70)

        for r in rows:
            lines.append(" | ".join(str(x) for x in r))

        return "\n".join(lines)

    except Exception:
        return f"Error:\n{traceback.format_exc()}"


def query_sqlite(db_path: str, sql: str, max_rows: int = 50) -> str:
   
    try:
        if not _is_safe_sql(sql):
            return "Error: Only read-only SELECT/WITH queries are allowed in this DB Agent."

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(sql)
        rows = cursor.fetchmany(max_rows)
        col_names = [d[0] for d in cursor.description] if cursor.description else []
        conn.close()

        if not rows:
            return "Query executed successfully. No rows returned."

        lines = []
        if col_names:
            lines.append(" | ".join(col_names))
            lines.append("-" * 70)

        for row in rows:
            lines.append(" | ".join(str(x) for x in row))

        if len(rows) == max_rows:
            lines.append(f"\n(Note: showing only first {max_rows} rows.)")

        return "\n".join(lines)

    except Exception:
        return f"Error:\n{traceback.format_exc()}"
    
    

schema_tool = FunctionTool(
    load_schema,
    "Load full DB schema (tables + columns) from a SQLite database."
)

list_tables_tool = FunctionTool(
    list_tables,
    "List all tables inside a SQLite database."
)

describe_table_tool = FunctionTool(
    describe_table,
    "Describe a table schema (columns, types, nullability, defaults, primary key) from SQLite."
)

db_query_tool = FunctionTool(
    query_sqlite,
    "Run a read-only SQL query (SELECT/WITH) on a SQLite database and return results."
)
