import mysql.connector

# run using (python unit_test.py)

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='password1',
        database='my_guitar_shop'
    )

def get_products_sorted_by_price():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_code, product_name, list_price, discount_percent
        FROM products
        ORDER BY list_price DESC;
    """)
    result = cursor.fetchall()
    conn.close()
    return result

def get_customers_m_to_z():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT first_name, last_name, CONCAT(last_name, ', ', first_name) AS full_name
        FROM customers
        WHERE last_name >= 'M'
        ORDER BY last_name ASC;
    """)
    result = cursor.fetchall()
    conn.close()
    return result

def get_products_price_range():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_name, list_price, date_added
        FROM products
        WHERE list_price > 500 AND list_price < 2000
        ORDER BY date_added DESC;
    """)
    result = cursor.fetchall()
    conn.close()
    return result

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
    result = cursor.fetchall()
    conn.close()
    return result

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
    # Convert list_price from Decimal to float
    return [(category, product, float(price)) for category, product, price in results]

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
    result = cursor.fetchall()
    conn.close()
    return result

def get_shipping_addresses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.first_name, c.last_name, a.line1, a.city, a.state, a.zip_code
        FROM customers c
        JOIN addresses a ON c.shipping_address_id = a.address_id
        ORDER BY a.zip_code ASC;
    """)
    result = cursor.fetchall()
    conn.close()
    return result
