#Задание 2-3

def switch_it_up(number):
  match number:
    case '0':
      print('zero')
    case '1':
      print('one')
    case '2':
      print('two')
    case '3':
      print('three')
    case '4':
      print('four')
    case '5':
      print('five')
    case '6':
      print('six')
    case '7':
      print('seven')
    case '8':
      print('eight')
    case '9':
      print('nine')
    case _:
      print('none')
  return
switch_it_up(input())