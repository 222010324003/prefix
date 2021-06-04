def prefix_words(prefix, words):
  lis = []
  for i in words:
    if i.startswith(prefix):
      lis.append(i)
  return lis
print(prefix_words("de", ["dog", "deal", "deer"]))

def prefix_words(prefix, words):
  lis = []
  for i in words:
    if i.startswith(prefix):
      lis.append(i)
  return lis
print(prefix_words("b" ,["banana", "binary", "carrot", "bit", "boar"]))
