from flask import Blueprint, render_template, g, flash, redirect, session, jsonify
from models import User, Deck, DeckCard, Card, db
# from .forms import PostForm, CommentForm
# from ..post.post import post

builder = Blueprint("builder", __name__, template_folder="templates", static_folder="static")

@builder.route('/')
def show_home():

    return render_template('builder/builder.html')


#/edit/:id -- post route to "load" the builder with an already working decklist.

#/copy/:id -- post route to open a copy of another users deck in the builder to save for current user

