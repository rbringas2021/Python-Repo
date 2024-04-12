import boto3
import sys
import configparser

def get_instance_name(instance_id, ec2_client):
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance_name = "N/A"
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
                    break
    return instance_name

def add_tags_to_eni(eni_id, ec2_client, new_tags):
    try:
        response = ec2_client.create_tags(Resources=[eni_id], Tags=new_tags)
        print(f"Etiquetas agregadas a la ENI '{eni_id}': {response}")
    except Exception as e:
        print(f"Error al agregar etiquetas a la ENI '{eni_id}': {str(e)}")

def get_eni_by_ip(ip_address, region_name, aws_access_key, aws_secret_key, new_tags):
    # Crear un cliente de EC2
    ec2_client = boto3.client('ec2', region_name=region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    # Obtener información sobre las ENIs asociadas a la dirección IP
    response = ec2_client.describe_network_interfaces(Filters=[{'Name': 'association.public-ip', 'Values': [ip_address]}])

    # Verificar si se encontraron ENIs asociadas a la dirección IP
    if not response['NetworkInterfaces']:
        print(f"No se encontraron ENIs asociadas a la dirección IP '{ip_address}'.")
        return

    # Mostrar el nombre de la ENI y el nombre de la instancia asociada
    for interface in response['NetworkInterfaces']:
        interface_id = interface['NetworkInterfaceId']
        instance_id = interface.get('Attachment', {}).get('InstanceId', 'N/A')
        instance_name = get_instance_name(instance_id, ec2_client)
        print(f"Nombre de la ENI: {instance_name}, Nombre de la instancia asociada: {instance_name}")
        tags_with_name = new_tags + [{'Key': 'Name', 'Value': instance_name}]
        add_tags_to_eni(interface_id, ec2_client, tags_with_name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]

    config = configparser.ConfigParser()
    config.read('/Users/rbringas/.aws/credentials')
    aws_access_key = config.get('default', 'aws_access_key_id')
    aws_secret_key = config.get('default', 'aws_secret_access_key')

    try:
        with open("eip_Addresses.txt", "r") as f:
            ip_addresses = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Archivo 'eip_Addresses.txt' no encontrado.")
        exit()

    new_tags = [
        {'Key': 'asset', 'Value': 'connector'},
        {'Key': 'product', 'Value': 'Connectors Commons'},
        {'Key': 'Product', 'Value': 'Connectors Commons'},
        {'Key': 'PRODUCT', 'Value': 'Connectors Commons'},
        {'Key': 'component', 'Value': 'connectors-test'},
        {'Key': 'service', 'Value': 'connectors-test-service'},
        {'Key': 'service-short', 'Value': 'connectors-test-service'},
        {'Key': 'long_running', 'Value': '2025/12/01'},
        {'Key': 'backup', 'Value': 'yes'},
        {'Key': 'Backup', 'Value': 'yes'},
        {'Key': 'PROJECT', 'Value': 'connectors-test'},
        {'Key': 'REPO', 'Value': 'tf-connectors-test'},
        {'Key': 'ROLE', 'Value': 'connectors-test'},
        {'Key': 'SERVICE', 'Value': 'connectors-test'},
        {'Key': 'ENV', 'Value': 'Development'},
        {'Key': 'u_gus_team_id', 'Value': 'a00EE00000YbxIT'},
        {'Key': 'u_customer_data', 'Value': 'Not Applicable'},
        {'Key': 'p_confidentiality', 'Value': 'Internal'},
        {'Key': 'u_service_tier', 'Value': '3'},
        {'Key': 'u_scan_eligibility', 'Value': 'Not Applicable'},
        {'Key': 'OWNER', 'Value': 'a00EE00000YbxIT'},
    ]

    for ip_address in ip_addresses:
        print(f"Buscando ENIs asociadas a la dirección IP: {ip_address}")
        get_eni_by_ip(ip_address, region_name, aws_access_key, aws_secret_key, new_tags)
