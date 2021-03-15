from flask import Blueprint, render_template, g, flash, redirect, session, jsonify
from models import User, Deck, DeckCard, Card, db

search = Blueprint("search", __name__, template_folder="templates", static_folder="static")

@search.route('/')
def show_home():

    return render_template('search/search.html')
