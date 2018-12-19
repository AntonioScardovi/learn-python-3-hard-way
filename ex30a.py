people = 40
cars = 40
trucks = 40


if cars > people or trucks < cars:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("Trucks it is.")
