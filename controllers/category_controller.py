from controllers.transactions_controller import transactions
from flask import Blueprint, Flask, redirect,render_template, request

from models.category import Category

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repositiory as transaction_repository
import repositories.category_repository as category_repository

category_blueprint = Blueprint("categories",__name__)

@category_blueprint.route("/categories/")
def categories():
    categories = category_repository.select_all()
    return render_template("categories/index.html", categories = categories)