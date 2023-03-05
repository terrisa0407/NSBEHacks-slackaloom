from flask import Blueprint, render_template

slackaloom = Blueprint("slackaloom", __name__)

#Selection 1
@slackaloom.route("/home")
def home():
    return render_template("slackloom.html")

@slackaloom.route("/social1left")
def home2():
    return render_template("socialhome2.html")

@slackaloom.route("/social1right")
def home3():
    return render_template("socialhome3.html")

@slackaloom.route("/social2left")
def home4():
    return render_template("socialhome4.html")

@slackaloom.route("/social2right")
def home5():
    return render_template("socialhome5.html")

@slackaloom.route("/healthfirst")
def home6():
    return render_template("healthfirst.html")

@slackaloom.route("/healthsecond")
def home7():
    return render_template("healthsecond.html")

@slackaloom.route("/education")
def home8():
    return render_template("education.html")

@slackaloom.route("/finance")
def home9():
    return render_template("finance.html")

