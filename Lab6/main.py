from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from typing import List

app = FastAPI(title="Guitar Shop API")

# Use (uvicorn main:app --reload) to run
# Link (http://127.0.0.1:8000/docs)

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='password1',
        database='my_guitar_shop'
    )

# Models
class CustomerName(BaseModel):
    first_name: str
    last_name: str

class Product(BaseModel):
    product_name: str
    list_price: float
    date_added: str  # or use datetime if preferred

# GET routes
@app.get("/products/sorted")
def get_products_sorted_by_price():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_code, product_name, list_price, discount_percent
        FROM products
        ORDER BY list_price DESC;
    """)
    results = cursor.fetchall()
    conn.close()
    return results

@app.get("/customers/m_to_z")
def get_customers_m_to_z():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT first_name, last_name, CONCAT(last_name, ', ', first_name) AS full_name
        FROM customers
        WHERE last_name >= 'M'
        ORDER BY last_name ASC;
    """)
    results = cursor.fetchall()
    conn.close()
    return results

@app.get("/products/range")
def get_products_price_range():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_name, list_price, date_added
        FROM products
        WHERE list_price > 500 AND list_price < 2000
        ORDER BY date_added DESC;
    """)
    results = cursor.fetchall()
    conn.close()
    return results

@app.get("/order-items/totals")
def get_order_item_totals():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT item_id, item_price, discount_amount, quantity,
               item_price * quantity AS price_total,
               discount_amount * quantity AS discount_total,
               (item_price - discount_amount) * quantity AS item_total
        FROM order_items
        HAVING item_total > 500
        ORDER BY item_total DESC;
    """)
    results = cursor.fetchall()
    conn.close()
    return results

@app.get("/products/with-category")
def get_products_with_category():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.category_name, p.product_name, p.list_price
        FROM categories c
        JOIN products p ON c.category_id = p.category_id
        ORDER BY c.category_name, p.product_name ASC;
    """)
    results = cursor.fetchall()
    conn.close()
    return [(category, product, float(price)) for category, product, price in results]

@app.get("/addresses/allan")
def get_addresses_for_allan():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.first_name, c.last_name, a.line1, a.city, a.state, a.zip_code
        FROM customers c
        JOIN addresses a ON c.customer_id = a.customer_id
        WHERE c.email_address = 'allan.sherwood@yahoo.com'
        ORDER BY a.zip_code ASC;
    """)
    results = cursor.fetchall()
    conn.close()
    return results

@app.get("/addresses/shipping")
def get_shipping_addresses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.first_name, c.last_name, a.line1, a.city, a.state, a.zip_code
        FROM customers c
        JOIN addresses a ON c.shipping_address_id = a.address_id
        ORDER BY a.zip_code ASC;
    """)
    results = cursor.fetchall()
    conn.close()
    return results

# PUT routes — Simulated (for demo purposes)
@app.put("/customers/update-name")
def update_customer_name(email: str, name: CustomerName):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE customers
        SET first_name = %s, last_name = %s
        WHERE email_address = %s;
    """, (name.first_name, name.last_name, email))
    conn.commit()
    conn.close()
    return {"message": "Customer name updated."}

@app.put("/products/update-price")
def update_product_price(product_code: str, new_price: float):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE products
        SET list_price = %s
        WHERE product_code = %s;
    """, (new_price, product_code))
    conn.commit()
    conn.close()
    return {"message": "Product price updated."}

@app.put("/products/add")
def add_product(product: Product):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO products (product_name, list_price, date_added)
        VALUES (%s, %s, %s);
    """, (product.product_name, product.list_price, product.date_added))
    conn.commit()
    conn.close()
    return {"message": "Product added."}
