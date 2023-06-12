from flask import jsonify, request
from webargs.flaskparser import use_args

from book_library_app import app, db
from book_library_app.models import Author, AuthorSchema, author_schema


@app.route('/api/v1/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    # parametr 'many=True' informuje marshmallow, że przekazujemy listę obiektów
    author_schema = AuthorSchema(many=True)
    # dump przekształca obiekty na format json
    return jsonify({
        'success': True,
        'data': author_schema.dump(authors),
        'number_of_records': len(authors)
    })


# use_args zwaliduje dane przesłane wg author_schema i zwróci je jako dictionary
# zmienna args to dictionary z zwalidowanymi danymi, który można wykorzystać do stworzenia obiektu Author
@app.route('/api/v1/authors', methods=['POST'])
@use_args(author_schema, error_status_code=400)
def create_author(args: dict):
    author = Author(**args)
    db.session.add(author)
    db.session.commit()
    return jsonify({
        'success': True,
        'data': author_schema.dump(author)
    }), 201


@app.route('/api/v1/authors/<int:author_id>', methods=['GET'])
def get_author(author_id: int):
    author = Author.query.get_or_404(author_id, description=f'Author with {author_id} does not exists.')

    return jsonify({
        'success': True,
        'data': author_schema.dump(author)
    })


@app.route('/api/v1/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id: int):
    return jsonify({
        'success': True,
        'data': f'Author with id = ${author_id} has been updated'
    })


@app.route('/api/v1/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id: int):
    return jsonify({
        'success': True,
        'data': f'Author with id = ${author_id} has been deleted'
    })
