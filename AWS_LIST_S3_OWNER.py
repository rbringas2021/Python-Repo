import boto3
import sys

file = open("buckets_creador.txt", "w")
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
    sys.stdout.write(f"El bucket {bucket_name} fue creado por el ARN {arn} en la región {location['LocationConstraint']}\n")

sys.stdout = sys.__stdout__
file.close()

#__END__