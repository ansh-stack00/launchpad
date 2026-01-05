

from src.prompts.llm_as_judge import build_judge_prompt
from src.prompts.fix_prompt import build_fix_prompt
import json
import re





# cleaning llm result to get sql query from it 
def extract_sql(llm_response):
   
    sql_block = re.search(
        r"```sql\s*(.*?)\s*```",
        llm_response,
        re.DOTALL | re.IGNORECASE
    )

    if sql_block:
        return sql_block.group(1).strip()

    fallback = re.search(
        r"(WITH\s+.*|SELECT\s+.*)",
        llm_response,
        re.DOTALL | re.IGNORECASE
    )

    if fallback:
        return fallback.group(1).strip()
    raise ValueError("No SQL found in LLM response")




def generate_sql(client, schema, user_question, previous_sql='', issues=''):
    # system promp to generate sql 
    SYSTEM_PROMPT=f"""
    You are a senior SQL developer and data analyst. 
    Your goal is to translate natural language questions into accurate, executable SQL queries.

    ### Instructions
    1. **Analyze Schema**: Identify necessary tables, columns, and foreign key relationships.
    2. **Decompose Question**: Break complex questions into logical sub-tasks (e.g., filtering, joining, aggregating).
    3. **Draft Chain-of-Thought**: Explicitly state your reasoning steps before writing the final SQL.
    4. **Final SQL**: Output the SQL query within ```sql tags.

    Rules:
    - Use only provided tables and columns
    - No DELETE, UPDATE, INSERT
    - SQLite/Postgres compatible
    - Return ONLY SQL
    - sqllite is case sensetive so do not change case.
    - Disallow boolean arithmetic in aggregations
    - Require CASE WHEN inside SUM/COUNT
    - Validate portability if DB type ≠ known

    Database schema:
    {json.dumps(schema, indent=2)}

    Question:
    {user_question}

    examples :
    ques : give the details of all the student with prending payment 
    ans : SELECT DISTINCT s.*
    FROM students s
    JOIN payments p
    ON s.student_id = p.student_id
    WHERE p.status = 'Pending';

    QUES : Students Enrolled in Multiple Courses
    Ans:SELECT s.name, COUNT(e.course_id) AS courses
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    GROUP BY s.name
    HAVING courses > 1;

    ques : give the attendence analytics 
    Ans :SELECT s.name,
        SUM(a.status = 'Present') * 1.0 / COUNT(*) AS attendance_rate
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    JOIN attendance a ON e.enrollment_id = a.enrollment_id
    GROUP BY s.name;


    Ques : Find students whose GPA is higher than the overall average GPA
    Ans : WITH student_gpa AS (
    SELECT
        s.student_id,
        s.name,
        AVG(
            CASE e.grade
                WHEN 'A'  THEN 4.0
                WHEN 'A-' THEN 3.7
                WHEN 'B+' THEN 3.3
                WHEN 'B'  THEN 3.0
                ELSE 0
            END
        ) AS gpa
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    GROUP BY s.student_id, s.name
    )
    SELECT *
    FROM student_gpa
    WHERE gpa > (SELECT AVG(gpa) FROM student_gpa);


    """


    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_question}
    ]

    if previous_sql and issues:
        messages.append({"role": "assistant", "content": f"```sql\n{previous_sql}\n```"})
        messages.append({"role": "user", "content": build_fix_prompt(user_question, issues)})

    
    # llm for genearatin the sql query 
    resposes = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    print("sql generated: ", extract_sql(resposes.choices[0].message.content))
    return extract_sql(resposes.choices[0].message.content)


# sql = extract_sql()
# print(sql)


# llm for judging the sql query created by sql genearator 
def parse_json(llm_response):
    match = re.search(r'\{.*\}', llm_response, re.DOTALL)
    if match:
        return json.loads(match.group(0))
    raise ValueError("No valid JSON found in LLM response")


def judge_sql(client, schema, user_question, sql):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": build_judge_prompt(schema, user_question, sql)
            }
        ]
    )
    raw_output = response.choices[0].message.content
    print("Raw judge output:\n", raw_output)
    judge_result = parse_json(raw_output)
    print("Parsed evaluation result:", judge_result)
    return judge_result
