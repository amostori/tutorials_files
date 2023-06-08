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

### Deleting data.

`git ls-files` - jakie pliki są w staging area