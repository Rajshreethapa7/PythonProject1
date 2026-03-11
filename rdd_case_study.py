from pyspark.sql import SparkSession

# Step 1: Create Spark Session
spark = SparkSession.builder \
    .appName("RDD Case Study") \
    .master("local[*]") \
    .getOrCreate()

# Spark Context
sc = spark.sparkContext


# step 2: loading data

data = [
    "1,101,5001,Laptop,Electronics,1000.0,1",
    "2,102,5002,Headphones,Electronics,50.0,2",
    "3,101,5003,Book,Books,20.0,3",
    "4,103,5004,Laptop,Electronics,1000.0,1",
    "5,102,5005,Chair,Furniture,150.0,1"
]

transactions_rdd = sc.parallelize(data)

#convert csv--->tuple

transactions_tuple_rdd = transactions_rdd.map(lambda line: line.split(","))
print(transactions_tuple_rdd.collect())

#filter transaction

high_quantity_rdd = transactions_tuple_rdd.filter(lambda x: int(x[6]) > 1)

print(high_quantity_rdd.collect())

#using flatmap

products_flat_rdd = transactions_tuple_rdd.flatMap(lambda x: [x[3]])

print(products_flat_rdd.collect())

#creating pair RDD

pair_rdd = transactions_tuple_rdd.map(
    lambda x: (x[1], (x[3], float(x[5]) * int(x[6])))
)

print(pair_rdd.collect())

# Total spending per customer
customer_spending_rdd = pair_rdd.map(
    lambda x: (x[0], x[1][1])
).reduceByKey(lambda x, y: x + y)

print(customer_spending_rdd.collect())



#product purchased per customer

customer_products_rdd = pair_rdd.map(
    lambda x: (x[0], x[1][0])
).groupByKey().mapValues(list)

print(customer_products_rdd.collect())

#creating product category RDD

product_category_data = [
    ('Laptop', 'Electronics'),
    ('Headphones', 'Electronics'),
    ('Book', 'Books'),
    ('Chair', 'Furniture')
]

product_category_rdd = sc.parallelize(product_category_data)

#join operations

customer_product_category_rdd = pair_rdd.map(
    lambda x: (x[1][0], (x[0], x[1][1]))
).join(product_category_rdd)

print(customer_product_category_rdd.collect())

