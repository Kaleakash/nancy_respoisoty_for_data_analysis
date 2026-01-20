from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext

# 1. Spark Configuration
conf = SparkConf() \
    .setAppName("PySparkStreamingWordCount") \
    .setMaster("local[2]")

sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

# 2. Streaming Context (batch interval = 5 seconds)
ssc = StreamingContext(sc, 5)

# 3. Create DStream from socket
lines = ssc.socketTextStream("localhost", 9999)

# 4. Transformations
words = lines.flatMap(lambda line: line.split(" "))
words.pprint();
word_pairs = words.map(lambda word: (word, 1))
word_pairs.pprint();
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)
# 5. Output
word_counts.pprint()

# 6. Start Streaming
ssc.start()
ssc.awaitTermination()
