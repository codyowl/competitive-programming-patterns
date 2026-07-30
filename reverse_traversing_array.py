# simple reverse traversing approach for carry method 

mylist = [1,2,3,4,5]
'''
 range(start, stop, step)
 len(mylist) - 1 -> last index
 -1              -> stop before -1, so index 0 is included
 -1              -> move backward
'''
for i in range(len(mylist) - 1, -1, -1):
	 print(i, mylist[i])

# this will be used to carry method and do operations from right to left
