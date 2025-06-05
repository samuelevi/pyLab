def user_details(data : str = 'Hello Users') -> str :
   return data

print(user_details().count('e'))
data = user_details()
print(data.upper())

data = user_details('I am a good guy')
print(data.upper())


def sum_nums(nums:list = [1, 2, 3, 4]) -> int :
   return sum(nums)

print(sum_nums())
print(sum_nums([12, 34, 56, 89, 54]) / 5)

sum_res = (sum_nums([12, 56, 78, 12, 56, 34]))

sum_res = sum_nums([1, 3, 8, 34, 90])
print(sum_res.as_integer_ratio())