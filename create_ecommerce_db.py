import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
""")

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL
)
""")

cursor.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date TEXT
)
""")

products = [
    (1, "iPhone 14", "Electronics", 80000),
    (2, "Samsung Galaxy S23", "Electronics", 75000),
    (3, "MacBook Air", "Electronics", 120000),
    (4, "Nike Shoes", "Fashion", 5000),
    (5, "T-Shirt", "Fashion", 800),
    (6, "Washing Machine", "Home Appliance", 25000),
    (7, "Refrigerator", "Home Appliance", 30000),
    (8, "Headphones", "Electronics", 2000)
]

customers = [
    (1, "Rishu", "Coimbatore"),
    (2, "Rahul", "Chennai"),
    (3, "Anjali", "Bangalore"),
    (4, "Kiran", "Hyderabad")
]

orders = [
    (1, 1, 1, 1, "2024-03-01"),
    (2, 1, 4, 2, "2024-03-02"),
    (3, 2, 2, 1, "2024-03-03"),
    (4, 3, 3, 1, "2024-03-04"),
    (5, 4, 5, 3, "2024-03-05"),
    (6, 2, 8, 2, "2024-03-06"),
    (7, 3, 6, 1, "2024-03-07"),
    (8, 1, 7, 1, "2024-03-08")
]

cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", products)
cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", customers)
cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", orders)

conn.commit()
conn.close()

print("✅ E-commerce DB ready!")