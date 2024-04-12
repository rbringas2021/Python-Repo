import boto3
import configparser
import os

# Crear una sesión de boto3
config = configparser.ConfigParser()
config.read('/Users/rbringas/.aws/credentials')

aws_access_key = config.get('default', 'aws_access_key_id')
aws_secret_key = config.get('default', 'aws_secret_access_key')

session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name='us-east-1'
)

# Verificar si el archivo de nombres de buckets existe
file_path = 'buckets_empty.txt'
if not os.path.exists(file_path):
    print(f"Error: el archivo '{file_path}' no existe.")
    exit()

# Leer nombres de buckets desde un archivo
bucket_names = []
with open(file_path, 'r') as f:
    for line in f:
        bucket_names.append(line.strip())

# Iterar sobre los nombres de buckets
for bucket_name in bucket_names:
    # Verificar si el bucket está vacío
    try:
        s3_client = boto3.client('s3')
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"El nombre de bucket '{bucket_name}' está vacío y ha sido eliminado.")
    except Exception as e:
        print(f"Error: No se pudo eliminar el nombre de bucket '{bucket_name}': {e}")

#__END__.