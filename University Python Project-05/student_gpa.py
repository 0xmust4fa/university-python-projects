def stu():
    print("Here I will say your GPA from 3 cores:")
    name = input("Please enter your name: ")
    num1 = float(input("Enter your score: "))
    num2 = float(input("Enter your score: "))
    num3 = float(input("Enter your score: "))

    res = round((num1 + num2 + num3) / 3, 0)
    print(f"Dear {name}, your score average is: {res}")
stu()