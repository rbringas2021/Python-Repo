import boto3
import sys
import configparser

def add_tags_to_nat_gateways(region_name):
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

    # Leer el nombre de las NAT Gateways desde el archivo NatGateway.txt
    try:
        with open("NatGateway.txt", "r") as f:
            nat_gateways = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Archivo 'NatGateway.txt' no encontrado.")
        sys.exit(1)

    for nat_gateway in nat_gateways:
        # Etiquetas comunes para cada NAT Gateway, incluyendo 'Name'
        common_tags = {
            'u_gus_team_id': 'a00EE00000YbxIT',
            'u_customer_data': 'Not Applicable',
            'p_confidentiality': 'Internal',
            'u_service_tier': '3',
            'u_scan_eligibility': 'Applicable',
            'asset': 'connector',
            'product': 'Connectors Commons',
            'component': 'connectors-test',
            'service': 'connectivity-connectors-test-service',
            'service-short': 'connectors-test-service',
            'long_running': '2025/12/01',
            'backup': 'yes',
            'PRODUCT': 'connectors-test',
            'PROJECT': 'connectors-test',
            'REPO': 'tf-connectors-test',
            'ROLE': 'connectors-test',
            'SERVICE': 'connectors-test',
            'ENV': 'Development',
            'OWNER': 'a00EE00000YbxIT',
            'Name': nat_gateway  # Agregar 'Name' con el nombre del NAT Gateway
        }

        # Agregar las etiquetas a cada NAT Gateway
        response = ec2_client.create_tags(
            Resources=[nat_gateway],
            Tags=[{'Key': key, 'Value': value} for key, value in common_tags.items()]
        )

        print(f"Etiquetas agregadas al NAT Gateway '{nat_gateway}': {response}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    add_tags_to_nat_gateways(region_name)
