math = float(input("Enter your Math score: "))
english = float(input("Enter your English score: "))
programming = float(input("Enter your Programming score: "))

ave = round(math + english + programming) / 3

if ave <= 100 and ave > 75:
    print(f"Your average is: {round(ave, 2)}")
    print("Great!!! Keep it up...")
elif ave <= 75 and ave > 50:
    print(f"Your average is: {round(ave, 2)}")
    print("GOOD!!! Keep it up...")
elif ave <= 50 and ave > 25:
    print(f"Your average is: {round(ave, 2)}")
    print("Not Bad!!! Keep working hard...")
else:
    print(f"Your average is: {round(ave, 2)}")
    print("Try more!!!")