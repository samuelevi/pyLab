vote_func = lambda age : print('You Can Vote') if age > 18 else print('You cannot Vote')
vote_func(20)

login = lambda usernaame , password : 'login successfully' \
if (usernaame == 'admin') and (password == 'abcd') else 'check your info'

print(login('admin' , 'abcd'))