#-----------------ITERAÇÃO-----------------#

#USANDO LOOP FOR

fav_songs = ["Deep End", "Armies", 
"Highest In The Room"]

for each_song in fav_songs:
    print(each_song)

#USANDO LOOP WHILE

count = 0
while count < len(fav_songs):
    print(fav_songs[count])
    count = count +1

#VERIFICANDO UMA LISTA PARA OBTER OUTRA LISTA

fav_songs_two = ["The Plan", "River Of Jordan",
 "Tell the World", fav_songs]

for each_song in fav_songs_two:
    if isinstance(each_song, list):
        for song in each_song:
            #ITERANDO LISTA DENTRO DE LISTA
            print(song)
    else:
        print(each_song)

#USANDO O BUILT-IN ITER()

fav_songs_three = ["The Box", "Too Cold", "Sweet Victory"]

hit = iter(fav_songs_three)

hit.__next__()
