`mysql -u root -p` - rozpoczęcie pracy z mysql (Pln77) 
`show databases;` - jak nazwa wskazuje  
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
