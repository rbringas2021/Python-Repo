import boto3
import sys
import configparser
import os

def get_aws_credentials():
    # Path to the AWS CLI credentials file
    aws_credentials_path = os.path.expanduser("~/.aws/credentials")

    if not os.path.exists(aws_credentials_path):
        print("Error: Archivo de credenciales de AWS no encontrado.")
        sys.exit(1)

    config = configparser.ConfigParser()
    config.read(aws_credentials_path)

    aws_access_key = config.get('default', 'aws_access_key_id')
    aws_secret_key = config.get('default', 'aws_secret_access_key')

    return aws_access_key, aws_secret_key

def validate_instance_ids(ec2, instance_ids):
    # Validar los Instance IDs
    valid_instance_ids = []
    invalid_instance_ids = []
    for instance_id in instance_ids:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        if response['Reservations']:
            valid_instance_ids.append(instance_id)
        else:
            invalid_instance_ids.append(instance_id)
    return valid_instance_ids, invalid_instance_ids

def update_tag_value(tag_to_update, new_tag_value, region, valid_instance_ids):
    # Obtener las credenciales de AWS
    aws_access_key, aws_secret_key = get_aws_credentials()

    # Crear una sesión de boto3 con las credenciales
    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region
    )

    # Crear un cliente EC2 en la sesión
    ec2 = session.client('ec2')

    print(f"Buscando instancias con la etiqueta '{tag_to_update}' en la región '{region}'...")

    # Procesar las instancias con IDs válidos
    for instance_id in valid_instance_ids:
        response = ec2.describe_tags(Filters=[{'Name': 'resource-id', 'Values': [instance_id]}])
        tags = response.get('Tags', [])

        tag_exists = any(tag['Key'] == tag_to_update for tag in tags)
        if not tag_exists:
            print(f"La etiqueta '{tag_to_update}' no existe para la instancia '{instance_id}'. Creándola...")
            ec2.create_tags(Resources=[instance_id], Tags=[{'Key': tag_to_update, 'Value': new_tag_value}])
        else:
            print(f"La etiqueta '{tag_to_update}' ya existe para la instancia '{instance_id}'. Actualizando su valor...")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python script.py <tag_to_update> <new_tag_value> <region>")
        sys.exit(1)

    tag_to_update = sys.argv[1]
    new_tag_value = sys.argv[2]
    region = sys.argv[3]

    try:
        with open("Irlanda.txt", "r") as f:
            instance_ids = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Archivo 'Irlanda.txt' no encontrado.")
        sys.exit(1)

    # Validar los Instance IDs
    ec2 = boto3.client('ec2', region_name=region)
    valid_instance_ids, invalid_instance_ids = validate_instance_ids(ec2, instance_ids)

    if invalid_instance_ids:
        print("Los siguientes Instance IDs no son válidos:")
        for invalid_id in invalid_instance_ids:
            print(invalid_id)
    else:
        # Actualizar etiquetas para instancias válidas
        update_tag_value(tag_to_update, new_tag_value, region, valid_instance_ids)
