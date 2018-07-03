'''
Problem 3: Computing the number of days between two dates
Now that we have a way to check if a given date is valid,
you will write a function called days_between that takes six integers (year1, month1, day1, year2, month2, day2)
and returns the number of days from an earlier date (year1-month1-day1) to a later date (year2-month2-day2).
If either date is invalid, the function should return 0. Notice that you already wrote a
function to determine if a date is valid or not! If the second date is earlier than the first date,
the function should also return 0.
'''
import datetime
from is_valid_date import is_valid_date

def days_between(year1,month1,day1,year2,month2,day2):
    if is_valid_date(year1,month1,day1):

        date1 = datetime.date(year1,month1,day1)
    else:
        return 0
    if is_valid_date(year2,month2,day2):

        date2 = datetime.date(year2,month2,day2)
    else:
        return 0

    delta = date2 - date1

    if delta.days <= 0:
        return 0
    else:
        return delta.days

# Testing

#print(days_between(1988,7,19,2018,7,3))
