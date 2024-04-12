import boto3
import sys
import configparser

def add_tags_to_kms_keys(region_name):
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

    # Crear un cliente KMS
    kms_client = session.client('kms')

    # Leer el nombre de los keys desde el archivo KMS.txt
    try:
        with open("KMS.txt", "r") as f:
            kms_keys = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Archivo 'KMS.txt' no encontrado.")
        sys.exit(1)

    for key_id in kms_keys:
        # Etiquetas comunes para cada key KMS, incluyendo 'Name'
        common_tags = [
            {'TagKey': 'u_gus_team_id', 'TagValue': 'a00EE00000YbxIT'},
            {'TagKey': 'u_customer_data', 'TagValue': 'Not Applicable'},
            {'TagKey': 'p_confidentiality', 'TagValue': 'Internal'},
            {'TagKey': 'u_service_tier', 'TagValue': '3'},
            {'TagKey': 'u_scan_eligibility', 'TagValue': 'Applicable'},
            {'TagKey': 'asset', 'TagValue': 'connector'},
            {'TagKey': 'product', 'TagValue': 'Connectors Commons'},
            {'TagKey': 'component', 'TagValue': 'connectors-test'},
            {'TagKey': 'service', 'TagValue': 'connectivity-connectors-test-service'},
            {'TagKey': 'service-short', 'TagValue': 'connectors-test-service'},
            {'TagKey': 'long_running', 'TagValue': '2025/12/01'},
            {'TagKey': 'backup', 'TagValue': 'yes'},
            {'TagKey': 'PRODUCT', 'TagValue': 'connectors-test'},
            {'TagKey': 'PROJECT', 'TagValue': 'connectors-test'},
            {'TagKey': 'REPO', 'TagValue': 'tf-connectors-test'},
            {'TagKey': 'ROLE', 'TagValue': 'connectors-test'},
            {'TagKey': 'SERVICE', 'TagValue': 'connectors-test'},
            {'TagKey': 'ENV', 'TagValue': 'Development'},
            {'TagKey': 'OWNER', 'TagValue': 'a00EE00000YbxIT'},
            {'TagKey': 'Name', 'TagValue': key_id}  # Agregar 'Name' con el ID del key
        ]

        # Agregar las etiquetas al key KMS
        response = kms_client.tag_resource(
            KeyId=key_id,
            Tags=common_tags
        )

        print(f"Etiquetas agregadas al key KMS '{key_id}': {response}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    add_tags_to_kms_keys(region_name)
