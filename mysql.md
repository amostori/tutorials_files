`mysql -u root -p` - rozpoczęcie pracy z mysql (Pln77)
`show databases;` - jak nazwa wskazuje  
`show tables;` - jak nazwa wskazuje  
`select * from <nazwa_tabeli>;` - jak nazwa wskazuje  
`exit`
Aby zmienić hasło roota:
Po zalogowaniu do mysql wykonaj:
`use mysql;` - następnie:
`ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY '<nowe_hasło>';`
`exit` i zaloguj się ponownie

Utworzenie nowej db dla nowego użytkownika:
`create database <nazwa_bazy_danych>;`
`create user '<nazwa_uzytkownika>'@'localhost' identified by '<hasło_nowego_uzytkownika>';`
`grant all on <nazwa_bazy_danych>.* to '<nazwa_uzytkownika>'@'localhost';`

---
`SQLALCHEMY_DATABASE_URI=mysql+pymysql://<nazwa_uzytkownika>:<hasło_uzytkownika>@localhost/<nazwa_db>?charset=utf8mb4`

W celu zbudowania bazy danych zainstaluj flask-migrate:
`pip install flask-migrate`
Następnie w pliku inicjacyjnym należy skonfigurować flask-migrate:
`migrate = Migrate(app, db)`
a w terminalu wykonać:
`flask db init` - inicjuje flask-migrate
`flask db migrate -m "<notatka>"` - tworzy pliki do migracji
`flask db upgrade` - dokonuje utworzenie bazy danych na podstawie plików migracji.

`flask run`
Kiedy uruchamiamy aplikację tą komendą odczytywany jest plik .flaskenv i to tam ma być ustawiona zmienna FLASK_APP.

