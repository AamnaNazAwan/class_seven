import numpy as np
#create sample data
data = np.array([[1,2,3],[4,5,6]])
another_array = np.array([10,20,30])

#save the data to rext file
np.savetxt('practice.txt',data,delimiter=',')
#load data from text to file
loaded_data_txt = np.loadtxt('practice.txt',delimiter=',')
print("loaded from text file:\n",loaded_data_txt)

array1 = np.array([1,2,3])
array2 = np.array ([6,7,8])
array3 = np.array([array1]+[array2])

print(array3)

m,n = 3,3
arr = np.eye(m,n)
print("the identity matrix of 3*3 is",arr)

start,stop,step = 10,50,1
arr = np.arange(start,stop,step)
print("the numpy array between 1 to 50 is",arr)
