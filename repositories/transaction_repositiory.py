from db.run_sql import run_sql
from models.transactions import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.category_repository as cateogry_repository

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, category_id, description, amount) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.merchant.id, transaction.category.id, transaction.description, transaction.amount]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for result in results:
        merchant = merchant_repository.select(result['merchant_id'])
        category = cateogry_repository.select(result['category_id'])
        transaction = Transaction(merchant, category, result['description'], result['amount'], result['id'])
        transactions.append(transaction)
    return transactions