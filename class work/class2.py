# nums = []
# num = int(input('Enter a number: '))
# if len(nums) <= 5:
#   print("4Input length is up to 5 characters.")
# else:
#   print("Input length exceeds 5 characters.")



total_sum = 0

print("Please enter 5 integers. ")

for index in range(5):
    user_input = input(f'Enter number {index + 1}: ')
    
    num = int(user_input)
    
    total_sum += num

print("The total sum of the 5 inputs is:", total_sum)

