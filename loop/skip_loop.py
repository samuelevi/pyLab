names : list = ['paul', 'walker', 'jOhN', 'dOe']
print(f'My name is {names[2].title()}')
for user in names:
   if user == 'jOhN':
      continue
   print(user.title())

for number in range(1, 51):
   if number == 21:
      continue
   print(f'2 times {number} is {2 * number}')
print() #for better formatting