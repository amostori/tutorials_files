`docker build . ` - zbudowanie image  
`docker run -p 3000:80 <nr_image>` - uruchomienie image'u jako kontenera w trybie atached
`docker ps` - pokaz wszystkie kontenery pracujące
`docker ps -a` - pokaz wszystkie kontenery
`docker start <nazwa_kontenera>` - ponowne uruchomienie już istniejącego kontenera w trybie
detached  
`docker attacha <nazwa_kontenera>` - przejście w tryb attach-będą widoczne logi.
`docker run -it <nr_image>` - uruchamia container w trybie interaktywnym (-i) oraz z terminalem (-t)
`docker start -a -i <nazwa_imageu>` - restartuje container w trybie attached i interaktywnym. 