from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Cleanup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("order_id"), col("customer_id"), col("amount"), lit(100).alias("account_length_days"))
