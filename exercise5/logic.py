# phone_num = input('What is my phone number? ')

# is_atl_num = phone_num.startswith('404')
# phone_num = '404 337 0867'
# print(f"Your phone number has a Atlanta area code: {phone_num.startswith('404')}")

# Take in user input for the phone number
# if the phone number starts with 404:
#  print 'this phone number is local to Atl'
# otherwise 
#  print 'this phone is not local to the area'



# conditionals
phone_num = input('What is your phone number? ')

if phone_num.startswith('404'):
    print('This phone number is local to Atl')
else:
    print('This phone number is not local to the area')

# <if> <condition>:
#    <indent> then statement
# <else>: