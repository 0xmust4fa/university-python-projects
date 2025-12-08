name = input('Please enter your name: ')
last_name = input('Please enter your last-name: ')
age = int(input('Please enter your age: '))

# person_dict = {name: name + last_name + str(age)}
person_dict = {name: f'name: {name}, last-name: {last_name}, age: {str(age)}'}
print(f'Hello dear {name}, your age is {age} and next year you will be {age + 1}')