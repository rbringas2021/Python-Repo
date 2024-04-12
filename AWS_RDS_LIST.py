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

# Crear un cliente RDS
rds = session.client('rds')

# Obtener información sobre las bases de datos RDS
response = rds.describe_db_instances()

# Obtener los nombres de las bases de datos RDS
db_names = [db_instance['DBInstanceIdentifier'] for db_instance in response['DBInstances']]

# Escribir los nombres de las bases de datos en el archivo "RDS.txt"
with open("RDS.txt", "w") as f:
    for db_name in db_names:
        f.write(f"{db_name}\n")

print("Nombres de bases de datos RDS agregados al archivo RDS.txt.")

# __END__.