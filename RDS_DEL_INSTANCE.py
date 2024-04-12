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
rds = session.client('rds')

# Ask user for RDS instance name
instance_name = input("Enter the name of the RDS instance you want to delete: ")

# Delete the RDS instance
response = rds.delete_db_instance(
    DBInstanceIdentifier=instance_name,
    SkipFinalSnapshot=True # Cambia a False si deseas crear un snapshot antes de eliminar
)

# Check status of the RDS instance
response = rds.describe_db_instances(DBInstanceIdentifier=instance_name)
status = response['DBInstances'][0]['DBInstanceStatus']
print(f"RDS instance {instance_name} is now in status: {status}")

#__END__.