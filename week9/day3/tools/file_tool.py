from autogen_core.tools import FunctionTool
import csv
import os
import sqlite3
import pandas as pd
from typing import List, Dict, Any
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent

def inspect_csv(file_path: str) -> dict:

    full_path = BASE_DIR / file_path

    if not full_path.exists():
        return {"error": f"File not found: {full_path}"}

    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
        reader = csv.reader(f)
        headers = next(reader, [])
        row_count = sum(1 for _ in reader)

    return {
        "file": str(full_path),
        "rows": row_count,
        "columns": headers,
    }


inspect_csv_tool = FunctionTool(
    inspect_csv,
    name="inspect_csv",
    description="Inspect CSV structure"
)


def read_csv(file_path: str) -> dict:

    full_path = BASE_DIR / file_path

    if not full_path.exists():
        return {"error": f"File not found: {full_path}"}

    df = pd.read_csv(full_path)

    return {
        "headers": list(df.columns),
        "rows": df.head(10).to_dict(orient="records"),
    }


read_csv_tool = FunctionTool(
    read_csv,
    name="read_csv",
    description="Read CSV"
)


def write_csv(file_path: str, rows: List[Dict[str, Any]]) -> str:

    full_path = BASE_DIR / file_path

    df = pd.DataFrame(rows)
    df.to_csv(full_path, index=False)

    return f"Wrote CSV to {full_path}"


write_csv_tool = FunctionTool(
    write_csv,
    name="write_csv",
    description="Write CSV"
)


def load_csv_to_sqlite(csv_path: str, db_path: str, table_name: str) -> str:

    csv_full = BASE_DIR / csv_path
    db_full = BASE_DIR / db_path

    if not csv_full.exists():
        return f"Error: File not found: {csv_full}"

    conn = sqlite3.connect(db_full)

    df = pd.read_csv(csv_full)
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.close()

    return f"Loaded {csv_full} into {db_full} as table '{table_name}'"


load_csv_tool = FunctionTool(
    load_csv_to_sqlite,
    name="load_csv_to_sqlite",
    description="Load CSV into SQLite"
)


def read_txt(file_path: str) -> str:

    full_path = BASE_DIR / file_path

    if not full_path.exists():
        return f"File not found: {full_path}"

    return full_path.read_text()


read_txt_tool = FunctionTool(
    read_txt,
    name="read_txt",
    description="Read .txt file" 
)


def write_txt(file_path: str, content: str) -> str:

    full_path = BASE_DIR / file_path
    full_path.write_text(content)

    return f"Wrote file {full_path}"


write_txt_tool = FunctionTool(
    write_txt,
    name="write_txt",
    description="Write .txt file"
)


def append_txt(file_path: str, content: str) -> str:

    full_path = BASE_DIR / file_path

    with open(full_path, "a") as f:
        f.write(content)

    return f"Appended to {full_path}"


append_txt_tool = FunctionTool(
    append_txt,
    name="append_txt",
    description="Append to .txt file"
)

FILE_TOOLS = [
    inspect_csv_tool,
    read_csv_tool,
    write_csv_tool,
    load_csv_tool,
    read_txt_tool,
    write_txt_tool,
    append_txt_tool,
]
