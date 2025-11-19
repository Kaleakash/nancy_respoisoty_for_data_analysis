from dask import delayed

@delayed
def add(a,b):
    return a+b

result1 = add(10,20);
print(result1)
print(result1.compute())