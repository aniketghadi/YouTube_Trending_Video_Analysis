import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalogs
AWSGlueDataCatalog_node1685656687510 = glueContext.create_dynamic_frame.from_catalog(
    database="de-youtube-cleansed-database",
    table_name="csv_data",
    transformation_ctx="AWSGlueDataCatalog_node1685656687510",
)

# Script generated for node AWS Glue Data Catalogs
AWSGlueDataCatalog_node1685656668801 = glueContext.create_dynamic_frame.from_catalog(
    database="de-youtube-cleansed-database",
    table_name="cleansed_statistics_reference_data",
    transformation_ctx="AWSGlueDataCatalog_node1685656668801",
)

# Script generated for node Join
Join_node1685656696109 = Join.apply(
    frame1=AWSGlueDataCatalog_node1685656687510,
    frame2=AWSGlueDataCatalog_node1685656668801,
    keys1=["category_id"],
    keys2=["id"],
    transformation_ctx="Join_node1685656696109",
)

# Script generated for node Amazon S3
AmazonS3_node1685656901947 = glueContext.getSink(
    path="s3://de-youtube-analytical-data",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["region", "category_id"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1685656901947",
)
AmazonS3_node1685656901947.setCatalogInfo(
    catalogDatabase="de-youtube-analytical-database", catalogTableName="analytical_data"
)
AmazonS3_node1685656901947.setFormat("glueparquet")
AmazonS3_node1685656901947.writeFrame(Join_node1685656696109)
job.commit()
