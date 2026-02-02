import sqlite3
import traceback
from autogen_core.tools import FunctionTool

db_path = "sales.db"


def extract_schema(db_path):

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


schema_cache = extract_schema(db_path)

valid_columns = {
    table: {col["column"].lower() for col in cols}
    for table, cols in schema_cache.items()
}


def _is_read_only_sql(sql):
    sql = sql.strip().lower()
    return sql.startswith("select") or sql.startswith("with")


def validate_sql(sql):

    tokens = sql.lower().replace(",", " ").split()

    for token in tokens:
        for table_cols in valid_columns.values():
            if token in table_cols:
                break
        else:
            if token.isidentifier():
                return False, f"Unknown column: {token}"

    return True, None


def schema_aware_query(db_path, sql, max_rows):

    try:

        if not _is_read_only_sql(sql):
            return {"error": "Only SELECT/WITH queries allowed."}

        ok, err = validate_sql(sql)
        if not ok:
            return {"error": err}

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
    strict=True
)

extract_schema_tool = FunctionTool(
    extract_schema,
    name="extract_schema_tool",
    strict=True
)
