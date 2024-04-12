import boto3
import sys

sys.stdout = open("buckets.txt", "w")

# Crea un cliente S3
s3 = boto3.client('s3', region_name='us-east-1')

# Utiliza el cliente para obtener información sobre los buckets
buckets_info = s3.list_buckets()

# Recorre los buckets y los imprime
for bucket in buckets_info["Buckets"]:
    print(bucket['Name'])

#__END__.