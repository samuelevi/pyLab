### Nested if
user_name = 'admin'
password = 'admin123'
if user_name == 'admin':
   if password == 'admin123':
      print('Welcome admin')
      print('You have full access to the system')
   else:
      print('Incorrect password')
      print('please try again')

else:
   print('Incorrect username')
   print('Please try again')