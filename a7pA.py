# Write a program that generates the entire calendar for one year.  The program
# must get two values from the user to do this.  First, you will need the year
# in order to check for leap years.  The year must be positive; you can assume
# it will be an integer.  Second, you will need the day of the week for January
# 1st of that year.  The user will enter 0 for Sunday, 1 for Monday, …, or 6 for
# Saturday.  Any other values are errors; you can assume it will be an integer.
# With these two values, your program will print out the calendar for that year,
# from January to December.
#
# The calendar must be printed in the form below.  In this example, January
# starts on a Friday (day 5).  January ends on Sunday as a result, and so
# February will start on a Monday.
#
# January
#                  1  2
#   3  4  5  6  7  8  9
#  10 11 12 13 14 15 16
#  17 18 19 20 21 22 23
#  24 25 26 27 28 29 30
#  31
#
# February
#      1  2  3  4  5  6
#   7  8  9 10 11 12 13
# ...
#
# You are required to create 4 functions to solve this problem:
#
# 1) A function named get_year(), with no parameters, that gets the year from
#    the user and returns it. The function must validate the input, and print an
#    error and exit if it's not valid.
# 2) A function named get_starting_day(), with no parameters, that gets the day
#    of the week for January 1st from the user and returns it.  The function
#    must validate the input, and print an error and exit if it's not valid.
# 3) A function named is_leap_year() that takes a single parameter (the year)
#    and returns True if it's a leap year or False if it's not a leap year.
#    Note that it's slightly more complicated than only checking if the year is
#    divisible by 4 (but not much, see the linked Wikipedia article above).
# 4) A function named print_month() that takes three parameters: the name of the
#    month, the number of days in the month, and the day of the week (0-6) that
#    the month starts on.  The function then prints out the calendar for that
#    one month only.  For instance, print_month("January", 31, 5) would print
#    the calendar for January (only) from the above example.
#
# Your top-level program will call get_year() and get_starting_day() to get the
# two needed inputs, then call is_leap_year() to determine how many days will be
# in February, and finally call print_month() 12 times - once for each month.
# The simplest approach for the last part is to have two lists, one with the
# names of the months in order and another with the number of days in each month
# in order.  Then, you can loop over the month list with enumerate() and call
# print_month() once for each month in the list with the correct number of days.
#
# This is a complex program with many pieces and moving parts.  There are
# several ways to approach it, but most importantly take some time before you
# dive into coding to be sure that you understand and have thought through the
# problem.  Also, it will be critical that you test your program early and
# often.  Don't write more than a few lines of code without stopping to test it
# and convince yourself that what you are doing makes sense.
#
# If you aren't sure how to get started, then here is a suggested way to proceed:
#
# 1) Write the get_year() function first, then call it from your main program to
#    make sure it's working as needed (erroring out if the year is not positive,
#    etc).
# 2) Write the get_starting_day() function next, then call it from your main
#    program to make sure it's also working as needed.
# 3) Write the is_leap_year() function, then call it from your main program to
#    make sure it's accurately detecting if the given year is a leap year or not
#    (for example, 1900 is not a leap year, but 2000 is; see the article above).
#    It would make sense to test this in your main program by getting the return
#    value and simply printing it out to start.
# 4) Now, move to the print_month() function.  This is the hardest part of the
#    assignment, so break it down into smaller chunks that you can write and
#    test.  In your main program, just call the function once for January to
#    start testing.
#    a) Start by printing out just the month name (given as a parameter).
#    b) Then, print out the correct number of days in the month, but don't worry
#       about spacing, the starting day, etc.  Recall that print() takes an
#       optional argument end that can suppress printing the automatic new
#       lines, e.g.: print("1", end=""), will print "1" without moving to the
#       next line afterwards.
#    c) Next, find a way to print out a new line after each Saturday.
#    d) Then, focus on getting the days to line up (think about single digit vs
#       double digit numbers).
#    e) Now, add some code to deal with the "blank" days at the beginning of
#       each month.  For example, if January starts on a Tuesday then you'll
#       have to print two "blank" days to start the first week.
#    f) Finally, you'll have to return a value from the function - the next day
#       of the week after the month ends.  You'll need that when you call
#       print_month() for the next month.  For example, if March ends on a
#       Thursday then April has to start on Friday.
# 5) Once you are comfortable that print_month() works for January, then add a
#    loop to call the function 12 times.
#    a) Don't forget to adjust the number of days in February if it's a leap
#       year.
#    b) Also, be sure that print_month() is handling newlines at the end of each
#       month correctly.  There should always be a single blank line after one
#       month before the next one starts.
#
# Your input and output messages must conform to the following examples:
#
# Enter the year: 0
# Year must be positive.
#
# Enter the year: 2000
# Enter the day of the week for January 1st (0 for Sunday, 1 for Monday, ...): 7
# Day must be 0-6.
#
# Enter the year: 2000
# Enter the day of the week for January 1st (0 for Sunday, 1 for Monday, ...): 5
# January
#                  1  2
#   3  4  5  6  7  8  9
#  10 11 12 13 14 15 16
#  17 18 19 20 21 22 23
#  24 25 26 27 28 29 30
#  31
#
# February
#      1  2  3  4  5  6
#   7  8  9 10 11 12 13
#  14 15 16 17 18 19 20
#  21 22 23 24 25 26 27
#  28 29
#
# March
#         1  2  3  4  5
#   6  7  8  9 10 11 12
#  13 14 15 16 17 18 19
#  20 21 22 23 24 25 26
#  27 28 29 30 31
#
# April
#                  1  2
#   3  4  5  6  7  8  9
#  10 11 12 13 14 15 16
#  17 18 19 20 21 22 23
#  24 25 26 27 28 29 30
#
# May
#   1  2  3  4  5  6  7
#   8  9 10 11 12 13 14
#  15 16 17 18 19 20 21
#  22 23 24 25 26 27 28
#  29 30 31
#
# June
#            1  2  3  4
#   5  6  7  8  9 10 11
#  12 13 14 15 16 17 18
#  19 20 21 22 23 24 25
#  26 27 28 29 30
#
# July
#                  1  2
#   3  4  5  6  7  8  9
#  10 11 12 13 14 15 16
#  17 18 19 20 21 22 23
#  24 25 26 27 28 29 30
#  31
#
# August
#      1  2  3  4  5  6
#   7  8  9 10 11 12 13
#  14 15 16 17 18 19 20
#  21 22 23 24 25 26 27
#  28 29 30 31
#
# September
#               1  2  3
#   4  5  6  7  8  9 10
#  11 12 13 14 15 16 17
#  18 19 20 21 22 23 24
#  25 26 27 28 29 30
#
# October
#                     1
#   2  3  4  5  6  7  8
#   9 10 11 12 13 14 15
#  16 17 18 19 20 21 22
#  23 24 25 26 27 28 29
#  30 31
#
# November
#         1  2  3  4  5
#   6  7  8  9 10 11 12
#  13 14 15 16 17 18 19
#  20 21 22 23 24 25 26
#  27 28 29 30
#
# December
#               1  2  3
#   4  5  6  7  8  9 10
#  11 12 13 14 15 16 17
#  18 19 20 21 22 23 24
#  25 26 27 28 29 30 31
#
# Note the order of inputs, capitalization of messages, spacing, etc.


import sys

def get_year():
    year = int(input("Enter the year: "))
    if year < 1:
        print("Year must be positive.")
        sys.exit()
    return year

def get_starting_day():
    day = int(input("Enter the day of the week for January 1st (0 for Sunday, 1 for Monday, ...): "))
    if day > 6 or day < 0:
        print("Day must be 0-6.")
        sys.exit()
    return day

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False 
    else:
        return True

def print_month(month, num_days, week_day_num):
    print(month)
    day = 1
    if week_day_num == 0:
        pass
    else:
        print("   " * (week_day_num), end="")
    while day <= (7 - week_day_num):
        print("",day, end=" ")
        day += 1
    print("\n", end="")
    start_day = day
    if week_day_num != 6:
        while start_day <= day < 10:
            print("",day, end=" ")
            day += 1
    else:
        while start_day <= day < 9:
            print("",day, end=" ")
            day += 1
    while 10 <= day <= start_day + 6:
        print(day, end=" ")
        day += 1
    print("\n", end="")
    start_day = day
    if week_day_num == 6:
            print(" ", end="")
    while start_day <= day <= start_day + 6:
        print(day, end=" ")
        day += 1
    print("\n", end="")
    start_day = day
    while start_day <= day <= start_day + 6:
        print(day, end=" ")
        day += 1
    print("\n", end="")
    start_day = day
    while start_day <= day <= start_day + 6 and day <= num_days:
        print(day, end=" ")
        day += 1
    print("\n", end="")
    while day <= num_days:
        print(day, end=" ")
        day += 1
    if week_day_num == 6 or week_day_num == 5:
        print("\n", end="")


year = get_year()
starting_day = get_starting_day()
leap = is_leap_year(year)

if leap == True:
    x = 29
else:
    x = 28
    
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 
days = [31, x, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for (month, day) in zip(months, days):
    print_month(month, day, starting_day)
    if day == 31:
        if starting_day >= 4:
            starting_day -= 4
        else:
            starting_day += 3
    if day == 30:
        if starting_day >= 5:
            starting_day -= 5
        else:
            starting_day += 2
    if day == 29:
        if starting_day == 6:
            starting_day -= 5
        else:
            starting_day += 1
    if day == 28:
        pass
    print("\n", end="")
