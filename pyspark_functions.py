from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window


# -----------------------------
# Create Spark Session
# -----------------------------
def create_spark():
    spark = SparkSession.builder \
        .appName("PySpark Functions Demo") \
        .getOrCreate()
    return spark


# -----------------------------
# Window Function Example
# -----------------------------
def window_functions(spark):

    data = [
        ("James", "Sales", 3000),
        ("Michael", "Sales", 4600),
        ("Robert", "Sales", 4100),
        ("Maria", "Finance", 3000),
        ("James", "Finance", 3900),
        ("Scott", "Finance", 3300)
    ]

    columns = ["employee_name", "department", "salary"]

    df = spark.createDataFrame(data, columns)

    windowSpec = Window.partitionBy("department").orderBy(col("salary").desc())

    result = df.withColumn("row_number", row_number().over(windowSpec)) \
        .withColumn("rank", rank().over(windowSpec)) \
        .withColumn("dense_rank", dense_rank().over(windowSpec))

    print("Window Functions Output")
    result.show()


# -----------------------------
# Lag and Lead Example
# -----------------------------
def lag_lead_functions(spark):

    data = [
        ("2023-01",100),
        ("2023-02",200),
        ("2023-03",300),
        ("2023-04",400)
    ]

    columns = ["month","sales"]

    df = spark.createDataFrame(data,columns)

    windowSpec = Window.orderBy("month")

    result = df.withColumn("previous_sales", lag("sales",1).over(windowSpec)) \
               .withColumn("next_sales", lead("sales",1).over(windowSpec))

    print("Lag Lead Output")
    result.show()


# -----------------------------
# Date Functions
# -----------------------------
def date_functions(spark):

    data = [("1","2020-02-01"),
            ("2","2019-03-01"),
            ("3","2021-03-01")]

    columns = ["id","date"]

    df = spark.createDataFrame(data,columns)

    df = df.withColumn("date", to_date(col("date")))

    result = df.withColumn("year", year("date")) \
        .withColumn("month", month("date")) \
        .withColumn("day", dayofmonth("date")) \
        .withColumn("week_of_year", weekofyear("date"))

    print("Date Functions Output")
    result.show()


# -----------------------------
# Timestamp Functions
# -----------------------------
def timestamp_functions(spark):

    data=[["1","2020-02-01 11:01:19"],
          ["2","2019-03-01 12:01:19"],
          ["3","2021-03-01 12:01:19"]]

    columns=["id","timestamp"]

    df=spark.createDataFrame(data,columns)

    df=df.withColumn("timestamp",to_timestamp("timestamp"))

    result=df.withColumn("hour",hour("timestamp")) \
             .withColumn("minute",minute("timestamp")) \
             .withColumn("second",second("timestamp"))

    print("Timestamp Functions Output")
    result.show()


# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":

    spark = create_spark()

    window_functions(spark)

    lag_lead_functions(spark)

    date_functions(spark)

    timestamp_functions(spark)

    spark.stop()