__author__ = 'Liquid'
import os
# Changing dir and checking location
os.chdir('C:/Users/Liquid/Desktop/untitled/mfiles')

# Listing files
for f in os.listdir():
    # Splitting file names from file extensions
    f_name, f_ext = os.path.splitext(f)
    # Splitting file names into parts
    f_title, f_course, f_num = f_name.split('-')
    # Stripping from whitespaces
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
    # Renaming files
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    os.rename(f, new_name)





