# zeller_congruence.py
# 10/28/17

# Zeller's congruence is an algorithm
# developed by Christian Zeller to
# calculate the day of the week.
name= input("Enter your name: ")
year = int(input('Enter year(e.g. 2015): '))
month = int(input('Enter month(1-12): '))
day = int(input('Enter day of the month(1-31): '))

# If January or February is entered you must add
# 12 to the month and minus 1 from the year. This
# puts you in month 13 or 14 of previous year.
if month == 1:
    month = month + 12
    year = year - 1
    
elif month == 2:
    month = month + 12
    year = year - 1
    
print("{} was born on {}th".format(name,day))
century = (year // 100)
century_year = (year % 100)

# Day of the week formula
dotw = (day + ((26 * (month + 1)) // (10)) + century_year + ((century_year) // \
    (4)) + ((century) // (4)) + (5 * century)) % 7

if dotw == 0:
    print('Day of the week is Saturday')
elif dotw == 1:
    print('Day of the week is Sunday')
elif dotw == 2:
    print('Day of the week is Monday')
elif dotw == 3:
    print('Day of the week is Tuesday')
elif dotw == 4:
    print('Day of the week is Wednesday')
elif dotw == 5:
    print('Day of the week is Thursday')
elif dotw == 6:
    print('Day of the week is Friday')

    
