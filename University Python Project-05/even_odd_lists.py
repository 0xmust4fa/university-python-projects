def even_odd_count():
    number = int(input("Please enter a number: "))

    odd = list(range(1,number,2))
    even = list(range(0,number,2))
    print(f"Odd numbers are: {odd}")
    print(f"Even numbers are: {even}")

even_odd_count()