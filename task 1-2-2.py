#Задание 1-2 со словарем

import random
import datetime
import time
from datetime import timedelta
my_favorite_songs_dict = {
    'Waste a Moment': '3.03',
    'New Salvation': '4.02',
    'Staying\' Alive': '3.40',
    'Out of Touch': '3.03',
    'A Sorta Fairytale': '5.28',
    'Easy': '4.15',
    'Beautiful Day': '4.04',
    'Nowhere to Run': '2.58',
    'In This World': '4.02',
}
arr = random.choices(list(my_favorite_songs_dict.values()), k=3)
duration = timedelta()
for i in arr:
  song_duration = time.strptime(i, "%M.%S")
  duration += timedelta(minutes = song_duration.tm_min, seconds = song_duration.tm_sec)
print ('Три песни звучат ', duration, ' минут')