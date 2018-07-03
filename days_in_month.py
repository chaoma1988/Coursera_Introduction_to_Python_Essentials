'''
Problem 1: Computing the number of days in a month
First, you will write a function called days_in_month
that takes two integers: a year and a month. The function should return the number of days in that month.
You may assume that both inputs are valid (in other words, you do not need to write any code to check whether or not they are reasonable,
you can just assume that the month input is a number between 1 and 12 and the year input is a
number between datetime.MINYEAR and datetime.MAXYEAR).
'''

import datetime

def days_in_month(year,month):
    if month == 12:

        date1 = datetime.date(year,month,1)
        date2 = datetime.date(year+1,1,1)

        delta = date2 - date1

        return delta.days

    else:

        date1 = datetime.date(year,month,1)
        date2 = datetime.date(year,month+1,1)

        delta = date2 - date1

        return delta.days
