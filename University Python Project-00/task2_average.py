math = float(input('Please insert your math score: '))
english = float(input('Please insert your English score: '))
pro = float(input('Please insert your Programming score: '))

res = round((math + english + pro) / 3, 4)
print(f'Your average from three subject is: {res}')