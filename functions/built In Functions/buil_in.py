### input functions ####
value = input("Enter a value: ")
print(f"You entered: {value}")

### converting to integer
fn = int(value)
print(f"You entered: {fn + 5}")


### type function ###
name = 'John'
print(type(name))


age = 23
print(type(age))

age = 23
print(type([]))

age = 23
print(type({2}))

### ord and chr functions ###
print(ord('A'))


print(chr(11422))

### id function ###
name = 'John'
age = 34
print(id(name))
print(id(age))


max_res = max([23, 93, 90, 50, 56])
print(max_res)
min_res = min([23, 93, 90, 50, 56])
print(min_res)

### round function ###
round_res = round(3.14159, 2)
print(round_res)

###abs function ###
abs_res = abs(-42)
print(abs_res)

### pow function ###
pow_res = pow(2, 3)
print(pow_res)
### divmod function ###
divmod_res = divmod(10, 3)
print(divmod_res)

bin_res = bin(42)
print(bin_res)
oct_res = bin(42)
print(oct_res)
hex_res = bin(42)
print(hex_res)
sorted_res = sorted([5, 2, 9, 1, 5, 6])
print(sorted_res)

reversed_res = list(reversed([1,2,3,4,5]))

enumerated_obj = enumerate(['apple', 'banana', 'cherry'])
print(list(enumerated_obj))

age = '34'
ins_res = isinstance(age, str)
print(ins_res)

name = ['John', 'Doe', 'Jane']
ins_res = isinstance(name, tuple)
print(ins_res)

