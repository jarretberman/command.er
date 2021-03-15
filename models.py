from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect the database to the Flask App
    """

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User Model"""
    
    def __repr__ (self):
        """Clearer Representation String"""
        return f'<User {self.id} : {self.username}, {self.email}>'
    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )


    @classmethod
    def signup(cls, username, email, password):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.
        If it finds such a user, returns that user object.
        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False

class Deck(db.Model): # Deck >--User
    """Deck Model """

    __tablename__ = 'decks'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    name = db.Column(
        db.Text,
        nullable=False,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )

    user = db.relationship('User', backref ='decks')

    cards = db.relationship(
        'Card',
        secondary= 'deck_cards',
        backref='decks'
    )

class DeckCard(db.Model):
    """ Many to Many table for Decks and Cards"""

    __tablename__ = 'deck_cards'

    deck_id = db.Column(
        db.Integer,
        db.ForeignKey('decks.id', ondelete='CASCADE'),
        nullable = False,
        primary_key=True
    )

    card_id = db.Column(
        db.Integer,
        db.ForeignKey('cards.scryfall_id', ondelete='CASCADE'),
        nullable = False,
        primary_key=True
    )

class Card(db.Model):
    """Model for saving cards from Scryfall API to decks"""

    __tablename__= 'cards'

    scryfall_id = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(
        db.String(50),
        nullable=False,
    )