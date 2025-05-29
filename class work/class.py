numbers = [4, 8, 9, 12, 3]
total=0
for number in numbers:
  total += number
print(total)


# # # summation = 0
# # #     summation += number
# # # print(summation)


# # # sum_of_numbers = sum(number)

# # # print(f"The sum of the numbers is: {sum_of_numbers}")

# # average = sum(number) / len(number)
# # print(average)

vals = {'a' : 30.05,
         'b' : 42.86,
         'c' : 50.82,
         'd' : 72.56,
         'e' : 17.59}

numbers = vals.values()
list_vals = list(numbers)
print(list_vals)

sum_val = 0
for list_val in list_vals:
  sum_val += list_val
print(sum_val)

for key, val in vals.items():
  vals[key] = val+val*0.25
print(vals)




vals = {
    'a': 30.05,
    'b': 42.86,
    'c': 50.82,
    'd': 72.56,
    'e': 17.59
}

# Calculate and print the cumulative sum directly from the dictionary values
sum_val = 0
for val in vals.values():
    sum_val += val
print(sum_val)

# Update values in the dictionary and print
vals = {key: val * 1.25 for key, val in vals.items()}
print(vals)
