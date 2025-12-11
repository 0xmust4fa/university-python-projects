count = int(input("Enter you many numbers you enter: "))
numbers = []
for i in range(count):
    num = float(input("Enter your score: "))
    numbers.append(num)

total = sum(numbers)
average = total / count

print(f"Sum = {total}")
print(f"Average = {average}")

if average < 40:
    print("Performance: Low")
elif 40 <= average <= 80:
    print("Performance: Good")
else:
    print("Performance: Excellent")