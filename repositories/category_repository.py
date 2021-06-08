from repositories.merchant_repository import categories
from db.run_sql import run_sql
from models.category import Category
from models.merchant import Merchant

def save(category):
    sql = "INSERT INTO categories( name ) VALUES( %s ) RETURNING id"
    values = [category.name]
    results = run_sql(sql, values)
    category.id = results[0]['id']
    return category

def select_all():
    categories = []

    sql = "SELECT * FROM categories"
    results = run_sql(sql)

    for result in results:
        category = Category(result['name'], result['id'])
        categories.append(category)
    return categories

def select(id):
    category = None
    sql ="SELECT * FROM categories WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        category = Category(result['name'], result['id'])
    return category

def delete_all():
    sql = "DELETE FROM categories"
    run_sql(sql)