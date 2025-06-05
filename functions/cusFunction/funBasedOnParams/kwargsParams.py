def users(**kwargs):
   return kwargs

app_users = users(one = 'Paul', two = 'Peter', three = 'Matt', four = 'Tola')
print(app_users)


def sum_nums(**nums):
   return sum(nums.values())

sum_res = sum_nums(c = 23, b = 56, a = 23, x = 12, y = 98, z = 45)
print(sum_res)


