# setting a variable (name) for a number
types_of_people = 10
# setting a variable as a formatted string which includes another variable
x = f"There are {types_of_people} types of people."

#setting some more variables as strings
binary = "binary"
do_not = "don't"
# setting a variable as a formatted string with two variables in a string
y = f"Those who know {binary} and those who {do_not}."

# printing variables
print(x)
print(y)

# printing formatted strings which include variables
print(f"I said: {x}")
print(f"I also said: '{y}'")

# setting a variable as a False statement
hilarious = False
# setting a variable as a string
joke_evaluation = "Isn't that joke so funny?! {}"

# printing a variable with a different kind of formatting
print(joke_evaluation.format(hilarious))

# setting two variables as strings
w = "This is the left side of..."
e = "a string with a right side."

# adding up two variables that are strings
print(w + e)
