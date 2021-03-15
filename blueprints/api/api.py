from flask import Blueprint, render_template, g, flash, redirect, session, jsonify, request
from models import User, Deck, DeckCard, Card, db
# from .forms import PostForm, CommentForm
# from ..post.post import post

api = Blueprint("api", __name__, template_folder="templates", static_folder="static")

@api.route('/')
def show_home():

    return jsonify({"working":"as intended"})

# /users
@api.route('/users')
def get_all_users():
    if g.user:
        users = User.query.all()
        return jsonify(users)

    else:
        flash('Please Login', 'secondary')
        return redirect('/')

#/users/:username
@api.route('/users/<username>')
def get_one_user(username):
    if g.user:
        user = User.query.filter(User.username == username).first()
        return jsonify(user)

    else:
        flash('Please Login', 'secondary')
        return redirect('/')


# /decks

@api.route('/decks')
def get_all_decks():
    if g.user:
        deck = Deck.query.all()
        return jsonify(deck)

    else:
        flash('Please Login', 'secondary')
        return redirect('/')


# /decks/:id
@api.route('/decks/<int:id>')
def get_one_deck(id):
    if g.user:
        deck = Deck.query.get_or_404(id)
        return jsonify(deck)
    else:
        flash('Please Login', 'secondary')
        return redirect('/')

# /cards/:id
@api.route('/cards/<id>')
def get_one_card(id):
    if g.user:
        card = Card.query.filter(Card.scryfall_id == id)
        return jsonify(card)
    else:
        else:
        flash('Please Login', 'secondary')
        return redirect('/')


# /cards
@api.route('/cards', methods = ['POST'])
def add_cards():
    cards = request.json
    db_cards = []
    for card in cards:
        card = Card(scryfall_id = card.id,name=card.name)
        db_cards.add(card)
    db.session.add_all(db_cards)
    db.session.commit()

    return jsonify({working:'as intended'})
    
    

