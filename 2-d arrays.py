#in this unit we can see 2d numpy array and its subseting
import numpy as np
a = np.array([5,8,3,4,6,2])
print(a[2:4])

a = [[1,2],[3,4]] #2d array as same as normal array list and list wwise
a = np.array(a)
b = a
print(b)


b = [[4,5,2],[6,5,2]] #same array list method
new = np.array(b)
print(new)

#.shape
#shape gets number of rows and cols from the array
a = np.array([[1,2],[2,4],[3,5]])
b = np.array([[6,3,9],[3,2,2]])
print(a.shape)
print(b.shape)

a = np.array([[7,7],[8,8],[9,9]])
print(a[1][0])
#sd mumpy subsetting above the example


a = np.array([[4,6],[8,2]])
print(a[1,1])
#or  same way in 2d array
print(a[1][1])

a = [[2,4],[6,3]]
b = np.array([8,1],[2,9])
print(a[2][0]==b[1,0])
#or
print(a[2,0]==b[1][0])





