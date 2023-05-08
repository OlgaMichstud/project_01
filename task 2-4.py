#Задание 2-4

def remove_exclamation_marks(s):
  s = s.replace('!', '')
  return s
def remove_last_em(s):
  if s[len(s)-1] == '!':
    s = s[0:-1]
  return s
s = input()
s1 = remove_last_em(s)
print("Убрать последний восклицательный знак:", s1)
s2 = remove_exclamation_marks(s)
print("Убрать все восклицательные знаки:", s2)