def string():
    text = input("Please enter your text: ")
    char = "a"
    char1 = "A"
    char_count1 = text.count(char)
    char_count2 = text.count(char1)
    print(f"The char 'a' appears in your text {char_count1} times!")
    print(f"The char 'A' appears in your text {char_count2} times!")
string()