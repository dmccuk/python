def anti_vowel(text):
  for i in "aeiouAEIOU":
    text = text.replace(i,"")
  return text
