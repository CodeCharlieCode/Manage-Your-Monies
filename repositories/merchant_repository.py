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

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)