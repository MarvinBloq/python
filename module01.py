__author__ = 'Liquid'
print('Imported module01...')
test = 'Test string'

# Find the index of a valie in sequence
def findIndex(toSearch, target):
    for i, value in enumerate(toSearch):
        if value == target:
            return i
    return -1