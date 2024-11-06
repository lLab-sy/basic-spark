# Import necessary libraries
from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder.appName("Example").getOrCreate()

# Create a DataFrame
data = [("Alice", 29), ("Bob", 31), ("Cathy", 25)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Show DataFrame content
df.show()
