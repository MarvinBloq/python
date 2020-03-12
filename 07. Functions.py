__author__ = 'Liquid'
# Creating empty function using pass keyword
# def helloFunction():
#     pass
# print(helloFunction())

# Functions return values
# def helloFunction():
#     return('Hello, folks')
# print(len(helloFunction()))

# Passing arguments to a function
# def funcOne(greeting = 'Hi', name = 'Second'):
#     return '{}, {} function.'.format(greeting, name)
# print(funcOne(name = 'Third'))

# Passing arguments and keyword arguments to a function
# def persInfo(*args, **kwargs):
#     print(args)
#     print(kwargs)
# name = ['John', 'Doe']
# info = {'age' : '25', 'sex' : 'male'}
# persInfo(*name, **info)

# Checking leap year and number of days in months
monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def leapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def daysInMonth(year, month):
    if not 1<= month <=12:
        return 'Invalid input'
    if month == 2 and leapYear(year):
        return 29
    return monthDays[month]
print(leapYear(2020))
print(daysInMonth(2017, 3))