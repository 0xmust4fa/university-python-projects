print("This program takes two int numbers and says all numbers between them in a list and prints how many numbers there are.")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
num_bet = list(range(a,b))
even_num = [i for i in range(a,b) if i % 2 == 0]
print(f"Even Numbers between {a}, and {b}: {even_num}")
print(f"There are {len(num_bet)} numbers between {a} and {b}")