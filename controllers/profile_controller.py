from flask import Blueprint, Flask, redirect,render_template, request

from models.profile import Profile
import repositories.profile_repository as profile_repository
import repositories.transaction_repositiory as transaction_repository

profile_blueprint = Blueprint("profiles",__name__)

@profile_blueprint.route("/profiles/")
def profiles():
    profiles = profile_repository.select_all()
    transactions = transaction_repository.select_all()

    total = 0
    for transaction in transactions:
        total += transaction.amount
    total_amount = round(total, 2)
    # for profile in profiles:
    #     over_budget = profile.total_budget - total_amount
    #     if total_amount > profile.balance:
    #         return render_template("profiles/insufficient.html", profiles = profiles, profile = profile, over_budget = over_budget)  
    return render_template("profiles/index.html", profiles = profiles, total_amount = total_amount)

@profile_blueprint.route("/profiles/new")
def new():
    profiles = profile_repository.select_all()
    return render_template("profiles/new.html", profiles = profiles)

@profile_blueprint.route("/profiles/<id>", methods=['GET'])
def show_profile(id):
    profile = profile_repository(id)
    return render_template("profiles/index.html", profile = profile)

@profile_blueprint.route("/profiles", methods=['POST'])
def create_profile():
    balance = request.form['balance']
    total_budget = request.form['total_budget']
    profile = Profile(balance, total_budget)
    profile_repository.save(profile)
    return redirect("/profiles")

@profile_blueprint.route("/profiles/<id>/edit", methods=['GET'])
def edit_profile(id):
    profile = profile_repository.select(id)
    return render_template("/profiles/edit.html", profile = profile)

@profile_blueprint.route("/profiles/<id>", methods=['POST'])
def update_profile(id):
    balance = request.form['balance']
    total_budget = request.form['total_budget']
    profile = Profile(balance, total_budget, id)
    profile_repository.delete(id)
    profile_repository.update(profile)
    profile_repository.save(profile)
    return redirect("/profiles")

