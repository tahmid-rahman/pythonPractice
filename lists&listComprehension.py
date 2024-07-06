list = ["banana", "apple", "date", "cherry", "jackfruit", "mango", "avocado", "orange", "pear" ]
#print(list[4])
print(list)
## Use a list comprehension to create a new list containing the lengths of each fruit.
list_length = [len(list) for list in list] #didn't understand the line of code.
print(list_length)

list.append("litchi") #adding item in last 
print(list)

#sort alphabetically
list1 = sorted(list)
print(list1)