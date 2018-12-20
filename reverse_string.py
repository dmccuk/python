# this doesn't use revers or ::-1

def reverse(text):
  str = ""
  for i in text: 
    str = i + str
  return str
