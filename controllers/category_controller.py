from controllers.transactions_controller import transactions
from flask import Blueprint, Flask, redirect,render_template, request

from models.category import Category
import repositories.transaction_repositiory as transaction_repository
import repositories.category_repository as category_repository

category_blueprint = Blueprint("categories",__name__)

@category_blueprint.route("/categories/")
def categories():
    categories = category_repository.select_all()
    transactions =transaction_repository.select_all()
    total = 0
    for category in categories:
        total += category.budget
    sum_of_budgets = round(total, 2)
    return render_template("categories/index.html", categories = categories, sum_of_budgets = sum_of_budgets)

@category_blueprint.route("/categories/category/<id>")
def show(id):
    category = category_repository.select(id)
    # transactions = category_repository.transactions(category)
    transactions =transaction_repository.select_all()
    total = 0
    for transaction in transactions:
        if category.id == transaction.category.id:
            total += transaction.amount
        total_amount = round(total, 2)
    remaining_budget = category.budget -total_amount
    return render_template("categories/show.html", category = category, transactions = transactions, remaining_budget =remaining_budget)

@category_blueprint.route("/categories/new/")
def new():
    categories = category_repository.select_all
    return render_template("categories/new.html", categories = categories)

@category_blueprint.route("/categories", methods=['POST'])
def create_category():
    name = request.form['category']
    budget = request.form['budget']
    category = Category(name, budget)
    category_repository.save(category)
    return redirect("/categories/")

@category_blueprint.route("/categories/<id>/delete", methods = ['POST'])
def delete_category(id):
    category_repository.delete(id)
    return redirect("/categories/")

@category_blueprint.route("/categories/<id>", methods=['POST'])
def update_category(id):
    name = request.form['category']
    budget = request.form['budget']
    category = Category(name, budget, id)
    category_repository.update(category)
    return redirect("/categories/")



    