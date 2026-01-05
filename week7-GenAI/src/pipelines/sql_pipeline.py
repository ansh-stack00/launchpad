from src.generator.llm_client import get_llm
from src.utils.schema_loader import load_schema
from src.generator.sql_generator import generate_sql,judge_sql
import sqlite3

client = get_llm()
schema = load_schema("lms.db")

user_question=input("Ask: ")
client = get_llm()


# execute sql 

def execute_sql(sql: str, db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    return columns, rows


# result summarizer llm

def summarize_results(columns, rows) -> str:
    prompt = f"""
Summarize the SQL result.

Columns:
{columns}

Rows:
{rows}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        
    )
    return response.choices[0].message.content

MAX_RETRIES=2

sql = generate_sql(client, schema , user_question)

for attempt in range(MAX_RETRIES + 1):
    judge_result = judge_sql(client, schema, user_question, sql)
    if judge_result["verdict"] == "PASS":
        print("SQL is correct:\n", sql)
        break

    if attempt == MAX_RETRIES:
        raise RuntimeError(f"SQL invalid after {MAX_RETRIES} retries:\n" + "\n".join(judge_result["issues"]))
    
    print(f"Fixing SQL (attempt {attempt+1})...")
    sql = generate_sql(
        client,
        schema,
        user_question,
        previous_sql=sql,
        issues=judge_result["issues"]
    )

columns, rows = execute_sql(sql,"lms.db")

print(rows)

summary = summarize_results(columns , rows)
print(summary)



       