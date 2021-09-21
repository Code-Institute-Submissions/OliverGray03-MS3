import os
import random
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def home():
    carousel_recipes = list(
        mongo.db.recipe_detail.find({"created_by": "admin"}))
    random.shuffle(carousel_recipes)

    recipes = list(mongo.db.recipe_detail.find())

    return render_template(
        "home.html",
        carousel_recipes=carousel_recipes,
        recipes=recipes)


@app.route("/get_recipe", methods=["GET", "POST"])
def get_recipe():
    if request.method == "POST":

        query = request.form.get("query")
        category_search = request.form.get("category_search")

        dbSearch = {}
        if query != "":
            dbSearch["$text"] = {"$search": query}

        if category_search is not None:
            dbSearch["category_name"] = category_search

        recipes = list(mongo.db.recipe_detail.find(dbSearch))
        categories = mongo.db.categories.find().sort("category_name", 1)

        return render_template(
            "get_recipe.html",
            recipes=recipes,
            categories=categories)

    recipes = mongo.db.recipe_detail.find()
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "get_recipe.html",
        recipes=recipes,
        categories=categories)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        gf_free = "on" if request.form.get("gf_free") else "off"
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "servings": int(request.form.get("servings")),
            "prep_time": int(request.form.get("prep_time")),
            "cook_time": int(request.form.get("cook_time")),
            "gf_free": gf_free,
            "ingredients": request.form.getlist("ingredients"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_method": request.form.getlist("method"),
            "created_by": session["user"],
            "difficulty": request.form.get("difficulty"),
            "cuisine": request.form.get("cuisine")
        }

        mongo.db.recipe_detail.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipe"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    difficulty = mongo.db.difficulty.find().sort("difficulty", 1)
    return render_template(
        "add_recipe.html",
        categories=categories,
        difficulty=difficulty)


@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):
    if "user" not in session:
        flash("You must register to be able to view a recipe")
        return redirect(url_for("register"))

    recipe = mongo.db.recipe_detail.find_one({"_id": ObjectId(recipe_id)})

    if recipe is None:
        abort(404)

    if session["user"]:
        return render_template(
            "full_recipe.html",
            recipe=recipe
        )
    else:
        flash("Please login to veiw the full recipe")
        return render_template(url_for("register"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if username already exists: flash message
        if existing_user:

            flash("Username already exists")
            return redirect(url_for("register"))

        # update mongoDB users collection
        register = {
            "firstname": request.form.get("firstname").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "saved_recipes": [],
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html", backgroundimage=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):

                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", backgroundimage=True)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    currentUser = mongo.db.users.find_one(
        {"username": session["user"]})
    username = currentUser["username"]

    saved_recipes = []

    if session["user"] == "admin":
        recipes = list(mongo.db.recipe_detail.find())
    else:
        recipes = list(mongo.db.recipe_detail.find(
            {"created_by": session['user']}))

    if "saved_recipes" in currentUser:
        for recipe_id in currentUser["saved_recipes"]:
            recipe = mongo.db.recipe_detail.find_one(
                {"_id": ObjectId(recipe_id)})
            saved_recipes.append(recipe)

    if session["user"]:
        return render_template(
            "profile.html",
            username=username,
            recipes=recipes,
            saved_recipes=saved_recipes)

    return redirect(url_for("login"))


@app.route("/remove_profile")
def remove_profile():

    # removes the session user from the database
    mongo.db.users.delete_one({"username": session["user"]})

    # removes the user from the session
    session.pop("user")
    flash("Your profile has been succesfully deleted")
    return redirect(url_for("register"))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    recipe = mongo.db.recipe_detail.find_one({"_id": ObjectId(recipe_id)})

    created_by = recipe['created_by']

    if session["user"] == "admin" or created_by == session["user"]:
        mongo.db.recipe_detail.delete_one(recipe)
        flash("Recipe Successfully Deleted")
        return redirect(url_for("profile", username=session['user']))
    else:
        abort(403)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):

    recipe = mongo.db.recipe_detail.find_one({"_id": ObjectId(recipe_id)})
    created_by = recipe['created_by']

    if request.method == "POST":
        gf_free = "on" if request.form.get("gf_free") else "off"
        edit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "servings": int(request.form.get("servings")),
            "prep_time": int(request.form.get("prep_time")),
            "cook_time": int(request.form.get("cook_time")),
            "gf_free": gf_free,
            "ingredients": request.form.getlist("ingredients"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_method": request.form.getlist("method"),
            "created_by": created_by,
            "difficulty": request.form.get("difficulty"),
            "cuisine": request.form.get("cuisine")
        }

        mongo.db.recipe_detail.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("home"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    difficulty = mongo.db.difficulty.find().sort("difficulty", 1)

    if session["user"] == "admin" or created_by == session["user"]:
        return render_template(
            "edit_recipe.html",
            recipe=recipe,
            categories=categories,
            difficulty=difficulty)


@app.route("/save/<recipe_id>", methods=["POST"])
def save_recipe(recipe_id):
    user = mongo.db.users.find_one({"username": session["user"]})

    if "saved_recipes" in user:
        if recipe_id in user["saved_recipes"]:
            flash("Recipe already saved")
            return redirect(url_for("profile", username=session['user']))

    mongo.db.users.update_one(
        user, {"$push": {"saved_recipes": recipe_id}})
    flash("Recipe saved to profile")
    return redirect(url_for("profile", username=session['user']))


@app.route("/remove/<recipe_id>", methods=["GET", "POST"])
def delete_saved_recipe(recipe_id):

    username = mongo.db.users.find_one({"username": session["user"]})

    mongo.db.users.update_one(
        username, {"$pull": {"saved_recipes": (recipe_id)}})
    flash("Recipe Removed from Profile")
    return redirect(url_for("profile", username=session['user']))


@app.errorhandler(404)
def not_found(e):
    return (render_template("404.html"), 404)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=False)
