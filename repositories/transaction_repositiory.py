from db.run_sql import run_sql
from models.transactions import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository
import pdb

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, category_id, description, amount, date) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [transaction.merchant.id, transaction.category.id, transaction.description, transaction.amount, transaction.date]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all(month=None):
    transactions = []

    if month==None:
        sql = "SELECT * FROM transactions ORDER by date DESC"
        results = run_sql(sql)
    else:
        # sql= "SELECT to_char(date, 'month') as month, extract(month from date) as m, sum(""amount"") as ""amount"" FROM transactions group by 1,2"
        sql="SELECT * FROM transactions WHERE to_char(date, 'MM') = %s ORDER by date DESC "
        values = [month]
        results = run_sql(sql, values)
    for result in results:
        merchant = merchant_repository.select(result['merchant_id'])
        category = category_repository.select(result['category_id'])
        transaction = Transaction(merchant, category, result['description'], result['amount'], result['date'], result['id'])
        transactions.append(transaction)
    return transactions

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)
    

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET (merchant_id, category_id, description, amount, date) =(%s, %s, %s, %s, %s) WHERE id = %s"
    values = [transaction.merchant.id, transaction.category.id, transaction.description, transaction.amount, transaction.date, transaction.id]
    run_sql(sql, values)

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = merchant_repository.select(result['merchant_id'])
        category = category_repository.select(result['category_id'])
        transaction = Transaction(merchant, category, result['description'], result['amount'], result['date'], result['id'])
    return transaction
