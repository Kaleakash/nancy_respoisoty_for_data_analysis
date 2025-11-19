import dask.bag as db

def main():
    result = db.from_sequence(range(100));
    result1 = result.map(lambda x:x*2).compute()
    print(result1)

if __name__=="__main__":
    main();