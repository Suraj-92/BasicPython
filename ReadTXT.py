'''
Author: Suraj N Temkar
Date: 12/04/2021
Title: File IO (Write The File)
'''

f = open("C:\\Users\\DELL\\Desktop\\Python\\FileIO\File1.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending
f = open("C:\\Users\\DELL\\Desktop\\Python\\FileIO\File1.txt", "r")
print(f.read())


# Open the file "File1.txt" and overwrite the content
# f = open("C:\\Users\\DELL\\Desktop\\Python\\FileIO\File1.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the appending
# f = open("C:\\Users\\DELL\\Desktop\\Python\\FileIO\File1.txt", "r")
# print(f.read())


# Create a file called "myfile.txt":
# f = open("File2.txt", "x")

# Create a new file if it does not exist:
# f = open("myfile.txt", "w")

