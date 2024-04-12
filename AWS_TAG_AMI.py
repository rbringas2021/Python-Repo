import boto3
import sys
import configparser

def add_tags_to_amis(region_name):
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

    # Leer el nombre de las AMIs desde el archivo AMI.txt
    try:
        with open("AMI.txt", "r") as f:
            ami_names = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Archivo 'AMI.txt' no encontrado.")
        sys.exit(1)

    tag_value = 'connectors-test'  # Reemplazar esto con el valor que necesitas para 'product'

    for ami_name in ami_names:
        # Obtener el ID de la AMI basado en el nombre
        images = ec2_client.describe_images(Filters=[{'Name': 'tag:Name', 'Values': [ami_name]}])
        if not images['Images']:
            print(f"Error: No se encontró la AMI con el nombre '{ami_name}'.")
            continue

        image_id = images['Images'][0]['ImageId']

        # Nuevas etiquetas para cada AMI
        new_tags = [
            {'Key': 'asset', 'Value': 'connector'},
            {'Key': 'product', 'Value': tag_value},
            {'Key': 'Product', 'Value': tag_value},
            {'Key': 'PRODUCT', 'Value': tag_value},
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
            {'Key': 'u_scan_eligibility', 'Value': 'Applicable'},
            {'Key': 'OWNER', 'Value': 'a00EE00000YbxIT'},
            {'Key': 'Name', 'Value': ami_name}
        ]

        # Agregar las nuevas etiquetas a cada AMI
        response = ec2_client.create_tags(
            Resources=[image_id],
            Tags=new_tags
        )

        print(f"Etiquetas agregadas a la AMI '{image_id}' (nombre: {ami_name}): {response}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    add_tags_to_amis(region_name)