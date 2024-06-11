from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Book

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admin')
def admin_home():
    books = Book.query.all()
    return render_template('admin_home.html', books=books)

@admin_bp.route('/admin/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        published_date = request.form['published_date']
        description = request.form['description']

        new_book = Book(title=title, author=author, isbn=isbn, published_date=published_date, description=description)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('admin_bp.admin_home'))

    return render_template('add_book.html')

@admin_bp.route('/admin/update/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.isbn = request.form['isbn']
        book.published_date = request.form['published_date']
        book.description = request.form['description']
        
        db.session.commit()
        return redirect(url_for('admin_bp.admin_home'))

    return render_template('update_book.html', book=book)

@admin_bp.route('/admin/delete/<int:id>')
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('admin_bp.admin_home'))
