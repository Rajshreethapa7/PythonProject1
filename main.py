from pyspark import SparkContext

sc = SparkContext("local", "CustomerDataCleaning")

data = [
    ("Smith",23,5.3),
    ("Rashmi",27,5.8),
    ("Smith",23,5.3),
    ("Payal",27,5.8),
    ("Megha",27,5.4)
]

# create RDD
rdd = sc.parallelize(data)

# remove exact duplicates
rdd1 = rdd.distinct()

# key by age and height
rdd2 = rdd1.map(lambda x: ((x[1], x[2]), x))

# remove duplicates by age,height
rdd3 = rdd2.reduceByKey(lambda a,b: a)

# result
result = rdd3.map(lambda x: x[1])

print(result.collect())

sc.stop()
