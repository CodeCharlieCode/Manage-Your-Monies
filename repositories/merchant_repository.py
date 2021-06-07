from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    sql = 'INSERT INTO merchants( name ) VALUES ( %s ) RETURNING id'
    values = [merchant.name]
    results = run_sql( sql, values)
    merchant.id = results[0]['id']
    return merchant

    