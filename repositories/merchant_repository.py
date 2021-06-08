from models.category import Category
from pdb import run
from models.transactions import Transaction
from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants( name ) VALUES ( %s ) RETURNING id"
    values = [merchant.name]
    results = run_sql( sql, values)
    merchant.id = results[0]['id']
    return merchant

def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for result in results:
        merchant = Merchant(result['name'], result['id'])
        merchants.append(merchant)
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['id'])
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def categories(merchant):
    categories = []

    sql = "SELECT categories.* FROM categories INNER JOIN transactions ON transactions.category_id = categories.id WHERE transactions.merchant_id = %s"
    values = [merchant.id]
    results = run_sql(sql, values)

    for result in results:
        category = Category(result['name'], result['id'])
        categories.append(category)
    
    return categories