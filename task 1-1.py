#Задание 1-1

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
print (my_favorite_songs[0 : my_favorite_songs.find(',')])
print (my_favorite_songs[my_favorite_songs.rfind(',')+2 : len(my_favorite_songs)])
print (my_favorite_songs[my_favorite_songs.find(',')+2:my_favorite_songs.find(',',my_favorite_songs.find(',')+1)])
print (my_favorite_songs[my_favorite_songs.rfind(',',0 ,my_favorite_songs.rfind(',')-1)+2:my_favorite_songs.rfind(',')])