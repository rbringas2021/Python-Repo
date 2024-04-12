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

# Obtener los nombres de las bases de datos RDS y sus grupos de opciones
db_info = [(db_instance['DBInstanceIdentifier'], db_instance.get('OptionGroupMemberships', [])) for db_instance in response['DBInstances']]

# Escribir los nombres de las bases de datos y sus grupos de opciones en el archivo "SQL.txt"
with open("SQL.txt", "w") as f:
    for db_name, option_groups in db_info:
        f.write(f"Nombre de la base de datos: {db_name}\n")
        f.write("Grupos de opciones:\n")
        for option_group in option_groups:
            f.write(f"  - {option_group['OptionGroupName']}\n")
        f.write("\n")

print("Información sobre bases de datos RDS y sus grupos de opciones agregada al archivo SQL.txt.")
