import boto3
import sys
import configparser

def add_tags_to_security_groups(region_name):
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

    # Leer el nombre de los grupos de seguridad desde el archivo security_groups.txt
    try:
        with open("security_groups.txt", "r") as f:
            security_group_ids = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Archivo 'security_groups.txt' no encontrado.")
        sys.exit(1)

    tag_value = 'connectors-test'  # Reemplazar esto con el valor que necesitas para 'product'

    for sg_id in security_group_ids:
        # Nuevas etiquetas para cada grupo de seguridad
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
            #{'Key': 'Name', 'Value': sg_id}
        ]

        # Agregar las nuevas etiquetas a cada grupo de seguridad
        response = ec2_client.create_tags(
            Resources=[sg_id],
            Tags=new_tags
        )

        print(f"Etiquetas agregadas al grupo de seguridad '{sg_id}': {response}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    add_tags_to_security_groups(region_name)
