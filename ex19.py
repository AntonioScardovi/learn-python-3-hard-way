def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)




def books(own, read):
    print(f"I own {own} books.")
    print(f"I read {read} of them.")
    print("I have to read more.")
    print("Time to buy more books! \n")

print("#1 - Giving numbers directly")
books(23, 5)


print("#2 - Using variables")
own_books = 21
read_books = 4
books(own_books, read_books)


print("#3 - Using math")
books(10 + 10, 3 + 3)


print("#4 - Using strings")
books("Twenty", "Six")


print("#5 - Using variables and math")
books(own_books + 5, read_books + 2)


print("#6 - Using input")
books_owned = input("How many books do you own? ")
books_read = input("How many books have you read? ")
books(int(books_owned), int(books_read))


print("#7 - Using input and math")
books(int(books_owned) + 1000, int(books_read) + 21)