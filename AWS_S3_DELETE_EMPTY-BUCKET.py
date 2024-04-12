import boto3
import configparser

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

# Obtener el nombre del bucket
bucket_name = input("Ingrese el nombre del bucket que desea borrar: ")

# Verificar si el bucket está vacío
try:
    s3_client = boto3.client('s3')
    s3_client.delete_bucket(Bucket=bucket_name)
    print(f"El nombre de bucket '{bucket_name}' está vacío y ha sido eliminado.")
except Exception as e:
    print(f"Error: No se pudo eliminar el nombre de bucket '{bucket_name}': {e}")

#__END__.