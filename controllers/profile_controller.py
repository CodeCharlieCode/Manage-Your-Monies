from flask import Blueprint, Flask, redirect,render_template, request

from models.profile import Profile
from models.transactions import Transaction
import repositories.profile_repository as profile_repository
import repositories.transaction_repositiory as transaction_repository

profile_blueprint = Blueprint("profiles",__name__)

@profile_blueprint.route("/profiles/")
def profile():
    profile = profile_repository.select_all()
    profile1= Profile(0, 0)
    transactions = transaction_repository.select_all()
    total = 0
    for transaction in transactions:
        total += transaction.amount
    total_amount = round(total, 2)
    if total_amount > profile1.balance:
        return render_template("profiles/insufficient.html")
    profile_repository.save(profile1)   
    return render_template("profiles/index.html", profile = profile, profile1 = profile1, total_amount=total_amount)