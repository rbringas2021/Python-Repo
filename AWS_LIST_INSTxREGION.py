import boto3
import sys
import configparser

# Leer las credenciales de AWS desde el archivo
config = configparser.ConfigParser()
config.read('/Users/rbringas/.aws/credentials')
aws_access_key = config.get('default', 'aws_access_key_id')
aws_secret_key = config.get('default', 'aws_secret_access_key')

# Crear una sesión de boto3
session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

# Obtener todas las regiones conocidas de EC2
ec2_regions = [region['RegionName'] for region in session.client('ec2').describe_regions()['Regions']]

# Leer los IDs de instancia desde el archivo instance_id.txt
try:
    with open("instance_id.txt", "r") as f:
        instance_ids = [line.strip() for line in f]
except FileNotFoundError:
    print("Error: Archivo 'instance_id.txt' no encontrado.")
    sys.exit(1)

# Buscar en cada región las instancias con los IDs proporcionados
for region_name in ec2_regions:
    # Crear un cliente EC2 para la región actual
    ec2_region = session.client('ec2', region_name=region_name)
    
    try:
        response = ec2_region.describe_instances(InstanceIds=instance_ids)
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                print(f"La instancia {instance['InstanceId']} está en la región {region_name}")
    except ec2_region.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidInstanceID.NotFound':
            print(f"No se encontraron instancias en la región {region_name} con los IDs proporcionados.")
        else:
            print(f"Error al buscar instancias en la región {region_name}: {e}")

