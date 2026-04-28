import sqlite3

def run_query(sql):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    cursor.execute(sql)
    result = cursor.fetchall()

    conn.close()
    return result