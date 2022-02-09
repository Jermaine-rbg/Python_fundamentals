# assigning variables
# updating variables
# integers and floats

# class tonight:
# strings
# boolean 
# convert integers and floats

# strings

street_address = 'Atlanta ave'

# element of a string inside qoutation marks 
# sinlge or double qoutes 

print('Atlanta ave')
# direct print statement

print(street_address)

# string concatenation

zipcode = 30313 # integer
zipcode = '30313' # string
city = 'Atlanta'
state = 'Ga'

print(street_address, zipcode, city, state)

print('My address is', street_address)

print(f'My address is {street_address}')

# shows data type() 
print(type(zipcode))

# the F string is way more powerful
print(f'My address is {street_address}, {city}, {state}, {zipcode}.')

# reassigning variables
# replace is a method and all methods have () like print 
city = 'Birmingham'
print(state.replace('Ga', 'Al'))
print(street_address.replace('Atlanta ave', 'Alabama'))
print(zipcode.replace('30313', '35211'))

# Boolean - True or Fasle

print(f'My address is {street_address}, {city}, {state}, {zipcode}.')
print(street_address.endswith('90210'))
print(street_address.startswith('Atlanta'))

