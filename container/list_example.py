#list
#is a class that acts as a container of data items
#a series of items ( can be diferent type )
#any item can be appended into or removed from a list

#important method
# .append( appending_item )
# .remove( removing item )
# .sort( )
# clear( )
# .index( finding_item )

#some builtin functions that can apply to a list
#len()
#sum()
#min()
#max()
#sorted()

#useful syntax structures that can apply to a list
#loop throug each element           -> for i in any_list :
#check if an item exist in a list c    -> if an_item in list :
#access an item by its index position -> any_list[ item_index ]

'''below lines here are list container class usage examples'''
#create a list with 5 items of different types
my_list = [4, 2, 'pokemon', 5.23, False] 
print('#1', my_list)

#access and show the 3rd item
#note : an index is 0-based, so 2 is the index of 3rd item
third_item = my_list[2] 
print('#2', third_item)

#append some more items
for i in range(3) :
    my_list.append(i)
print('#3', my_list)

#remove an item at the back
my_list.remove(False)
print('#4', my_list)

#remove items that is not integer type
for each_item in my_list :
    if type(each_item) is not int :
        my_list.remove(each_item)
print('#5', my_list)

#from 0 to 9 check whether each is in the list or not
for i in range(10) :
    if i in my_list :
        print('#6', i, 'is in my_list')
    else :
        print('#6', i, 'is not in my_list')

#sort the list
my_list.sort()
print('#7', my_list)

#find its summation, max, min values
print('#8', 'summation :', sum(my_list))
print('#9', 'min value :', min(my_list))
print('#10', 'max value :', max(my_list))

#clear it
my_list.clear()
print('#11', my_list)
