numbers : list = [2, 5, 6, 7, 1, 9]
print(sum(numbers))

total = 0
for number in numbers:
   total += number
print(total)
#### List Comprehension ###
numbers: list = [2, 5, 6, 7, 1, 9]
num_sqr = [number ** 2 for number in numbers]
print(num_sqr)

names :list = ['PeTeR' , 'jOhN' , 'PaUl' , 'PaMeLla' , 'mArY' , 'aNnA']
tit_names = [name.title() for name in names]
print(tit_names)
names_conts = [name_cont for name_cont in tit_names if name_cont.__contains__('a')]
print(names_conts)

names_start = [name_start for name_start in tit_names if name_start.startswith('P')]
print(names_start)

names_conts = [name_cont for name_cont in tit_names if name_cont.endswith('a')]
print(names_conts)

values : list = [23, 46, 75, 22, 3, 90, 11, 68]

even_vals = [value for value in values if value % 2 == 0]
print(even_vals)