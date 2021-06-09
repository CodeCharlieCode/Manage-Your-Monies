from flask import Blueprint, Flask, redirect, render_template, request

from models.transactions import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repositiory as transaction_repository
import repositories.category_repository as category_repository

transactions_blueprint = Blueprint("transactions",__name__)

@transactions_blueprint.route("/transactions/")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions = transactions)