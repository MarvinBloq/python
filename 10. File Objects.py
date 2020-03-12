# File objects
# Reading file: r, writing: w, reading and writing: r+
# f = open('list.txt', 'r')
# print(f.name)
# print(f.mode)
# f.close()

# Working with files using context manager
# with open('list.txt', 'w') as f:
    # fcontents = f.read()
    # print(fcontents)
    # Reading separate lines
    # fcontents = f.readlines()
    # print(fcontents)

    # Reading single line
    # fcontents = f.readline()
    # print(fcontents, end='')

    # Printing all content at once without reading and memory issues
    # for line in f:
    #     print(line, end='')

    # Specifying amount of characters, which will be read at a time and looping walk through file
    # sizeToRead = 6
    # fcontents = f.read(sizeToRead)
    # while len(fcontents) > 0:
    #     print(fcontents, end='*')
    #     fcontents = f.read(sizeToRead)

    # Printing the position
    # print(f.tell())

    # Creating a file and writing into it
    # with open('list2.txt', 'w') as f1:
    #     f1.write('Test')

# Opening the file, creating another and copying content from first file into second
with open('list2.txt', 'r') as rf:
    with open('list_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# Working in binary mode, e. g. with pictures
# with open('image.png', 'rb') as rf:
#     with open('image_copy.png', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

# Working with chunks of file
with open('image.png', 'rb') as rf:
    with open('image_copy.png', 'wb') as wf:
        chunk_size = 1024
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
