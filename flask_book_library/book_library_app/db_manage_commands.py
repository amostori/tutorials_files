import json
from pathlib import Path
from book_library_app import app, db
from book_library_app.models import Author
from datetime import datetime


# W ten sposób można dodać komendy do flaska. Aby je zobaczyć należy w terminal wpisać `flask`

@app.cli.group()
def db_manage():
    """Database management commands"""
    pass


@db_manage.command()
def add_data():
    """Add sample data to database"""
    try:
        authors_path = Path(__file__).parent / 'samples' / 'authors.json'
        with open(authors_path) as file:
            # plik jest w formacie .json więc trzeba je przekonwertować na pythonowski dict
            data_json = json.load(file)
        for item in data_json:
            # strptime() przekształca String na obiekt DateTime
            # date() przeszktałca obiekt DateTime na obiekt Date
            item['birth_date'] = datetime.strptime(item('birth_date'), '%d-%m-%Y').date()
            author = Author(**item)
            db.session.add(author)
        db.session.commit()
        print('Data has been added')
    except Exception as exc:
        print(f'Unexpected error: ${exc}')


@db_manage.command()
def remove_data():
    """Remove all data from database"""

    try:
        # Polecenie SQL TRUNCATE TABLES authors usuwa wszystkie dane z tabeli authors i resetuje klucz podstawowy
        db.session.execute('TRUNCATE TABLES authors')
        db.session.commit()
        print('Data has been removed')
    except Exception as exc:
        print(f'Unexpected error: ${exc}')
