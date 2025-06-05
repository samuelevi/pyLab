def user_details() -> str :
   return 'User Details'

print(user_details().count('e'))
data = user_details()
print(data.upper())



def sum_nums() -> int :
   return sum([12, 34, 56, 89, 54])

print(sum_nums() / 5)