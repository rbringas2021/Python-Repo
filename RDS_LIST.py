import boto3
import configparser
import datetime

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

# Crear un cliente de Amazon RDS
rds_client = boto3.client('rds',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name='us-east-1'
)

# Obtiene una lista de todas las instancias RDS
response = rds_client.describe_db_instances()

# Ordena las instancias RDS por fecha de creación
sorted_instances = sorted(response['DBInstances'], key=lambda x: x['InstanceCreateTime'])

# Imprime los nombres de las bases de datos y su tiempo de creación
for instance in sorted_instances:
    print(instance['DBInstanceIdentifier'], instance['InstanceCreateTime'].year)

# Imprime el número total de bases de datos
print("\nTotal number of RDS databases: ", len(response['DBInstances']))

#__END__.