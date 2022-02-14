# introduction to list 

 
# grocery_list = ["apples", "pasta", "milk"]
# print(grocery_list)

# integer_list = [60, 93, 723]
# float_list = [60.0, 93.5, 72.3]
# boolean_list = [True, False]

# mixed_list = [60, 723, 'rollin six owe']

# print(integer_list)
# print(float_list)
# print(boolean_list)
# print(mixed_list)

item_one = 'apples'
item_two = 'pasta'
item_three = 'milk'

grocery_list_two = [item_one, item_two, item_three]
print(grocery_list_two)

# creating a list with no elements

empty_list = []
print(empty_list)
print(type(empty_list))

# integer list modification 3

integer_list = [1,2,3,4,5,6]
print(integer_list)

length = len(integer_list)
print(length)

# adding element to list
integer_list.append(7)
print(len(integer_list))
print(integer_list)


# remove element from list
integer_list.remove(5)
print(len(integer_list))
print(integer_list)