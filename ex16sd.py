from sys import argv
script, filename = argv

print(f"We're going to read {filename}")
print("Press RETURN to continue")
input("...")

print("Opening the file...")
file = open(filename)

print("Printing the file...")
print(file.read())
print("Closing the file...")
file.close()