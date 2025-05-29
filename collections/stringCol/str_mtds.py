message : str = 'Congratulations User'
print(len(message))

print(message.capitalize())
print(message.title())
print(message.upper())
print(message.lower())
print(message.casefold())
print(message.swapcase())

my_music = 'hello.mp3'
print(my_music.startswith('mp3'))
print(my_music.endswith('mp3'))

user_details = '  my details are Samuel Evi   '
print(user_details.strip())
print(user_details.lstrip())
print(user_details.rstrip())

print(user_details.count('e'))
print(user_details.count('a' , 3))
print(user_details.count('a' , 3 , 9))

print(user_details.find('Samuel'))
print(user_details.index('Samuel'))

