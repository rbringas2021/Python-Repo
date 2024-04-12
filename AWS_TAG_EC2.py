import boto3
import sys
import configparser

def add_tags_to_ec2_instances(region_name):
    # Leer las credenciales de AWS desde el archivo
    config = configparser.ConfigParser()
    config.read('/Users/rbringas/.aws/credentials')
    aws_access_key = config.get('default', 'aws_access_key_id')
    aws_secret_key = config.get('default', 'aws_secret_access_key')

    # Crear una sesión de boto3
    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region_name
    )

    # Crear un cliente EC2
    ec2_client = session.client('ec2')

    # Leer el nombre de las instancias EC2 desde el archivo Instance.txt
    try:
        with open("Instance.txt", "r") as f:
            instance_names = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Archivo 'Instance.txt' no encontrado.")
        sys.exit(1)

    tag_value = 'connectors-test'  # Reemplazar esto con el valor que necesitas para 'product'

    for instance_name in instance_names:
        # Obtener el ID de la instancia basado en el nombre
        instances = ec2_client.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': [instance_name]}])
        if not instances['Reservations']:
            print(f"Error: No se encontró la instancia con el nombre '{instance_name}'.")
            continue

        instance_id = instances['Reservations'][0]['Instances'][0]['InstanceId']

        # Nuevas etiquetas para cada instancia EC2
        new_tags = [
    {'Key': 'asset', 'Value': 'connector'},
            {'Key': 'product', 'Value': 'Connectors Commons'},
            {'Key': 'Product', 'Value': 'Connectors Commons'},
            {'Key': 'PRODUCT', 'Value': 'Connectors Commons'},
            {'Key': 'component', 'Value': 'connectors-test'},
            {'Key': 'service', 'Value': f'{tag_value}-connectors-test-service'},
            {'Key': 'service-short', 'Value': 'connectors-test-service'},
            {'Key': 'long_running', 'Value': '2025/12/01'},
            {'Key': 'backup', 'Value': 'yes'},
            {'Key': 'Backup', 'Value': 'yes'},
            {'Key': 'PROJECT', 'Value': tag_value},
            {'Key': 'REPO', 'Value': 'tf-connectors-test'},
            {'Key': 'ROLE', 'Value': tag_value},
            {'Key': 'SERVICE', 'Value': tag_value},
            {'Key': 'ENV', 'Value': 'Development'},
            {'Key': 'u_gus_team_id', 'Value': 'a00EE00000YbxIT'},
            {'Key': 'u_customer_data', 'Value': 'Not Applicable'},
            {'Key': 'p_confidentiality', 'Value': 'Internal'},
            {'Key': 'u_service_tier', 'Value': '3'},
            {'Key': 'u_scan_eligibility', 'Value': 'Not Applicable'},
            {'Key': 'OWNER', 'Value': 'a00EE00000YbxIT'},
            {'Key': 'Name', 'Value': instance_name}
        ]

        # Agregar las nuevas etiquetas a cada instancia EC2
        response = ec2_client.create_tags(
            Resources=[instance_id],
            Tags=new_tags
        )

        print(f"Etiquetas agregadas a la instancia EC2 '{instance_id}' (nombre: {instance_name}): {response}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    add_tags_to_ec2_instances(region_name)
