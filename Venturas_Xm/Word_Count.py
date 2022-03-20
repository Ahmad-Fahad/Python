def WordCount(strg):
  count = 0
  for i in strg:
    if i == ' ':
      count = count+1
  word_n = count+1
  return word_n


print(WordCount(input()))