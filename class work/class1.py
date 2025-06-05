def add_numbers() -> int:
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = num1 + num2
    return result
print(add_numbers())

### write a function to sum numbers in a list

def sum_list(nums:list) -> int:
    total:int = 0
    for num in nums:
       total = total + num
    return total
    
print(sum_list([4,7,3,9]))


# print(user_details().count('e'))
# data = user_details()
# print(data.upper())

# numbers = [4, 8, 9, 12, 3]
# total=0
# for number in numbers:
#   total += number
# print(total)