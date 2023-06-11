Po instalacji Mongo pojawia się problem z brakiem uprawnień do uzycia pliku WiredTiger.turtle. Trzeba je zmienić.  
Unable to start mongo instance on Mac OS Monterrey 12.6 using homebrew:   
`sudo chown osUserName /opt/homebrew/var/mongodb/WiredTiger.turtle`  
`sudo chown osUserName /opt/homebrew/var/mongodb/journal/WiredTiger*`

`brew services start mongodb-community@6.0` - uruchomienie serwera Mongo  
`mongosh` - rozpoczęcie pracy z Mongo  
`brew services list`  
`brew services stop mongodb-community@6.0` - zatrzymanie serwera
`show dbs`  
`use <nazwa_bazy_danych>` - utworzenie nowej bazy danych lub start pracy z istniejącą już. Po
tej komendzie użyj `db` jako odniesienie do bazy.
Dane są przechowywane jako Collections.

`db.<nazwa_kolekcji>.insertOne({<nazwa_klucza>:"<nazwa_wartości>"})` - utworzenie kolekcji o
podanej nazwie i dodanie dokumentu.   
Pozostałe komendy: insertMany(), find(), findOne(), updateOne(), updateMany(), replaceOne(), deleteOne(), deleteMany()

```
db.<nazwa_kolekcji>.insertMany([
{
"departureAirport": "MUC",
"arrivalAirport": "SFO",
"aircraft": "Airbus A380",
"distance": 12000,
"intercontinental": true
"status": {"description": "on-time"}
},
{
"departureAirport": "LHR",
"arrivalAirport": "TXL",
"aircraft": "Airbus A320",
"distance": 950,
"intercontinental": false
}
])
```

`db.<nazwa_kolekcji>.find().pretty()`
`db.<nazwa_kolekcji>.deleteOne({departureAirport: "TXL"})`

Aby wykonać update. Pierwszy argument służy do wyszukania dokumentu do zmiany, a drugi to element do zmiany przy pomocy
słowa kluczowego `$set`.   
`db.<nazwa_kolekcji>.updateOne({departureAirport: "TXL"}, {$set{marker: "delete"}})`

{} oznacza 'wybierz wszystkie dokumenty':
`db.<nazwa_kolekcji>.updateMany({}, {$set{marker: "toDelete"}})`

Funkcja `update()` nie wymaga $set, ale podmienia cały obiekt, podobnie jak funkcja replaceOne().
`db.<nazwa_kolekcji>.update({departureAirport: "TXL"}, {marker: "delete"})`

findAll()  
`db.<nazwa_kolekcji>.findAll({nazwa_pola_szukanego:"wartość_pola"})` - wyszukuje dokument z danymi podanymi w {}  
`db.<nazwa_kolekcji>.findAll({distance: {$gt:100}}).pretty()` - wyszukuje dokument posiadający pole "distance" o
wartości większej niż 100.

`db.<nazwa_kolekcji>.find()` - funkcja ta zwraca tzw. obiekt Cursor. Wyświetlanych jest pierwszych 20
dokumentów. Można na nim wykonywać metody `pretty()`, `forEach((doc){})`, `toArray()`.

### Projection

Projekcja to dane zwrocone, ale zawierające tylko pola, które interesują użytkownika. Projekcja to drugi nawias
klamrowy, w którym oznacza się dane do pobrania (1). Domyślnie zwracany jest też _id chyba, że oznaczymy to pole (0).
`db.passengers.find({}, {name: 1, _id:0})`

### Embedded documents - nested documents and arrays.

`db.<nazwa_kolekcji>.updateMany({}, {$set{status: {marker: "toDelete"}}})`
`db.<nazwa_kolekcji>.updateOne({name: "Albert Einstein"}, {$set{hobbies: ["sports", "programming"]}})`
Aby pobrać nested documents:
`db.<nazwa_kolekcji>.findOne({name: "Albert Einstein"}).hobbies` zwraca `["sports", "programming"]`
`db.<nazwa_kolekcji>.find({"status.descriptions": "on-time"})` zwraca zagnieżdżony obiekt `status.descriptions`, który w
takiej sytuacji musi być w cudzysłowiu.

Przykład zagnieżdżonego obiektu 'description':

```
{
    "distance": 12000,
    "intercontinental": true
    "status": {
        "description": "on-time"
            }
}
```






