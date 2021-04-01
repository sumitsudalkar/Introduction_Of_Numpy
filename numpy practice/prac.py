import numpy as np 

mylist = [10,20,30,40,50,64]
arr = np.array(mylist)
print("Elements:")
for ele in arr:
    print(ele)

mylist1 = [[10,20,30],[40,50,60],[70,80,90]]
matrix = np.array(mylist1)
print(matrix)
for row in matrix:
    print(row)

for row in matrix:
    for ele in row:
        print(ele)

res = matrix[: :]
print(res)