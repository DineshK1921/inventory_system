from db import get_connection


def get_all_products():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, name, category, price, quantity, supplier, created_at
                FROM products
                ORDER BY id
            """)
            rows = cur.fetchall()

    return [
        {
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3],
            "quantity": row[4],
            "supplier": row[5],
            "created_at": row[6],
        }
        for row in rows
    ]


def add_product(name, category, price, quantity, supplier):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO products (name, category, price, quantity, supplier)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, category, price, quantity, supplier))
        conn.commit()


def get_product_by_id(product_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, name, category, price, quantity, supplier, created_at
                FROM products
                WHERE id = %s
            """, (product_id,))
            row = cur.fetchone()

    if not row:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "category": row[2],
        "price": row[3],
        "quantity": row[4],
        "supplier": row[5],
        "created_at": row[6],
    }


def update_product(product_id, name, category, price, quantity, supplier):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE products
                SET name = %s,
                    category = %s,
                    price = %s,
                    quantity = %s,
                    supplier = %s
                WHERE id = %s
            """, (name, category, price, quantity, supplier, product_id))
        conn.commit()


def delete_product(product_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
        conn.commit()