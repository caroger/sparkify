import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import asc, desc
from pyspark.sql.functions import sum as Fsum
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType, StringType


# Create Spark Session
spark = SparkSession.builder.appName("Sparkify").getOrCreate()

# Load Data
file_path = "./mini_sparkify_event_data.json"
df = spark.read.json(file_path)

print(df.head())


