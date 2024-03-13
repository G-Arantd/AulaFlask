from flask import request

from app import app
from app.Controller.Controle import *

@app.route("/view-user", methods=["GET"])
def view_user():
    
    data = request.json
    
    result = get_user(data)
    
    return result

@app.route("/add-user", methods=["POST"])
def add_user():
    
    data = request.json
    
    result = create_user(data)
    
    return result

@app.route("/edit-user", methods=["PUT"])
def edit_user():
    
    data = request.json
    
    result = update_user(data)
    
    return result

@app.route("/remove-user", methods=["DELETE"])
def remove_user():
    
    data = request.json
    
    result = delete_user(data)
    
    return result