from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions = sessions)

# @sessions_blueprint.route("/sessions/upcoming", methods=["GET"])
# def sessions_upcoming():
#     sessions = session_repository.select_all()
#     return render_template("sessions/upcoming.html", sessions = sessions)

@sessions_blueprint.route("/sessions/<id>")
def show(id):
    session = session_repository.select(id)
    members = session_repository.members(session)
    return render_template("sessions/show.html", session = session, members = members)

@sessions_blueprint.route("/sessions/new", methods=['GET'])
def new_session():
    sessions = session_repository.select_all()
    return render_template("sessions/new.html", sessions = sessions)

@sessions_blueprint.route("/sessions", methods = ['POST'])
def create_session():
    name = request.form['name']
    category = request.form['category']
    date = request.form['date']
    time = request.form['time']
    session = Session(name, category, date, time)
    session_repository.save(session)
    return redirect("/sessions")

@sessions_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete_session(id):
    session_repository.delete(id)
    return redirect('/sessions')

@sessions_blueprint.route("/sessions/<id>/edit", methods=["GET"])
def edit_session(id):
    session = session_repository.select(id)
    return render_template('sessions/edit.html', session = session)

@sessions_blueprint.route("/sessions/<id>", methods=['POST'])
def update_session(id):
    name = request.form['name']
    category = request.form['category']
    date = request.form['date']
    time = request.form['time']
    session = Session(name, category, date, time, id)
    session_repository.update(session)
    return redirect('/sessions')

