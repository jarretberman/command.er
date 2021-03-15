from flask import Blueprint, render_template, g, flash, redirect, session, jsonify
from models import User, Deck, DeckCard, Card, db

user = Blueprint("user", __name__, template_folder="templates", static_folder="static")

@user.route('/')
def show_home():

    return render_template('user/profile.html')



# /mydecks -- view list of all decks with some description features

# /deck/:id -- view deck list