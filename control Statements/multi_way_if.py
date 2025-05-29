## Multi way if statement allows us to check multiple conditions
## syntax
## if condition 1:
##  # block of code to be executed if condition 1 is true
## elif condition 2:
##  # block of code to be executed if condition 2 is true
## elif condition 3:
##  # block of code to be executed if condition 3 is true
##else:
##  # block of code to be executed if all conditions are false

day = input('Enter the day of the week: ')
if day == 'Monday':
   print('Today is Monday')
   print('start of the week')
elif day == 'Tuesday':
   print('Today is Tuesday')
   print('Second day of the week')
elif day == 'Wednesday':
   print('Today is Wednesday')
   print('Third day of the week')
elif day == 'Thursday':
   print('Today is Thursday')
   print('Fourth day of the week')
elif day == 'Friday':
   print('Today is Friday')
   print('Fifth day of the week')
elif day == 'Saturday':
   print('Today is Saturday')
   print('Sixth day of the week')
else :
   print('Today is Sunday')
   print('Last day of the week')