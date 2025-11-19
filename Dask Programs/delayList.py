from dask import delayed

@delayed
def double(x):
    return x*2;

data = [1,2,3,4,5];

task = [double(i) for i in data]
#print(task)
print([t.compute() for t in task])