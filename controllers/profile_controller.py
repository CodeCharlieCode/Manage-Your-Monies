from flask import Blueprint, Flask, redirect,render_template, request

from models.profile import Profile
import repositories.profile_repository as profile_repository

profile_blueprint = Blueprint("profiles",__name__)

@profile_blueprint.route("/profiles/")
def profile(id):
    profile = profile_repository.select(id)
    return render_template("profiles/index.html", profile = profile)