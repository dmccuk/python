''' this program 
works out the maths for
Radius and Triangle area.
'''

print "the calculator is starting up."
shape = raw_input("Enter C for Circle and T for Tirangle: ")
shape = shape.lower()
if shape == 'c':
  radius = float(raw_input("Input the radius: "))
  area = 3.1459 * radius**2
  print area
elif shape == 't':
  base = float(raw_input("Input the Base of the Triangle: "))
  height = float(raw_input("Input the Height of the Triangle: "))
  area = 0.5 * base * height
  print area
else:
  print "You entered an invalid charater - Bye"

print "program is exiting!"
