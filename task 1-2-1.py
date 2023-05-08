#Задание 1-2 со списком

import random
import datetime
import time
from datetime import timedelta
my_favorite_songs = [
    ['Waste a Moment', '3.03'],
    ['New Salvation', '4.02'],
    ['Staying\' Alive', '3.40'],
    ['Out of Touch', '3.03'],
    ['A Sorta Fairytale', '5.28'],
    ['Easy', '4.15'],
    ['Beautiful Day', '4.04'],
    ['Nowhere to Run', '2.58'],
    ['In This World', '4.02'],
]
arr = random.choices(my_favorite_songs, k=3)
song1 = time.strptime(arr[0][1], "%M.%S")
song1_duration = timedelta(minutes=song1.tm_min, seconds = song1.tm_sec)
song2 = time.strptime(arr[1][1], "%M.%S") 
song2_duration = timedelta(minutes=song2.tm_min, seconds = song2.tm_sec)
song3 = time.strptime(arr[2][1], "%M.%S")
song3_duration = timedelta(minutes=song3.tm_min, seconds = song3.tm_sec)
print ('Три песни звучат ', song1_duration + song2_duration + song3_duration, ' минут')