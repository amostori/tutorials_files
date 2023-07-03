`git log` - podejrzenie komitów
`git checkout <branch_name>` lub `git switch <branch_name>` - przejście do ostatniego komitu w gałęzi o podaniej
nazwie.  
`git branch` - wyświetla nazwę gałęzi.  
`git branch <branch_name>` - tworzy gałąź.  
`git checkout -b <branch_name>` lub `git switch -c <branch_name>`- tworzy gałąź i do niej przechodzi.  
Merging branch
Z poziomu jednej gałęzi przyłącza się drugą. Zwykle z 'master' przyłącza się inną do 'master'.
`git checkout master`
`git merge <branch_name>`

Detached head.
Kiedy jesteś w tym trybie, nie jesteś na żadnej gałęzi. Aby wrócić należy: `git checkout <branch_name>`.

### Deleting data przed `git add`

`git ls-files` - jakie pliki są w unstaging area (jakie git śledzi).
` git rm --cached <path/file_name>` - usunięcie pliku ze śledzonych przez gita.

Po usunięciu jakiegoś pliku z working directory należy wykonać `git add .` by usunąć go z unstaging area.

`git checkout <nazwa_pliku>` - usunięcie ostatnich zmian w pliku o podanej nazwie aż do ostatniego commitu w bieżącej
gałęzi.
`git checkout .` - usunięcie ostatnich zmian we wszystkich plikach aż do ostatniego commitu w bieżącej gałęzi.
Zamiast `git checkout` można użyć komendy `git restore`.
`git clean -dn` - usunięcie pliku dodanego po ostatnim commicie. Pojawi się info jakie pliki będą usunięte ('n' listuje
te pliki), ('d' oznacza usunięcie untracted files).  
`git clean -df` - dokonanie usunięcia ('f' - force).

#### Deleting zmian w pliku po komendzie `git add .`:

Należy wykonać `git restore --staged <nazwa_pliku>` a następnie `git checkout <nazwa_pliku>`.

#### Deleting zmian w pliku po komendzie `git commit -m "<opis>`:

`git reset --soft HEAD~1` - wymazanie ostatniego commita, ale zmiany w plikach pozostają w staging area (jaki po git
add).
`git reset HEAD~1` - wymazanie ostatniego commita, ale zmiany w plikach pozostają, ale nie ma ich w staging area.
`git reset --hard HEAD~1` - wymazanie ostatniego commita, razem ze zmianami w plikach (usuwa też pliki dodane ostatnio).

#### Deleting branches

`git branch -d <nazwa_gałęzi>` - usuń gałąź, która jest połączona z główną (po 'git merge').
`git branch -D <nazwa_gałęzi>` - usuń gałąź, bez względu na to czy jest połączona z główną (po 'git merge').

### Detached head

Jeśli chcesz dodać coś w innym commicie zrób `git checkout <nr_commita>` - jesteś w trybie Detached HEAD - zrób zmiany,
dodaj je (`git add .`) i zakomituj (`git commit -m "<opis>"`) a następnie stwórz nową gałąź `git branch <nowa_gałąź>`.  
Teraz wróć do gałęzi 'master' (`git switch master`) i zrób merge (`git merge <nowa_gałąź>`). Możesz usunąć niepotrzebną
gałąź (`git branch -D <nowa_gałąź>`).

### .gitignore

`*.<file_extension>` - ignoruje wszystkie pliki o rozszerzeniu <file_extension>.
`!<file_name>.<file_extension>` - ignoruje wszystkie pliki o rozszerzeniu <file_extension> za wyjątkiem podanego.

#### git stash

Stash pozwala zapisywać zmiany w pamięci podręcznej i w dowolnym momencie je przywracać.
`git stash` zapisuje najnowsze dane w pamięci podręcznej (stash) i równocześnie resetuje wszystkie zmiany do ostatniego
komitu.
`git stash push -m "<opis>"` jak wyżej, ale z opisem
`git stash list` - listuje stash
`git stash pop <index_stashu>` - przywraca zmiany ze stasha o odpowiednim indexie równocześnie usuwając stasha ze
stasha.
`git stash apply` - przywraca ostatnie zmiany ze stasha. Można je teraz dodać i zakomitować.
`git stash drop <index_stashu>` - usuwa stasha o podanym indexie ze stasha.  
`git stash clear` - usuwa wszystkie stashe ze stasha.

#### git reflog

`git reflog` służy do odzyskiwania skasowanych komitów i gałęzi. Komenda ta daje podgląd na wszystkie operacje wykonane.
Przykładowo: po komendzie `git reset --hard HEAD~1` usunęliśmy ostatni komit. Teraz należy podejrzeć hash tego komita
komendą
`git reflog` i następnie `git reset --hard <hash komita usuniętego>` by przywrócić komita.
Po usunięciu brancha komendą `git branch -D <nazwa_gałęzi>` również należy podejrzeć hash komita z gałęzią usuniętą i
wykonać `git checkout <hash komita>`. Znajdziemy się w trybie 'detached'. Teraz stwórz nową gałąź o nazwie
usuniętej `git switch -c <branch_name>`. I już.

### Merge i rozwiązywanie konfliktów

Merge może przebiegać w różnych trybach. Gdy gałąź 'master' jest niezmieniana komenda `git merge <branch_name>` (
wykonana z poziomu 'master') powoduje
dodanie zmian i komitów do 'master' w trybie 'fast-forward'. Nie jest tworzony żaden nowy komit.  
Jeśli nie chcesz mieć wszystkich komitów z innej gałęzi, tylko same zmiany użyj:
`git merge --squash <branch_name>` - spowoduje to dołączenie tylko zmian z jednej gałęzi do 'mastera', bez komitów. Po
komendzie tej należy utworzyć komit i opisać go np jako dodanie nowego feature'a.  
`git merge --no-ff <branch_name>` - merge bez 'fast-forward', czyli 'recursive'. Powoduje zachowanie gałęzi i utworzenie
nowego commitu, z domyślnym komunikatem o dokonanym merge'u. 'Recursive' merge jest domyślnie ustawiony, gdy łączymy
nową gałąź z masterem, u którego też wykonano jakieś zmiany (ma jakieś nowe komity).

### Git rebase

Rebase przepisuje historię commitów. Jakaś gałąź, w której powstały komity, po komendzie `git rebase` zmienia podstawę,
na której się opiera z mastera, który też został zaktualizowany w międzyczasie. Nie jest to zalecane postępowanie.

#### merge conflicts  
