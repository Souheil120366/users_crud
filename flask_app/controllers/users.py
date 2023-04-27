from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route("/")
def index():
    return redirect('/users')

@app.route("/users")
def users_list():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("read.html",users_list=users)

@app.route("/users/<int:id>")
def user_show(id):
    # call the get all classmethod to get all friends
    users = User.get_user(id)
    print(users)
    return render_template("read_one.html",user=users)

@app.route("/users/<int:id>/edit")
def user_edit(id):
    users = User.get_user(id)
    print("user",users)
    return render_template("edit.html",user=users)

@app.route('/users/new')
def create_user():
            
    return render_template("create.html")

@app.route("/new",methods=['POST'])
def new_user():
    
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route("/update_user/<int:id>",methods=['POST'])
def update_user(id):
    User.update_user(id,request.form)
    
    return redirect('/users')

@app.route("/delete_user/<int:id>")
def delete_user(id):
    User.del_user(id)
    
    return redirect('/users')