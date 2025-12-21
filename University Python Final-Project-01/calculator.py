def add(a, b):
    return a + b 

def sub(a, b):
    return a - b  

def mul(a, b):
    return a * b  

def div(a, b):
    if b == 0:
        return "Error"  # division by zero
    return a / b

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def remainder(a, b):
    return a % b


# The Program 

while True:
    print("\n### Calculator Menu ###\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Factorial\n6. Sum 1 to N\n7. Remainder\n8. Exit")

    choice = input("Choose option: ")

    match choice:
        case "1" | "2" | "3" | "4":
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))

            match choice:
                case "1":
                    print("Result:", add(a, b))
                case "2":
                    print("Result:", sub(a, b))
                case "3":
                    print("Result:", mul(a, b))
                case "4":
                    print("Result:", div(a, b))
        
        case "5":
            n = int(input("Enter number: "))
            print("Result:", factorial(n))

        case "6":
            n = int(input("Enter N: "))
            print("Sum:", sum_to_n(n))

        case "7":
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            print("Remainder:", remainder(a, b))

        case "8":
            print("Exiting...")
            break

        case _:
            print("Invalid option.")
