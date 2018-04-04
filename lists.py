my_list1 = [1,2,3,4]
print(my_list1)
print(type(my_list1))

list1 = ["Dennis",3.4,5.6,"Lists are Flexible",14]
print(list1)


list2 = [1,2,3,4,5,6,7,8,9,0,0,0,5]
print(len(list2))

my_list3 = list("Hello World!")
print(my_list3)


my_list = [1,2,3,4,5,"a","b",3.14]
print(my_list)
print(my_list[0])
print(my_list[2])
print(my_list[5])
print(my_list[-1]) # print last entry in the list
print(len(my_list)) # print length of list - integer
print(my_list[len(my_list)-1]) # print last character

print(my_list[2:]) # get everything after the 2nd in the list
print(my_list[:4]) # get everything up to 4th in the list
print(my_list[::2]) # get every 2nd item from the list
print(my_list[::-1]) # Reverse list


list1 = [1,2,3]
list2 = [4,5,6]
print(list1 + list2) # concatinate both lists
print(list2 + list1) # concatinate both lists
new_list = list1 + list2
print(new_list)

print(list1 * 3) # you get 3 of the last list

list1 *= 3
print(list1) # list1 now = 3 of the same

my_list[0] = 8
print(my_list)


another_list = [1,2,3,4,5]
print(another_list)
another_list[:2] =  [10,20]
print(another_list)


# METHODS
# append to a list

list4 = [1,2,3,4,5]
print(list4)
list4.append(6)
print(list4)
list4.append("python")
print(list4)

# remove elements from list
list4.pop() #last added element
print(list4)

list4.pop(1) # remove the second element
print(list4)

# using DEL for lists:

list5 = [1,2,3,4,5]
del list5 # delete the list completely

list5 = [1,2,3,4,5]
del list5[3] # delete only the 3rd (4th) element
print(list5)

del list5[1:3] # deletes elements 1-3
print(list5)

# SORT Methos

numbers = [23,456,54,232,1,2,3,67,88,7,654]
print(numbers)
numbers.sort() # sorts list into numbr order - low to high
print(numbers)
numbers.sort(reverse = True) # reverse the order
print(numbers)

cars = ["bmw","merc","audi","bugatti"]
print(cars)
cars.sort()
print(cars)
cars.sort(reverse = True)
print(cars)

# Nested lists
l = [1,2,3, [4,5], [6,7,8]]
print(l)
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

new_list = [list1,list2,list3]
print(new_list)

print(new_list[1]) # grab the second list (list2)
print(new_list[1][1]) # grab the second list and second number



