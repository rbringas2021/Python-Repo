import boto3
import sys

sys.stdout = open("empty_buckets.txt", "w")

# Crea un cliente S3
s3 = boto3.client('s3', region_name='us-east-1')

# Utiliza el cliente para obtener información sobre los bucket
buckets_info = s3.list_buckets()

# Recorre los bucket y los imprime
for bucket in buckets_info["Buckets"]:

    # Utiliza el cliente para verificar si hay objetos o no dentro de los buckets
    response = s3.list_objects_v2(Bucket=bucket['Name'])
    if 'Contents' not in response:
        print("El bucket '%s' está vacío" % bucket['Name'])
        sys.stdout.flush()

#__END__.