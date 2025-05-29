### Match case
day = input('Enter the day of the week: ')
match day:
   case 'Monday':
      print('Today is Monday')
      print('start of the week')
   case 'Tuesday':
      print('Today is Tuesday')
      print('Second day of the week')
   case 'Wednesday':
      print('Today is Wednesday')
      print('Third day of the week')
   case 'Thursday':
      print('Today is Thursday')
      print('Fourth day of the week')
   case 'Friday':
      print('Today is Friday')
      print('Fifth day of the week')
   case 'Saturday':
      print('Today is Saturday')
      print('Sixth day of the week')
   case 'Sunday':
      print('Today is Sunday')
      print('Weekends')
   case _:
      print('Invalid day')
      print('Please enter a valid day of the week')