#CRUD

CREATE_MARKET = """
      CREATE TABLE IF NOT EXISTS market (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      product TEXT NOT NULL,
      buyed INTEGER DEFAULT 0
      )"""
    

INSERT_PRODUCTS = "INSERT INTO market (product) VALUES (?)"

SELECT_PRODUCTS = "SELECT id, product, buyed FROM  market"

SELECT_PRODUCTS_BUYED = "SELECT id, product, buyed FROM market WHERE buyed = 1"

SELECT_PRODUCTS_NOT_BUYED = "SELECT id, product, buyed FROM market WHERE buyed = 0"

UPDATE_PRODUCTS = "UPDATE market SET product = ? WHERE id = ? "

DELETE_PRODUCTS = "DELETE FROM market WHERE id = ?"