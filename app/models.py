from flask import  url_for
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from app import db


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    image = db.Column(db.String(250))
    page = db.Column(db.Integer)


    def __str__(self):
        return self.title

    # @property
    # def image_url(self):
    # return url_for('static', filename=f"images/{self.image}")

    # @property
    # def image_url(self):
    #     return url_for('static', filename=f"/images/{self.image}")

    @property
    def image_url(self):
        return url_for('static', filename=f"images/{self.image}")

    @property
    def show_url(self):
        return url_for('books.show', id=self.id)

    @property
    def delete_url(self):
        return url_for('books.delete', id=self.id)


