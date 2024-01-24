first_array = [1,2,3,4,5,6]
second_array = [3,5]

missing_array_list = [x for x in first_array if x not in second_array]

print(missing_array_list)