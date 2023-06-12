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
