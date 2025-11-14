# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# list ar epart of the collection family in Python
# Creatiing list
my_list = [1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]
print(len(my_list)) # 5
print(type(my_list)) # <class 'list'>
print(my_list[0]) # 1
print(my_list[1:4]) # [2, 3, 4]
print(my_list[1:]) # [2, 3, 4, 5]
print(my_list[:-1]) 
# Reverse the list
print(my_list[::-1]) # [5, 4, 3, 2, 1]
# Modifying a list
my_list.append(6)
print(my_list)
# add 7 and 8 to the end of the list
my_list.extend([7, 8])
print(my_list)
# remove the last item
my_list.pop()
print(my_list)
# Remove the item at index 2
my_list.pop(2)
print(my_list)
# sort the list in ascending order
my_list.sort()
print(my_list)
# reverse the list
my_list.reverse()
print(my_list)
# .remover to remove a specific value
my_list.remove(4)
print(my_list)
# remove the last item using negative inde

#add 50 more to th end of the list
new_list = list(range(12 , 120))
print(new_list)
my_list.append(new_list)
print(my_list)
# print every 3rd number
print(my_list[::3])
# print every 10th number
print(my_list[::10])
# remove every 3rd element
del (my_list[::3])
print(len(my_list))
print(my_list)


# list functions
# .append() - adds an item to the end of the list
# .extend() - adds multiple items to the end of the list
# .pop() - removes and returns an iteam at a given index
#   (default is the last item)
# .remove() - removes the first occurence of a specific value
# .sort() - sorts the list in ascending order
# .reverse() - reverses the order of the list
#why is a list more important than a variable?
# a list can hold multipule valuse,
# while a variable can only hold one value at a time
cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
print(cakes)
#access the fist term
print(cakes[0]) #chocolate
#access the last item
print(cakes[-1])
# want to chocolate cake instead of vanilla
cakes[0] = 'strawberry'
print(cakes)
# add a new cake to the end of the list
cakes.append('lemmon')
print(cakes)
cakes[1] = 'chocolate'
print(cakes)
# insert a new cake at index 2
cakes.insert(2, 'funfetti')
print(cakes)







# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# # Practice Problems:

# # Create a list with 5 of your favorite foods.
fav_food_list = ['chips', 'tea', 'soup', 'bread', 'cake']
# # Print the second and last item.
print(fav_food_list[1])
print(fav_food_list[4])
# # Add a new item using .append().
fav_food_list.append('mango')
print(fav_food_list)
# # Remove the first item using .pop(0).
fav_food_list.pop(0)
print(fav_food_list)
# # Reverse your list using .reverse().
fav_food_list.reverse()
print(fav_food_list)

# sets = {1, 2, 3}
# sets are unordered colections of unique items
# sets do not support indexing or slicing
# sets are mutable, meaning you can add or remove items
# sets are created using curly braces{}
# do sets allow duplicate items? No, sets do not allow duplicate itema
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))
# add and iteam to the list
my_set.add(6)
print(my_set)
#remove an item
my_set.remove(3)
print(my_set)
#check is an istem is true
print(4 in my_set)
print(3 in my_set)


#Tuples are ordered collections of items
#tuples are immutable, meaning you cannot modify them after creation
#tuples are created using ()
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1:4])




# # Create a list of 3 lists (matrix), and access the middle element.