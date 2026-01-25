from autogen_core.tools import FunctionTool
import csv
import os
import traceback
from typing import List, Dict, Any

def ensure_parent_dir(file_path: str) -> None:
    parent = os.path.dirname(file_path)
    if parent and not os.path.exists(parent):
        os.makedirs(parent, exist_ok=True)

def read_txt(file_path: str) -> str:
    try:
        if not os.path.exists(file_path):
            return f"Error: File not found: {file_path}"

        if not file_path.lower().endswith(".txt"):
            return "Error: Only .txt files are supported by read_txt."

        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    except Exception:
        return f"Error:\n{traceback.format_exc()}"


def write_txt(file_path: str, content: str) -> str:
    try:
        if not file_path.lower().endswith(".txt"):
            return "Error: Only .txt files are supported by write_txt."

        ensure_parent_dir(file_path)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"Wrote text file: {file_path}"

    except Exception:
        return f"Error:\n{traceback.format_exc()}"


def append_txt(file_path: str, content: str) -> str:
    try:
        if not file_path.lower().endswith(".txt"):
            return "Error: Only .txt files are supported by append_txt."

        ensure_parent_dir(file_path)

        with open(file_path, "a", encoding="utf-8") as f:
            f.write(content)

        return f"Appended to text file: {file_path}"

    except Exception:
        return f"Error:\n{traceback.format_exc()}"

# csv tools
def read_csv(file_path: str, max_rows: int = 50) -> dict:
    """
    Read a CSV file with encoding fallback.
    """
    try:
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}"}

        if not file_path.lower().endswith(".csv"):
            return {"error": "Only .csv files are supported by read_csv."}

        encodings_to_try = ["utf-8", "latin-1", "ISO-8859-1", "cp1252"]
        last_error = None

        for encoding in encodings_to_try:
            try:
                with open(file_path, "r", encoding=encoding, newline="") as f:
                    reader = csv.DictReader(f)
                    headers = reader.fieldnames or []
                    rows = []

                    for i, row in enumerate(reader):
                        if i >= max_rows:
                            break
                        rows.append(row)

                return {
                    "encoding_used": encoding,
                    "headers": headers,
                    "rows": rows,
                    "note": f"Showing first {len(rows)} rows"
                }

            except UnicodeDecodeError as e:
                last_error = e
                continue

        return {
            "error": "Failed to decode CSV with supported encodings",
            "details": str(last_error),
        }

    except Exception:
        return {"error": traceback.format_exc()}



def write_csv(file_path: str, rows: List[Dict[str, Any]]) -> str:
    
    try:
        if not file_path.lower().endswith(".csv"):
            return "Error: Only .csv files are supported by write_csv."

        if not rows:
            return "Error: rows is empty. Provide at least one row."

        ensure_parent_dir(file_path)

        headers = list(rows[0].keys())
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)

        return f"Wrote CSV file: {file_path}"

    except Exception:
        return f"Error:\n{traceback.format_exc()}"



read_txt_tool = FunctionTool(read_txt, "Read a .txt file and return its contents.")
write_txt_tool = FunctionTool(write_txt, "Write content to a .txt file (overwrite).")
append_txt_tool = FunctionTool(append_txt, "Append content to a .txt file.")

read_csv_tool = FunctionTool(read_csv, "Read a .csv file and return headers + rows.")
write_csv_tool = FunctionTool(write_csv, "Write rows (list of dicts) to a .csv file.")
