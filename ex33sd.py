
def wloop(i, var, j, numbers):
    while i < var:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + j
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
        print("\n")



    print("The numbers: ")

    for num in numbers:
        print(num)

wloop(0, 20, 2, [])


########################################################


i = 0
numbers = []

varial = 6

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    print("\n")

    wloop(0, 10, 1, [])



print("The numbers: ")

for num in numbers:
    print(num)


########################################################


for i in range(0 < 6):
    print(">>>> for loop START")
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    print("\n")



print("The numbers: ")

for num in numbers:
    print(num)
