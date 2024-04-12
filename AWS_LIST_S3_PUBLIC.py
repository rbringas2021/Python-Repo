import boto3
import sys

file = open("buckets_status.txt", "w")
sys.stdout = file

# Crea un cliente S3
s3 = boto3.client('s3')
sts = boto3.client('sts')

# Utiliza el cliente para obtener información sobre los bucket
response = s3.list_buckets()

# Recorre los bucket y verifica quién es el creador del bucket
for bucket in response["Buckets"]:
    bucket_name = bucket["Name"]
    location = s3.get_bucket_location(Bucket=bucket_name)
    identity = sts.get_caller_identity()
    arn = identity['Arn']
    acl = s3.get_bucket_acl(Bucket=bucket_name)
    is_public = False
    for grant in acl['Grants']:
        if 'URI' in grant['Grantee'] and grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
            is_public = True
            break
    sys.stdout.write(f"El bucket {bucket_name} fue creado por el ARN {arn} en la región {location['LocationConstraint']} y es {'publico' if is_public else 'privado'}\n")

sys.stdout = sys.__stdout__
file.close()
