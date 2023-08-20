Po zainstalowaniu pakietów 'hive' i 'hive_flutter' dodaj jeszcze pakiet 'path_provider'.
Teraz w funkcji 'main' aplikacji zainicjuj Hive:

```
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  Directory directory = await getApplicationDocumentsDirectory();
  Hive.init(directory.path);
  runApp(const MyApp());
}
```  

Hive przechowuje dane w 'boxach'. Należy otworzyć taki box w dowolnym miejscu, np w 'main':
`await Hive.openBox('<nazwa_boxa>');`  
Aby uzyskać dostęp do boxa:
`var box = Hive.box('<nazwa_boxa>');`  
By go zamknąć w dispose():  
`Hive.close();`  
`super.dispose();`  
Dodanie danych do boxa:  
`box.put('<key_name>','<value_name>');`
Dodanie danych, jak lista, z indexem:
`box.add('<name>');` - index 0, wartość 0  
`box.add('<name2>');` - index 1, wartość 1  
Pobieranie danych:  
`var name = box.get('<key_name>);`  
Update danych:  
`box.put('<key_name>','<value_name>');` lub podając index:
`box.putAt(0, '<value>');`  
Kasowanie danych:  
`box.delete('<key_name>');` lub podając index:  
`box.deleteAt(<nr_indexu>);`  
    
