'''
Problem 2: Checking if a date is valid
Next, you will write a function called is_valid_date
that takes three integers: a year, a month, and a day. The function
should return True if that date is valid and False otherwise.
This function should not assume that the inputs are valid. Rather, this function should check that
all three inputs combine to form a valid date, with a year between datetime.MINYEAR and datetime.MAXYEAR,
a month between 1 and 12, and a day between 1 and the number of days in the given month.
Notice that the function days_in_month
that you wrote for Part 1 will be useful here!
'''

import datetime
from days_in_month import days_in_month

def is_valid_date(year,month,day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    days = days_in_month(year,month)

    if (year>=datetime.MINYEAR) and (year<=datetime.MAXYEAR) and (month>=1) and (month<=12) and (day>=1) and (day<=days):
        return True
    else:
        return False

# Testing
# print(is_valid_date(1998,12,12))
