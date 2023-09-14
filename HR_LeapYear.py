import calendar

def is_leap(year):
    leap = False
    
    # Write your logic here
    if calendar.isleap(year):
        print(True)
    else:
        print(False)

year = int(input())
print(is_leap(year))
