from dask import delayed
def add(a,b):
    return a+b
result1 = add(10,20);   # calling normal function 
print(result1)
result2 = delayed(add)(10,20);
result3 = delayed(add)(30,40);
print(result2)
print(result3)
print(result2.compute());   #now perform the task
print(result3.compute())
result4 = delayed(add)(result2,result3)
print(result4.compute())