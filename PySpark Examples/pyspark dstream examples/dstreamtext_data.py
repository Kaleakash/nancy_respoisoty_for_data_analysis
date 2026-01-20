from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext

# 1. Spark Config
conf = SparkConf() \
    .setAppName("SimpleTextStream") \
    .setMaster("local[*]")

sc = SparkContext(conf=conf)
#sc.setLogLevel("ERROR")

# 2. Streaming Context (5 seconds)
ssc = StreamingContext(sc, 5)

# 3. Read streaming text data from socket
lines = ssc.socketTextStream("localhost", 9999)

# 4. Display data as-is
lines.pprint()

# 5. Start streaming
ssc.start()
ssc.awaitTermination()
