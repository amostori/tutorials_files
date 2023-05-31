Po instalacji Mongo pojawia się problem z brakiem uprawnień do uzycia pliku WiredTiger.turtle. Trzeba je zmienić.  
Unable to start mongo instance on Mac OS Monterrey 12.6 using homebrew:   
`sudo chown osUserName /opt/homebrew/var/mongodb/WiredTiger.turtle`  
`sudo chown osUserName /opt/homebrew/var/mongodb/journal/WiredTiger*`  

---
`brew services start mongodb-community@6.0` - uruchomienie serwera Mongo  
`mongosh` - rozpoczęcie pracy z Mongo  
 `brew services list`  
 `brew services stop mongodb-community@6.0` - zatrzymanie serwera 

