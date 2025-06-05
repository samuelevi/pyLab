def users(*args):
   return args

app_users = users('Paul', 'Peter', 'Matt', 'Tola')
print(app_users)


def sum_nums(*nums):
   return sum(sum_nums)

sum_res = sum_nums(23, 56, 23, 12, 98, 45)
print(sum_res)