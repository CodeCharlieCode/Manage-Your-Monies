from flask import Blueprint, Flask, redirect,render_template, request

from models.profile import Profile
import repositories.profile_repository as profile_repository

profile_blueprint = Blueprint("profiles",__name__)

@profile_blueprint.route("/profiles/")
def profile():
    profile = profile_repository.select_all()
    profile1= Profile(0, 0)
    profile_repository.save(profile1)   
    return render_template("profiles/index.html", profile = profile, profile1 = profile1)