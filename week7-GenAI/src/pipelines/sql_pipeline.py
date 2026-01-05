from src.generator.llm_client import get_llm
from src.utils.schema_loader import load_schema
from src.generator.sql_generator import generate_sql,judge_sql
client = get_llm()
schema = load_schema("lms.db")

user_question=input("Ask: ")
client = get_llm()
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

    print(sql)
