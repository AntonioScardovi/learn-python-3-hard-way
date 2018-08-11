# imports argument variable from libraries
from sys import argv
# assigns variable names
script, filename = argv

# open the file and return it as file object
txt = open(filename)

print(f"Here's your file {filename}:")
# prints the text of the file
print(txt.read())
txt.close()

# assign a variable to a file by input
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()


# print("Type the second filename")
# file2 = input("> ")

# txt2 = open(file2)

# print("Here's your second file:")
# print(txt2.read())