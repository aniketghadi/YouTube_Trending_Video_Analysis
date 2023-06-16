# YouTube_Trending_Video_Analysis

Summary of the Project
The project aims to securely manage, streamline, and perform analysis on structured and semi-structured YouTube video data. The data will be ingested from the Kaggle Dataset,  Lambda function used for Data Cleaning, processed using a Glue ETL job, and then later stored in AWS Athena by running Glue Crawler on the S3 buckets. The data was then analyzed using AWS Quicksight and also tried to generate reports and insights using Tableau.

Services Used
The following AWS services will be used to achieve the project goals:

A. Amazon S3
Amazon S3 will be used to store the structured data in a data lake. The data will be partitioned and stored in S3 buckets.

B. AWS IAM
AWS IAM will be used to manage access to AWS resources. IAM policies will be created to ensure that only authorized users have access to the data.

C. QuickSight/Tableau
AWS QuickSight will be used to generate reports and insights from the data stored in the data lake. QuickSight will provide a user-friendly interface for generating reports.

D. AWS Glue
AWS Glue will be used to create the ETL system. The glue will extract, transform, and load the data into the data lake.

E. AWS Lambda
AWS Lambda will be used to execute code in response to events. Lambda will be used to trigger the ETL process when new data is available on the source S3 path and also to clean the data.

F. AWS Athena
AWS Athena will be used to query the data stored in the data lake. Athena provides a serverless query service that allows users to analyze data using SQL.


Benefits of Analyzing Trending YouTube Video Data
Analyzing YouTube video data can provide valuable insights into user behavior, content popularity, and trends. These insights can be used to improve content creation, marketing strategies, and user engagement.
