# Python has two primitive loop commands:
# while loops and for loops 
# With the while loop we can execute a set of statements as long as a condition is true.
# With the break statement we can stop the loop even if the while condition is true:


# print('welecome to loops')

laundry_basket = ['jeans', 'sweater', 'tank top', 'dress shirt']
#      garment =


# for each garment in our laundry basket 
#    fold the garment
#    put away the garment
# clean clothes

# for garment in laundry_basket:
#     if garment == 'jeans':
#         print(f'check if the {garment} are dry')
#     print(f'fold the garment {garment}')
#     print(f'put away the garment {garment}' )
#     print()

# print('clean clothes')




# for loops for each item in a group of items 
# do something to that item

# for loops with the range function 
# for each time in a number of times
# do something 

# print(list(range(4)))

#for index in range(4):
#    print(index)



# correct_password = '1234'

# for i in range(3):
#     user_password = input ('enter your password:')

#     if user_password == correct_password:
#         print('welcome')
#         break
# while loop
# while a condition is true
#    keep going


correct_password = '1234'
user_password = ''

while user_password != correct_password:
    user_password = input('enter your password')

print('welcome')