import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"


def generate_sql(question):
    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "messages": [
                {
                    "role": "user",
                    "content": f"""
You are an SQL generator.

STRICT RULES:
- Output ONLY SQL
- Start with SELECT
- No explanation
- No markdown
- Use LIKE instead of =
- Use LOWER() for case-insensitive matching

Tables:
products(id, name, category, price)
customers(id, name, city)
orders(id, customer_id, product_id, quantity, order_date)

Relationships:
- orders.customer_id = customers.id
- orders.product_id = products.id

IMPORTANT:
- Product names may vary (singular/plural)
- Always use LIKE '%keyword%'
- Always use LOWER()

Example:
SELECT price FROM products WHERE LOWER(name) LIKE '%headphone%';

Question:
{question}
"""
                }
            ],
            "max_tokens": 200
        })
    )

    result = json.loads(response["body"].read())
    return result["content"][0]["text"]


def generate_answer(question, result):
    if result == []:
        return "No matching data found."

    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "messages": [
                {
                    "role": "user",
                    "content": f"""
User question: {question}
SQL result: {result}

Give ONLY a short, direct answer.
- Max 1–2 lines
- No explanation
- No technical details

Example:
Headphones cost 2000.

Answer:
"""
                }
            ],
            "max_tokens": 100
        })
    )

    result = json.loads(response["body"].read())
    return result["content"][0]["text"]