def purify(list):
  even = []
  for i in list:
    if i % 2 == 0:
      even.append(i)
  return even

print purify([1,2,3,4,5])
