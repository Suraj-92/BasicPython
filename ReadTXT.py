'''
Author: Suraj N Temkar
Date: 12/04/2021
Title: File IO (Read The File)
'''

f = open("File1.txt", "r")
# print(f.read())   # Read File Contents

# print(f.read(5))    # Reads Only Parts of file

# print(f.readline())     # Reads Single Line
# print(f.readline())     


# Loop through the file line by line
for x in f:
  print(x)

f.close()       # Close File
