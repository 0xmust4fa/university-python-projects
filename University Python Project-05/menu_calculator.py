def sum():
    print("Sum operation!")
    a = float(input("Enter your number: "))
    b = float(input("Enter your number: "))
    res = a + b
    print(f"{a} + {b} = {res}")

def sub():
    print("Subtraction operation!")
    a = float(input("Enter your number: "))
    b = float(input("Enter your number: "))
    res = a - b
    print(f"{a} - {b} = {res}")

def multi():
    print("Multiplication operation!")
    a = float(input("Enter your number: "))
    b = float(input("Enter your number: "))
    res = a * b
    print(f"{a} * {b} = {res}")

def division():
    print("Division operation!")
    a = float(input("Enter your number: "))
    b = float(input("Enter your number: "))
    if b == 0:
        print("Error: Cannot divide by zero.")
    else:
        res = a / b
        print(f"{a} / {b} = {res}")
        
while True:
    print("Please choose one:\n1. Sum\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choose = int(input("Choice: "))
    match choose:
        case 1:
            sum()
        case 2:
            sub()
        case 3:
            multi()
        case 4:
            division()
        case 5:
            print("Exiting...")
            break
        case _:
            print("invalid input!")