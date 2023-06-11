`docker build . ` - zbudowanie image  
`docker run -p 3000:80 <nr_image>` - uruchomienie image'u jako kontenera w trybie atached
`docker ps` - pokaz wszystkie kontenery pracujące
`docker ps -a` - pokaz wszystkie kontenery
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