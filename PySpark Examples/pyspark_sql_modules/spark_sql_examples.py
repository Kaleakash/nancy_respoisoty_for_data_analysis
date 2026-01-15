from pyspark.sql import SparkSession
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
print("Display Employee details using DataFrame with show functions")
#df.show();
print("---------------------------");
df.createOrReplaceTempView("employee");  # providing temporary table name as employee 
print("Display Employee details using SQL query")
#spark.sql("select * from employee").show();
# display only few columsn 
#spark.sql("select Name,Salary from employee").show();
# display record with salary condition 
#spark.sql("select * from employee where Salary > 50000").show();
# display data with order by clause 
#spark.sql("select * from employee order by Salary desc").show();
# group by clause 
spark.sql("select Department,sum(Salary) from employee group by Department").show();
spark.stop();