from llm_sql import generate_sql, generate_answer
from db import run_query
import re


def clean_sql(sql):
    sql = re.sub(r"```sql|```", "", sql, flags=re.IGNORECASE)

    match = re.search(r"(SELECT .*?;)", sql, re.IGNORECASE | re.DOTALL)

    if match:
        return match.group(1).strip()

    return sql.strip()


def agent(question):
    raw_sql = generate_sql(question)
    sql = clean_sql(raw_sql)

    result = run_query(sql)
    answer = generate_answer(question, result)

    return answer, sql