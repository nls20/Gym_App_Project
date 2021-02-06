from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    sessions = member_repository.sessions(member)
    return render_template("members/show.html", member=member, sessions=sessions)

@members_blueprint.route("/members/new", methods=['GET'])
def new_member():
    members = member_repository.select_all()
    return render_template("members/new.html", members = members)

@members_blueprint.route("/members", methods = ['POST'])
def create_member():
    name = request.form['name']
    member = Member(name)
    member_repository.save(member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repository.delete(id)
    return redirect('/members')

@members_blueprint.route("/members/<id>/edit", methods=["GET"])
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member = member)

@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    name = request.form['name']
    member = Member(name, id)
    member_repository.update(member)
    return redirect('/members')
