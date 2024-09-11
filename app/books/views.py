from flask import Flask, render_template, request, redirect, url_for
from app.models import Book, db
from app.books import book_blueprint
from werkzeug.utils import secure_filename
from app.books.forms import BookForm
import os



@book_blueprint.route("", endpoint='landing')
def books_landing():
    books = Book.query.all()
    return render_template('landing.html', books=books)

##################### Show book details #####################
@book_blueprint.route("<int:id>/show", endpoint='show')
def books_show(id):
    book = db.get_or_404(Book, id)
    return render_template('show.html', book=book)

##################### Create a new book #####################
@book_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
def books_create():
    form = BookForm()
    if request.method == 'POST':
        image_name=None
        if request.files.get('image'):
            image= form.image.data
            image_name= secure_filename (image.filename)
            image.save(os.path.join('app/static/images', image_name))
        new_book = Book(
            title=request.form['title'],
            description=request.form['description'],
            # image=request.form['image'],
            page=request.form['page'],
            image=image_name
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('books.landing'))
    return render_template('create.html', form=form)

##################### Edit book details #####################
@book_blueprint.route('<int:id>/edit', endpoint='edit', methods=['GET', 'POST'])
def books_edit(id):
    book = db.get_or_404(Book, id)
    form = BookForm(obj=book)
    if request.method == 'POST' and form.validate_on_submit():
        book.title = form.title.data
        book.description = form.description.data
        book.page = form.page.data
        if request.files.get('image'):
            image = form.image.data
            image_name= secure_filename (image.filename)
            image.save(os.path.join('app/static/images', image_name))
            book.image = image_name
        # book.image = request.form['image']
        
        db.session.commit()
        # return redirect(url_for('books.show', id=book.id))
        return redirect(book.show_url)
    return render_template('edit.html', form=form, book=book)

##################### Delete a book #####################
@book_blueprint.route('<int:id>/delete', endpoint='delete', methods=['GET', 'POST'])
def books_delete(id):
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('books.landing'))