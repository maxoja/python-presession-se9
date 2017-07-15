#list usage example

#create an empty list
my_list = list()

#add 1 2 5 4 into my_list
my_list.append(1)
my_list.append(2)
my_list.append(5)
my_list.append(4)
print(my_list)
print()

#remove 3 from my_list
my_list.remove(2)
print(my_list)
print()

#sort the list
my_list.sort()
print(my_list)
print()

#find the maximum value in the list
print('max :', max(my_list))
print('min :', min(my_list))
print()

#number of items in the list
print('there are', len(my_list), 'in this list')
print()
