from db.run_sql import run_sql
from models.transactions import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as category_repository

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, category_id, description, amount, date) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [transaction.merchant.id, transaction.category.id, transaction.description, transaction.amount, transaction.date]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

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
    values = [transaction.merchant.name, transaction.category.name, transaction.description, transaction.amount, transaction.date, transaction.id]
    run_sql(sql, values)

# def select(id):
#     transaction = None
#     sql = "SELECT * FROM transactions WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         merchant = merchant_repository.select(result['merchant_id'])
#         category = cateogry_repository.select(result['category_id'])
#         transaction = Transaction(merchant, category, result['description'], result['amount'], result['id'])
#     return transaction
