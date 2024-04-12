import boto3
import configparser
import sys

# Leer el archivo PP y obtener las instancias y sus respectivas tags
try:
    with open("PP", "r") as f:
        instance_tags = [line.strip().split() for line in f]
except FileNotFoundError:
    print("Error: Archivo 'PP' no encontrado.")
    sys.exit(1)

# Crear una sesión de boto3
config = configparser.ConfigParser()
config.read('/Users/rbringas/.aws/credentials')

aws_access_key = config.get('default', 'aws_access_key_id')
aws_secret_key = config.get('default', 'aws_secret_access_key')

session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name='us-east-1'  # Cambiado a la región us-east-1
)

# Crear un cliente EC2
ec2 = session.client('ec2')

for instance_id, tag_value in instance_tags:
    # Crear las etiquetas para cada instancia
    tags = [
        {'Key': 'asset', 'Value': 'connector'},
        {'Key': 'product', 'Value': tag_value},
        {'Key': 'component', 'Value': 'connectors-test'},
        {'Key': 'service', 'Value': f'{tag_value}-connectors-test-service'},
        {'Key': 'service-short', 'Value': 'connectors-test-service'},
        {'Key': 'long_running', 'Value': '2025/12/01'},
        {'Key': 'backup', 'Value': 'yes'},
        {'Key': 'PRODUCT', 'Value': tag_value},
        {'Key': 'PROJECT', 'Value': tag_value},
        {'Key': 'REPO', 'Value': 'tf-connectors-test'},
        {'Key': 'ROLE', 'Value': tag_value},
        {'Key': 'SERVICE', 'Value': tag_value},
        {'Key': 'ENV', 'Value': 'Development'}
    ]

    # Agregar las etiquetas a la instancia
    response = ec2.create_tags(Resources=[instance_id], Tags=tags)

    print(f"Etiquetas agregadas a la instancia '{instance_id}': {response}")

#__END__.