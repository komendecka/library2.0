from app import db
from sqlalchemy.orm import relationship


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    author = db.Column(db.String(200), index=True, unique=True)

    def __str__(self):
        return f"<Book {self.title}>"


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True, unique=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Author {self.id} {self.name[:50]} ...>"


class Borrowed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    on_shelf = db.Column(db.Boolean, index=True, default=True)

    book = relationship("Book", backref="borrowed_books")

    def __str__(self):
        book_title = self.book.title if self.book else "Unknown"
        return f"<The book is on shelf {self.id} - Title: {book_title} - On shelf: {self.on_shelf}>"