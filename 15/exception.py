# try:
#     file = open(r"/path/to/file/file.txt", "r")
# except EOFError:
#     print("file not found")

# f = open(r"/path/to/file/file.txt", "r")

# print(type(open(r"/path/to/file/file.txt", "r")))

# file = None
# try:
#     file = open(r"/path/to/file/file.txt", "r")
# except:
#     print("input / output error")
# finally:
#     print("Closing file")
#     if type(file) == ''
#     file.close()
    

file = None
try:
    file = open(r"newFile.txt", "r")
except EOFError:
    print("input / output error")
finally:
    file.close()
    print("Closing file")