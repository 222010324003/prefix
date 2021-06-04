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

def suffix_words(suffix,word):
  if word.endswith(suffix):
    print("Ends with {}").format(suffix)\
suffix="ly"
word="quickly"
