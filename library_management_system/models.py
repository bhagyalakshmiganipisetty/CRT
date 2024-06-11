from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    published_date = db.Column(db.String(10), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Book {self.title}>'
