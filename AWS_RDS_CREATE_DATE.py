import boto3
import configparser
from datetime import datetime

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

# Obtener información detallada sobre las bases de datos RDS
response = rds.describe_db_instances()

# Obtener los nombres y fechas de creación de las bases de datos RDS
db_details = [(db_instance['DBInstanceIdentifier'], db_instance['InstanceCreateTime']) for db_instance in response['DBInstances']]

# Escribir los nombres y fechas de creación en el archivo "RDS.txt"
with open("RDS.txt", "w") as f:
    for db_name, create_time in db_details:
        create_time_str = create_time.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{db_name} - {create_time_str}\n")

print("Nombres y fechas de creación de bases de datos RDS agregados al archivo RDS.txt.")
