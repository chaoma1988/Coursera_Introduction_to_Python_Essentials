'''
Problem 4: Calculating a person's age in days
Finally, you will write a function called
age_in_days that takes three integers as input: the year, month, and day of a persons birthday.
The function should return that person's age in days as of today.
The function should return 0 if the input date is invalid (remember you have a function to check that!).
The function should also return 0 if the input date is in the future.
Remember that you already have a function that returns the number of days between two dates
that you wrote in Part 3. Which two dates could you pass to that function to solve this problem?
'''

import datetime
from is_valid_date import is_valid_date
from days_between import days_between


def age_in_days(year,month,day):


    today = datetime.date.today()
    dob = datetime.date(year,month,day)

    if (is_valid_date(year,month,day)) and (today >= dob):
        days = days_between(year,month,day,today.year,today.month,today.day)
        return days
    else:
        return 0


year = int(input('Input the year of your date of birth : '))
month = int(input('Input the month of your date of birth: '))
day = int(input('Input the date of your date of birth: '))

print(age_in_days(year,month,day))