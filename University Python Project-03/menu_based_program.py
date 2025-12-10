print("Please choose one option from following: \n1. Say hello\n2. Show numbers 0 to 10\n3. Mean of 4 numbers\n4. Say Goodbye ")
a = int(input("Option: "))
if a == 1:
    print("Hello!")
elif a == 2:
    print(list(range(0,11)))
elif a == 3:
    print("Enter 4 numbers to calculate their average:")
    num_1 = int(input("Enter number one: "))
    num_2 = int(input("Enter number two: "))
    num_3 = int(input("Enter number three: "))
    num_4 = int(input("Enter number four: "))
    res = (num_1 + num_2 + num_3 + num_4) / 4
    print(res)
elif a == 4:
    print("Good Bye!")
else:
    print("Incorrect input!")