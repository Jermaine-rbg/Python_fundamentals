# Enter work hours
wh = input("Enter Hours: ")
# Enter hourly rate
hr = input("Enter Rate: ")
# Calculate gross check, convert strings into numbers by using float
check = float(wh) * float(hr)
# Total gross pay
print("Pay:", check)