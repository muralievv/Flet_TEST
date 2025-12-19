import sqlite3
from db import queries
from config import path_db

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_MARKET)
    print('База данных успешно создана')
    conn.commit()
    conn.close()

def add_product(product):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_PRODUCTS, (product,))
    conn.commit()
    product_id = cursor.lastrowid
    conn.close()
    return product_id

def get_product(filter_type):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if filter_type == 'buyed':
        cursor.execute(queries.SELECT_PRODUCTS_BUYED)
    elif filter_type == 'not_buyed':
        cursor.execute(queries.SELECT_PRODUCTS_NOT_BUYED)
    elif filter_type == 'all':
        cursor.execute(queries.SELECT_PRODUCTS)
    
    conn.commit()
    products = cursor.fetchall()
    conn.close()
    return products

def update_products(product_id, new_product = None, buyed = None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if new_product is not None:
        cursor.execute(queries.UPDATE_PRODUCTS, (new_product, product_id))
    elif buyed is not None:
        cursor.execute("UPDATE market SET buyed = ? WHERE id = ?", (buyed, product_id))
    conn.commit()
    conn.close()
    

def delete_product(product_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_PRODUCTS, (product_id, ))
    conn.commit()
    conn.close()

