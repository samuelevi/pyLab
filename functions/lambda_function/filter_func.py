salary : list = [2345.89, 8976.90, 5723.8, 4721.53]
sal_ups = lambda sal : sal > 5000
filt_obj = filter(sal_ups , salary)
print(filt_obj)
print(list(filt_obj))

nums_1 = [13, 17, 77, 45, 12, 34, 56]
odd_nums = lambda num : num % 2 == 1
filt_obj = filter(odd_nums , nums_1)
print(tuple(filt_obj))

fruits = ['mango', 'Kiwi', 'apple', 'carrot', 'cherry', 'sour-sop']
fruita = lambda fruit : fruit.__contains__('a')
filt_obj = filter(fruita , fruits)
print(tuple(filt_obj))