#! /usr/bin/python
import pyspark
from pyspark.sql.functions import *
from pyspark.sql.types import DoubleType

# Initialize Spark Session
from pyspark.sql import SparkSession
spark = SparkSession \
  .builder \
  .master('yarn') \
  .appName('air_quality_pyspark') \
  .getOrCreate()

#Pull all file from google storage once off and concatenate them
df = spark.read.option("delimiter", ",").option("header", True).csv("gs://air_quality_cyprus/Data_Hourly_*.csv")

#Add Datetime
df = df.withColumn("date_time",to_timestamp(df.date_time,'dd/MM/yyyy HH:mm'))
df = df.withColumn("date",date_format(df.date_time,'yyyy-MM-dd'))

#Set pollutant_value as DoubleType
df = df.withColumn("pollutant_value",df.pollutant_value.cast(DoubleType()))
df_aggr_daily = df.groupby(['date','station_code','pollutant_id']).mean("pollutant_value").withColumnRenamed("avg(pollutant_value)","mean_pollutant_value")

#load AirQualityMonitoringStations
df_stations = spark.read.option("delimiter", ",").option("header", True).csv("gs://air_quality_cyprus/AirQualityMonitoringStations.csv")
df_stations = df_stations.select(col("station_code"),col("station_name_en"),col("latitude"),col("longitude"))
df_stations = df_stations.withColumnRenamed('station_code','station_code_pk')

#Load PollutantsId
df_Pollutants = spark.read.option("delimiter", ",").option("header", True).csv("gs://air_quality_cyprus/PollutantsId.csv")
df_Pollutants = df_Pollutants.select(col("pollutant_id"),col("pollutant_code"),col("pollutant_name_en"),col("Unit_of_measurement_en"))
df_Pollutants = df_Pollutants.withColumnRenamed('pollutant_id','pollutant_id_pk')

#Join on aggr data
df_aggr_daily = df_aggr_daily.join(df_stations,df_aggr_daily.station_code == df_stations.station_code_pk, how="inner")
df_aggr_daily = df_aggr_daily.join(df_Pollutants,df_aggr_daily.pollutant_id == df_Pollutants.pollutant_id_pk, how="inner")
df_aggr_daily = df_aggr_daily.drop("station_code_pk").drop("pollutant_id_pk")

# Saving the data to BigQuery
temp_bucket = 'staging_for_bigquery'
table = "comp548dl-big-data.air_quality_cyprus.daily_data"
df_aggr_daily.write.format("bigquery").mode('overwrite').option("temporaryGcsBucket",temp_bucket).option("table",table).save()

#Store the date
#df_aggr_daily.write.option("delimiter", ",").option("quote", "\"").option("header", True).option("temporaryGcsBucket","some-bucket").mode('overwrite').csv('gs://air_quality_cyprus/Data_Daily_All')