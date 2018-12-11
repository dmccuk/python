# Write your function below!
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count 

type_fizz = ["fizz", "yellow", "fizz" ]
winner = fizz_count(type_fizz)
print winner
