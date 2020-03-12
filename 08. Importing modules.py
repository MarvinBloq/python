__author__ = 'Liquid'
# Importing whole module
# import module01 as m01
courses = ['Math', 'History', 'Art', 'CompSci', 'PhysEd', 'Chem']
# index = m01.findIndex(courses, 'Art')
# print(index)

# Importing separate function
# from module01 import findIndex as fi
# courses = ['Math', 'History', 'Art', 'CompSci']
# index = fi(courses, 'Math')
# print(index)

# Using standard libraries and modules
import random
randomCourse = random.choice(courses)
print(randomCourse)

import math
rads = math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

import os
print(os.getcwd())

import antigravity
