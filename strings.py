
import socket

s = "welcome"
print(s)

#HOSTNAME = $hostname
#print(HOSTNAME)
name = "firstname lastname" * 3
print(name[4])
print(name[-2])

my_course = "learning python"
print(my_course[2:14])
print(my_course[:4])
print(my_course[11:])
print(my_course[:-1])
len(my_course)
print(len(my_course))

HOSTNAME = (socket.gethostname())
print(HOSTNAME[:-1])
print(len(HOSTNAME))

print(name + my_course + HOSTNAME)


s = "Welcome"

print(s)

l = "I'm learning python"
print(l)

name = "Dennis McCarthy"
print(name[1])
print(name[-1])

my_course = "Python is awesome!"
print(my_course) # All 
print(my_course[2:11]) #between
print(my_course[:5]) #upto 5
print(my_course[10:]) # index 10 onwards
print(my_course[:-1]) # index -1 onwards

a = "python programming language"
print(a[::2]) # skip 2 characters until the end
print(a[::3]) # skip 3 characters until the end
print(a[::-1]) # skip backward -1 characters until the end

s = "united kingdom rules by the Queen"
print(len(s))

a = "python"
b = "is"
c = "Really"
d = "Good"

print(a + b + c + d)

print("Money " * 3) # prints 3 times




