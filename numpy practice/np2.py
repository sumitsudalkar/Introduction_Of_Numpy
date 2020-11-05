import numpy as np

n1 = np.array([10,20,24,15,30,589,30,20])
n2 = np.array([12,20,30,45,84,886,33,20])
r = np.intersect1d(n1,n2)
print(r)

r1 = np.setdiff1d(n1,n2)
print(r1)

#numpy mathematics
add = np.sum([n1,n2])
print(add)

#scaler mathematics in numpy
scaler = np.array([10,20,36,25,89,78])
scalar = scaler+1
print(scaler)

scaler = scaler/2
print(scaler)

scaler = scaler-5
print(scaler)

scaler = scaler*4
print(scaler)

#save and load 
arr1 = np.array([15,20,22,14,45,13])
np.save('my_arr1',arr1)

new_arr1 = np.load('my_arr1.npy')
print(new_arr1)