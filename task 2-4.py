#Задание 2-4

def remove_exclamation_marks(s):
  s = s.replace('!', '')
  return s
def remove_last_em(s):
  if s[len(s)-1] == '!':
    s = s[0:-1]
  return s
def remove_word_with_one_em(s):
  line = s.split()
  for i in line:
    if (i.find('!')==i.rfind('!')) and (i.find('!') !=-1):
      line.remove(i)
  s = str(line)
  return line
s = input()
s1 = remove_last_em(s)
print("Убрать последний восклицательный знак:", s1)
s2 = remove_exclamation_marks(s)
print("Убрать все восклицательные знаки:", s2)
s3 = remove_word_with_one_em(s)
print("Убрать все слова с 1 вослицательным знаком:", " ".join(s3))