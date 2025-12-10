people = ["hassan","ali","reza","mohammad","karim"]
name = input("Please enter your name: ")
name = name.lower()

if name in people:
    print(f"Hello {name.capitalize()}, Welcome to the program!")
else:
    people.append(name)
    print("Your name has been added to the list!")
    print(people)