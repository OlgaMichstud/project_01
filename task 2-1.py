#Задание 2-1

def maximum(arr):
  max = arr[0]
  for i in arr:
    if i > max:
      max = i
  return max

def minimum(arr):
  min = arr[0]
  for i in arr:
    if i < min:
      min = i
  return min

arr = [4,6,2,1,9,63,-134,566]
print('max = ', maximum(arr))
print('min = ', minimum(arr))