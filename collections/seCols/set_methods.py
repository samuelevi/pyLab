#### Difference method

first_vals : set = {1 , 3 , 5 , 7 , 9}
second_vals : set = {2 , 3 , 5 , 7 , 11}
diff_res = first_vals.difference(second_vals)
print(diff_res)


###union method
###duplicates are excluded
set_one : set = {'Paul', 'John', 'Mary', 'Tim', 'Jerry'}
set_two : set = {'Peter', 'John', 'Marrita', 'Tom', 'Jerry'}
set_union = set_one.union(set_two)
print(set_union)


####intersection method
set_one : set = {'Paul', 'John', 'Mary', 'Tim', 'Jerry'}
set_two : set = {'Peter', 'John', 'Marrita', 'Tom', 'Jerry'}
set_union = set_one.intersection(set_two)
print(set_union)



#### Difference update method
set_one : set = {'Paul', 'John', 'Mary', 'Tim', 'Jerry'}
set_two : set = {'Peter', 'John', 'Marrita', 'Tom', 'Jerry'}
set_two.difference_update(set_one)
print(set_two)



####intersection update method
set_one : set = {'Paul', 'John', 'Mary', 'Tim', 'Jerry'}
set_two : set = {'Peter', 'John', 'Marrita', 'Tom', 'Jerry'}
set_one.intersection_update(set_two)
print(set_one)

###set comprehension
new_set = {name for name in set_one if name.startswith('J')}
print(new_set)

new_set_a = {name for name in set_one if 'a' in name}
print(new_set_a)