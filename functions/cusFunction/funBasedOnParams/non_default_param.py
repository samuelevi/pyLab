def user_details(data : str) -> str :
   return data

print(user_details('Hello Friends').count('e'))
data = user_details('Hello Students')
print(data.upper())



def sum_nums(nums:list) -> int :
   return sum(nums)

print(sum_nums([12, 34, 56, 89, 54]) / 5)

sum_res = (sum_nums([12, 56, 78, 12, 56, 34]))

sum_res = sum_nums([1, 3, 8, 34, 90])
print(sum_res.as_integer_ratio())