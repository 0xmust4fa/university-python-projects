while True:
    print("PLease choose one option!\n1. Sum from 1 to N\n2. Print all even numbers to N\n3. Exit")
    choose = int(input("--> "))
    match choose:
        case 1:
            num = int(input("Enter a number: "))
            sum_num = []
            for i in range(1, num+1):
                sum_num.append(num)
                total = sum(sum_num)
            print(f"Sum from 1 to {num} is = {total}")
        case 2:
            num = int(input("Enter a number: "))
            for i in range(1, num+1):
                if i % 2 == 0:
                    print(i)
        case 3:
            print("Closing the program...")
            break
        case _:
            print("Invalid input!")
            
            