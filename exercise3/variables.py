# Enter work hours
wh = input("Enter Hours: ")
# Enter hourly rate
hr = input("Enter Rate: ")
# overtime hours and rate 
oh = float(wh)
pr = float(hr)
# print(oh, pr)
# Calculate gross check with overtime, convert strings into numbers by using float
if oh > 40 : 
    # print("Overtime")
    regular = oh * pr
    overtimerate = (oh - 40.0) * (pr * 0.5 )
    # print(regular,overtimerate)
    check = regular + overtimerate
else: 
    # print("Regular")
    check = oh * pr
# Total gross pay
print("Pay:", check)