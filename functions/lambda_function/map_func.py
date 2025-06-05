salary : list = [2345.89, 8976.90, 5723.8, 4721.53]
sal_ups = lambda sal : sal + (sal * 0.05)
map_obj = map(sal_ups , salary)
print(map_obj)
print(list(map_obj))

nums_1 = [12, 34, 56]
nums_2 = [12, 34, 56]
sum_nums = lambda num1 , num2 : num2 + num1
mp_obj = map(sum_nums , nums_1 , nums_2)
print(tuple(mp_obj))

names = ['mAttT', 'jOhN', 'pEteR', 'jaMeS', 'rUTh']
name_cl = lambda name : name.title()
print(list(map(name_cl ,  names)))

words = ['cat', 'dog', 'fish']
with_suffix = list(map(lambda x: x + '_pet', words))
print(with_suffix)