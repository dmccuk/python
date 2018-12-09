''' Dice game
between computer and
user'''

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Make a guess: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The Maximun possible is %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "error - value too high"
  else:
    print "Rolling..."
    sleep(2)
    print "The 1st roll is: %d" % first_roll
    sleep(1)
    print "The 2nd roll is: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "Total value is: %d" % total_roll
    sleep(1)
    if guess == total_roll:
      print "You Won!"
    else:
      print "You lost, try again."
  
roll_dice(6)
