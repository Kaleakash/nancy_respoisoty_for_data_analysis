from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.master("local[*]").appName("DataFrame Examples").getOrCreate();
# sample data 
data = [
    ("IT","Raj",50000),
    ("HR","Anita",60000),
    ("IT","John",55000),
    ("Finance","Sara",70000),
    ("HR","David",62000),
    ("Finance","Mike",75000),
    ("IT","Sophia",52000),
    ("Finance","Linda",72000),
    ("HR","James",58000)
]
column = ["Department","Name","Salary"]

df = spark.createDataFrame(data, column);
# display data in table format 
#df.show();

# display schema of data frame
#df.printSchema();


# select specific columns
#df.select("Name","Salary").show();

# filter rows based on condition
#df.filter(df.Salary > 60000).show();

# column base conditions 
#df.withColumn("salary_with_bonus",col("Salary")+2000).show();

#drop particular column 
#df.drop("Department").show();


# order by clause 
#df.orderBy("Salary",ascending=False).show();
df.orderBy("Salary",ascending=True).show();
spark.stop();