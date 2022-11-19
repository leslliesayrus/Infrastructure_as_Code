import boto3
from io import StringIO
import pandas as pd

# creating the dataframe
dic = {
    'name': ['Charlie', 'Jennifer', 'Emma'],
    'age': [19, 25, 30]
}

df = pd.DataFrame(dic)

# preparing the dataframe to load
csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    
# setting the connection to the AWS
conn_aws = boto3.client('s3', 
    region_name = 'region',
    aws_access_key_id = 'id_key',
    aws_secret_access_key = 'secret_id'
    )

# loading the file 
response=conn_aws.put_object(Body=csv_buffer.getvalue(),
                           Bucket='bucket-name',
                           Key='file_name.csv')