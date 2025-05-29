user_name : str = 'Paul Walker'
print(user_name)

#for loop
### syntax
# for <variable> in <iterable>:
# <code block>

###Loop through a string
for char in user_name:
   print(char , end = ' ,')
   print()

###loop through a string with index
for index in range(len(user_name)):
   print(user_name[index], end = ' ,')
   print()

names : list = ['paul', 'Walker', 'jOhN', 'dOe']
print(f'My name is {names[2].title()}')
for user in names:
   print(user.title())

##for loop to display numbers
for number in range(1, 11):
   print(number, end = ' ,')
   print()

for numbers in range (5, 11):
   print(f'2 times {number} is {2 * number}')
   print()
