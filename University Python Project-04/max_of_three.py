a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b and a > c:
    print(f"{a} is the biggest")
elif b > a and b > c:
    print(f"{b} is the biggest")
else:
    print(f"{c} is the biggest")