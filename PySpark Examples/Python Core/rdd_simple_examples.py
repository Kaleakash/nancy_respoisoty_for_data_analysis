from pyspark import SparkContext, SparkConf
# configure Spark Configuration 
config = SparkConf().setAppName("RDD Set Operations Example").setMaster("local[4]")

# create Spark Context
sc = SparkContext(conf=config)

# Input Data 
data = [1, 2, 3, 4, 5,6,7,8,9,10]

# using list we need to create RDD 
rdd = sc.parallelize(data);



# action on RDD 
# result = rdd.collect()
# print("Original RDD: ", result)


# we can do some transformation on rdd data 
# map transformation
# mapped_rdd = rdd.map(lambda x: x * 3)
# result1 = mapped_rdd.collect()
# print("Mapped RDD: ", result1)

# filter transformation
#filtered_rdd = rdd.filter(lambda x: x > 5)
# result2 = filtered_rdd.collect()
# print("Filtered RDD (elements > 5): ", result2)    

even_rdd = rdd.filter(lambda x: x % 2 == 0)
odd_rdd = rdd.filter(lambda x: x % 2 != 0)
#print("Even RDD: ", even_rdd)
#print("Odd RDD: ", odd_rdd)

print("Even RDD: ", even_rdd.collect())
print("Odd RDD: ", odd_rdd.collect())

# stop spark context 
sc.stop();
