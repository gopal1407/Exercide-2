

def is_leap_year(year):
    if ("year % 400 ==0") or ("year % 4 == 0") and ("year % 100 !=0"): 
        return True

    else:
        return False

year = input("Enter a year:")
if is_leap_year(year):
    print("{year} is leap year")
else:
    print("{year} is not leap year.") 
    
