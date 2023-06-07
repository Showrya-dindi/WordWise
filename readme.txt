1. lambda_function.py uses YouTube Data API to download video comments as JSON documents and store it into s3 bucket.
NOTE: lambda_function.py has dependencies which needs to be deployed as .zip folder. For more information refer https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

2. pyspark_code.ipynb has the spark to clean the data, create a frequency table and finally generate a word cloud out of it.
