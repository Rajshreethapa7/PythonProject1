from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col

spark = SparkSession.builder.appName("CarPowerAnalysis").getOrCreate()


def transform_car_data():
    global df_transformed


transform_car_data()

df_transformed.show(spark)