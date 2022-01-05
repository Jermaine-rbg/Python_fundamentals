def computepay(hours, rate) :
    
    if hours > 40 :
       regular = hours * rate
       overtimerate = (hours - 40.0) * (rate * 0.5 )
       check = regular + overtimerate
    else: 
        check = hours * rate
    
    return check


wh = input("Enter Hours: ")
hr = input("Enter Rate: ")
oh = float(wh)
pr = float(hr)
check = computepay(oh, pr)

print("Pay:", check)