`docker build . ` - zbudowanie image  
`docker run -p 3000:80 <nr_image>` - uruchomienie image'u jako kontenera w trybie atached
`docker ps` - pokaz wszystkie kontenery pracujące
`docker ps -a` - pokaz wszystkie kontenery
`docker start <nazwa_kontenera>` - ponowne uruchomienie już istniejącego kontenera w trybie
detached  
`docker attacha <nazwa_kontenera>` - przejście w tryb attach - będą widoczne logi.