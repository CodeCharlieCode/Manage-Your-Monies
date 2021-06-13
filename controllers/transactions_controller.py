from flask import Blueprint, Flask, redirect, render_template, request

from models.transactions import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repositiory as transaction_repository
import repositories.category_repository as category_repository

transactions_blueprint = Blueprint("transactions",__name__)

@transactions_blueprint.route("/transactions/")
def transactions():
    transactions = transaction_repository.select_all()
    total = 0
    for transaction in transactions:
        total += transaction.amount
    total_amount = round(total, 2)
    return render_template("transactions/index.html", transactions = transactions, total_amount = total_amount)

@transactions_blueprint.route("/transactions/new")
def new():
    transactions = transaction_repository.select_all()
    merchants = merchant_repository.select_all()
    categories = category_repository.select_all()
    return render_template("transactions/new.html", transactions = transactions, merchants = merchants, categories = categories)

@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    merchant_id = request.form['merchant_id']
    category_id = request.form['category_id']
    amount = request.form['amount']
    description = request.form['description']
    date = request.form['date']
    merchant = merchant_repository.select(merchant_id)
    category = category_repository.select(category_id)
    transaction = Transaction(merchant, category, description, amount, date)
    transaction_repository.save(transaction)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    merchant_id = request.form['merchant_id']
    amount = request.form['amount']
    description = request.form['description']
    date = request.form['date']
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(merchant, merchant, description, amount, date, id)
    transaction_repository.update(transaction)
    return redirect("/transactions")

