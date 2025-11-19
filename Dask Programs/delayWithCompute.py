from dask import delayed,compute
@delayed
def add(a,b):
    return a+b;

result1 = add(10,20)
print(result1.compute())    # return result as output 
result2 = add(30,40);
result3 = compute(result2); # return as tuple 
print(result3)
result4 = compute(result1,result2,result3);
print(result4)