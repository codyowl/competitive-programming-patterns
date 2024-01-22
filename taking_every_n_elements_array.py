mylist = [1,2,3,4,5,6,7,8]

'''
for framing every two element in the given list
'''
# 1 elements
zip_list = list(zip(mylist,mylist[1:]))
print(mylist)
print("taking 1 element")
print(zip_list)

# 2 elements
zip_list = list(zip(mylist,mylist[2:]))
print("taking 2 element")
print(zip_list)

#forming combination of each element with sequential one
a = [1,2,3,4,5,6]
one_element_combination = list(zip(a[::2], a[1::2]))
print(a)
print("forming pair by taking eery two elements")
print(one_element_combination)