from dask import delayed

@delayed
def add(a,b):
    print("Hello")
    return a+b;

def add1(a,b):
    print("Hi")
    return a+b;

#result1 = add(10,20);
#result2 = add1(10,20);
# print(result1)
# print(result1.compute())
# print(result1)
#print(result1.persist())    # run that task in background 
#print(result1.persist())    # run that task in background 
#print(result1.compute())