people = 50
cars = 30
trucks = 30

# if there are more cars than people, print the line below
if cars > people:
    print(">>>> first if:", cars, people) # DEBUGGING
    print("We should take the cars.")

# if there are not more cars than people but less, print the line below
elif cars < people:
    print(">>>> first elif:", cars, people) # DEBUGGING
    print("We should not take the cars.")

# if there are neither more nor less cars than people, print the line below
else:
    print(">>>> first else:", cars, people) # DEBUGGING
    print("We can't decide.")

####

# if there are more trucks than cars, print line below
if trucks > cars:
    print(">>>> second if:", trucks, cars) # DEBUGGING
    print("That's too many trucks.")

# if there are not more trucks than cars but less, print line below
elif trucks < cars:
    print(">>>> second elif:", trucks, cars) # DEBUGGING
    print("Maybe we could take the trucks.")

# if there are neither more nor less trucks than cars, print line below
else:
    print(">>>> second else:", trucks, cars) # DEBUGGING
    print("We still can't decide.")


####

# if there are more people than trucks, print line below
if people > trucks:
    print(">>>> third if:", people, trucks) # DEBUGGING
    print("Alright, let's just take the trucks.")

# if there are not more people than trucks, print line below
else:
    print(">>>> third else:", people, trucks) # DEBUGGING
    print("Fine, let's stay home then.")
