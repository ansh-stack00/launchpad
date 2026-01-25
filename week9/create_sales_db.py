import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT
);
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price REAL NOT NULL
);
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    sale_date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);
""")


cursor.executemany(
    "INSERT INTO customers (name, country) VALUES (?, ?);",
    [
        ("Ansh", "India"),
        ("Riya", "India"),
        ("John", "USA"),
        ("Maria", "Spain"),
    ]
)

cursor.executemany(
    "INSERT INTO products (product_name, price) VALUES (?, ?);",
    [
        ("Laptop", 80000),
        ("Phone", 40000),
        ("Tablet", 30000),
        ("Headphones", 5000),
    ]
)

cursor.executemany(
    "INSERT INTO sales (customer_id, product_id, quantity, sale_date) VALUES (?, ?, ?, ?);",
    [
        (1, 1, 1, "2024-01-10"),
        (1, 4, 2, "2024-01-11"),
        (2, 2, 1, "2024-01-12"),
        (3, 1, 1, "2024-01-13"),
        (4, 3, 3, "2024-01-14"),
        (2, 4, 1, "2024-01-15"),
    ]
)

conn.commit()
conn.close()

print("sales.db created successfully")
