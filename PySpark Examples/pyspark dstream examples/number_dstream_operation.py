from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext

# 1. Spark Configuration
conf = SparkConf() \
    .setAppName("PySparkStreamingWordCount") \
    .setMaster("local[2]")

sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

# 2. Streaming Context (batch interval = 5 seconds)
ssc = StreamingContext(sc, 1)

# 3. Create DStream from socket
lines = ssc.socketTextStream("localhost", 9999)

# 4. Transformations
double_number = lines.map(lambda x:int(x)*int(x))
double_number.pprint();

# 6. Start Streaming
ssc.start()
ssc.awaitTermination()
