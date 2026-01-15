from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
# configure Spark Configuration 
config = SparkConf().setAppName("RDD as well as DataFrame").setMaster("local[4]")
# create Spark Context
sc = SparkContext(conf=config)
# create Spark Session
# list of tuples
emp_data = [("James",34,"M"),("Anna",30,"F"),("Jeff",41,"M")] 
# to create the RDD 
emp_rdd = sc.parallelize(emp_data)
# age conditions 
age_filter = emp_rdd.filter(lambda x: x[1] > 30)
# collect the results

print(age_filter.collect()) # it display those records whose age is greater than 30
sc.stop();

print("------------------------------------------");
spark = SparkSession.builder.config(conf=config).getOrCreate();
# we do with DataFrame with spark reference 
emp_data_df = spark.createDataFrame(emp_data, ["Name", "Age", "Gender"])   
# display the DataFrame
emp_data_df.show()                  # it display all records in DataFrame format
spark.stop();