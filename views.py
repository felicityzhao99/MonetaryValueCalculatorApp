from activities.monetary_value_calculator import get_monetary_value
from flask import Blueprint, render_template

"""
All views are listed below, including the default home view and the offer view.
"""
views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/offer")
def offer():
    url = "https://questionnaire-148920.appspot.com/swe/data.html"
    monetary_value = get_monetary_value(url)
    return render_template("offer.html", value=monetary_value)
