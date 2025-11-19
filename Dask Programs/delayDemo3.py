from dask import delayed

@delayed
def fun1(x):
    return x*2;

@delayed
def fun2(x):
    return x*3;

result1 = fun1(10);
print(result1)
result2= fun2(result1.compute());
print(result2.compute())
#result1 = fun2(fun1(10))
#print(result1)
#print(result1.compute())