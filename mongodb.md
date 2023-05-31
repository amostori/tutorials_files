Po instalacji Mongo pojawia się problem z brakiem uprawnień do uzycia pliku WiredTiger.turtle. Trzeba je zmienić.  
Unable to start mongo instance on Mac OS Monterrey 12.6 using homebrew:   
`sudo chown osUserName /opt/homebrew/var/mongodb/WiredTiger.turtle`  
`sudo chown osUserName /opt/homebrew/var/mongodb/journal/WiredTiger*`  

---
`brew services start mongodb-community@6.0` - uruchomienie serwera Mongo  
`mongosh` - rozpoczęcie pracy z Mongo  
 `brew services list`  
 `brew services stop mongodb-community@6.0` - zatrzymanie serwera 
`show dbs`  
`use <nazwa_bazy_danych>` - utworzenie nowej bazy danych lub start pracy z istniejącą już. Po 
tej komendzie użyj `db` jako odniesienie do bazy. 
---
Dane są przechowywane jako Collections. 
`db.<nazwa_kolekcji>.insertOne({<nazwa_klucza>:"<nazwa_wartości>"})` - utworzenie kolekcji o 
podanej nazwie i dodanie dokumentu.


