from flask import Blueprint, render_template
from .models import Book

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def user_home():
    books = Book.query.all()
    return render_template('user_home.html', books=books)

@user_bp.route('/book/<int:id>')
def book_details(id):
    book = Book.query.get_or_404(id)
    return render_template('book_details.html', book=book)
