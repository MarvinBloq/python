__author__ = 'Liquid'
import os
from datetime import datetime
# print(os.getcwd())
os.chdir('C:/Users/Liquid/Desktop')
# print(os.getcwd())
# print(os.listdir())

# Creating single or multiple directories
# os.mkdir('pyone')
# os.makedirs('pytwo/pytwoone')

# # Removing dirs
# os.rmdir('pyone')
# os.removedirs('pytwo/pytwoone')

# Rename file or folder
# os.rename('pyone', 'pydemo')

# Statistics on file
# modTime = os.stat('djinni.txt').st_mtime
# print(datetime.fromtimestamp(modTime))

# Walking through dirs and files
# for dirpath, dirnames, filenames in os.walk('C:/Users/Liquid/Desktop'):
#     print('Current path', dirpath)
#     print('Directories', dirnames)
#     print('Files', filenames)
#     print()

# Print basename and dirname of a path, separately and simultaneously
print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))

# Existing of file path
print(os.path.exists('/tmp/test.txt'))

# Isdir and isfile check
print('Is this a dir?', os.path.isdir('/tmp/test.txt'))
print('Is this a file?', os.path.isfile('/tmp/test.txt'))

# Splitting file extension of off root
print(os.path.splitext('/tmp/test.txt'))