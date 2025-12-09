print("For participating in this competition please give us your /City/ and /age/. ")
city = input("Enter your city: ")
city = city.lower()
age = int(input("Enter your age: "))
if city == "kabul" and age < 30:
    print("Bravo! Welcome to the competition.")
else:
    print("Sorry! Please change your city or age.")