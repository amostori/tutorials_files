`docker build . ` - zbudowanie image  
`docker run -p 3000:80 <nr_image>` - uruchomienie image'u jako kontenera w trybie atached
`docker ps` - pokaz wszystkie kontenery pracujące
`docker ps -a` - pokaz wszystkie kontenery
`docker logs <nazwa_kontenera>` - pokaż logi, jak kontener się wysypie
`docker start <nazwa_kontenera>` - ponowne uruchomienie już istniejącego kontenera w trybie detached  
`docker stop <nazwa_kontenera>` - zatrzymanie istniejącego kontenera.
`docker attacha <nazwa_kontenera>` - przejście w tryb attach-będą widoczne logi.
`docker run -it <nr_image>` - uruchamia container w trybie interaktywnym (-i) oraz z terminalem (-t)
`docker start -a -i <nazwa_image'u>` - restartuje container w trybie attached i interaktywnym.

`docker rm <nazwa_kontenera>` - usunięcie kontenera (tylko jeśli jest zatrzymany).
`docker container prune` - usunięcie wszystkich zatrzymanych kontenerów.
`docker images` - listowanie image'ów.
`docker rmi <nazwa_image'u>` - usuwanie image'u (tylko jeśli nie ma konteneru).
`docker image prune` - usunięcie wszystkich image'ów nieposiadających kontenerów
`docker image prune -a` - usunięcie wszystkich image'ów nieposiadających kontenerów, również nazwanych i stagowanych.
`docker run -p 3000:80 -d --rm <nr_image>` - uruchomienie kontenera w trybie detached (-d) oraz z automatycznym jego
usunięciu po zakończeniu pracy (--rm).  
`docker image inspect`  - jak nazwa wskazuje - podgląd na wszystkie ustawienia image.

#### Nazywanie obrazów i kontenerów.

`docker run -p 3000:80 -d --rm --name <Dowolna_nazwa> <nr_image>` - uruchomienie kontenera i nazwanie go.
`docker build -t <nazwa>:<tag_name> .` - zbudowanie image'u z nazwą i tagiem.

#### Sharing images

Na stronie Docker Hub wybierz 'Create repository', nadaj nazwę dla repozytorium i wciśnij 'Create'. W terminalu, w
folderze z projektem wykonaj komendę:
`docker login` - trzeba podać login i hasło.
Aby projekt został przesłany image musi mieć tą samą nazwę (pełną) co repozytorium, czyli `<nazwa_konta>/<nazwa_repo>`.
Należy zbudować nowy i nadać mu odpowiednią nazwę lub zmienić nazwę komendą:
`docker tag <stara_nazwa>:<stary_tag> <nowa_nazwa>`  
Teraz wykonaj:
`docker push <nazwa_konta>/<nazwa_repo>`

### Volumes

Są 2 rodzaje trwałej pamięci: Volumes i Bind Mounts. Są dwa rodzaje Volumes: Anonimowe i named.
Aby utworzyć anonimowe volume, do pliku Dockerfile dopisz:
`VOLUME ["/<working_directory_path>/<path_to_persistant_directory>"]` np:
`VOLUME ["/app/feedback"]`
Anonimowe volume jest usuwane razem z kontenerem, więc nie można używać go jako persistant data storage. Do tego służy
Named Volume, które nie tworzy się w pliku Dockerfile tylko z pomocą flagi '-v' przy komendzie 'docker run':  
`docker run -p 3000:80 -d --rm --name <Dowolna_nazwa_dla_kontenera> -v <volume_name>:<volume_path> <nr_lub_name_of_image>`  
Aby usunąć anonimowe volume (bo może się nie usunąć automatycznie) użyj komendy:
`docker volume prune` lub `docker volume rm VOLUME_NAME`

Aby można było aktualizować kod na bieżąco, należy użyć Bind Mounts. Tworzy się je tak samo, jak named volume, ale
podaje
się ścieżkę do projektu (skrót: `$(pwd)`) i po dwukropku, ścieżkę do kodu w kontenerze.
`docker run -p 3000:80 -d --rm --name <Dowolna_nazwa_dla_kontenera> -v <volume_name>:<volume_path> -v $(pwd):<workdir_kontenera> <nr_lub_name_of_image>`  
Ale uwaga, w tej sytuacji cały kod w kontenerze zostanie nadpisany przez kod z komputera gospodarza (na lokalnym
kompie). W niektórych sytuacjach nie jest to zalecane. Gdy w pliku dockerfile wykonywana jest jakaś komenda tworząca
jakieś foldery, najczęściej jakieś biblioteki lub pakiety zależności należy te foldery umieścić w anonimowym volume,
dodając kolejny '-v', tym razem bez nazwy (jeśli nie ma dwukropka, nie ma nazwy dla volume) lub dodając anonimowe volume
w pliku Dockerfile.
`docker run -p 3000:80 -d --rm --name <Dowolna_nazwa_dla_kontenera> -v <volume_name>:<volume_path> -v $(pwd):<workdir_kontenera> -v /<workdir_kontenera>/<package_directory> <nr_lub_name_of_image>`

`  -v /app/data ` - anonymus volume
`  -v data:/app/data` - named volume
`  -v /path/to/code:/app/data` - bind mount