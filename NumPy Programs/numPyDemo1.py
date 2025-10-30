import numpy as np;
# one D array 
arr = np.array([10,20,30,40,50]);
print("NumPy Array data ",arr)
# two D Array 
zeros = np.zeros((2,3))
ones = np.ones((3,3))
print(zeros)
print(ones)
range_array = np.arange(0,20,1);# start, end and increment 
print(range_array)
random = np.random.randint(1,100)
print(random)
print("matrix attributes")
matrix = np.array([[1,2,3],[4,5,6]])
print(matrix)
print("Shape ",matrix.shape)
print("Dimension ",matrix.ndim)
print("Data types  ",matrix.dtype)
print("-------------------")
a = np.array([1,2,3,4])
b = np.array([10,20,30,40]);
c = np.array([100,200,300])
d = np.array([1000,2000,3000])
print("Addition ",a+b);
print("Sub ",a-b);
print("Mul ",a*b);
print("Div ",a/b);
print("add ",c+d)