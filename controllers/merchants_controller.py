from repositories.category_repository import select_all
from flask import Blueprint, Flask, redirect, render_template, request

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repositiory as transaction_repository


merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants/")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants = merchants)

@merchants_blueprint.route("/merchants/<id>")
def show(id):
    merchant = merchant_repository.select(id)
    transactions = transaction_repository.select_all()
    return render_template("merchants/show.html", merchant = merchant, transactions = transactions)

@merchants_blueprint.route("/merchants/new/")
def new():
    merchants = merchant_repository.select_all()
    return render_template("merchants/new.html", merchants = merchants)

@merchants_blueprint.route("/merchants", methods=['POST'])
def create_merchant():
    name = request.form['name']
    merchant = Merchant(name)
    merchant_repository.save(merchant)
    return redirect("/merchants/")

@merchants_blueprint.route("/merchants/<id>/delete", methods = ['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect("/merchants/")

@merchants_blueprint.route("/merchants/<id>", methods=['POST'])
def update_merchant(id):
    name = request.form['name']
    merchant = Merchant(name, id)
    merchant_repository.update(merchant)
    return redirect("/merchants/")