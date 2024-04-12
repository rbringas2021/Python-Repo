import boto3
import sys
import configparser

def list_eni_without_product_tag(region_name, aws_access_key, aws_secret_key):
    # Crear un cliente de EC2
    ec2_client = boto3.client('ec2', region_name=region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    # Obtener todas las ENI
    response = ec2_client.describe_network_interfaces()

    # Iterar sobre las ENI y verificar si tienen la etiqueta 'product'
    for eni in response['NetworkInterfaces']:
        eni_id = eni['NetworkInterfaceId']
        instance_id = eni.get('Attachment', {}).get('InstanceId', 'N/A')
        
        # Obtener el nombre de la instancia asociada (si existe)
        instance_name = 'N/A'
        if instance_id != 'N/A':
            instance_name = 'N/A (Instance ID: ' + instance_id + ')'

        # Verificar si la ENI tiene la etiqueta 'product'
        tags = eni.get('TagSet', [])
        has_product_tag = any(tag['Key'] == 'product' for tag in tags)

        # Mostrar el ID de la ENI si no tiene la etiqueta 'product'
        if not has_product_tag:
            print(f"ENI ID sin etiqueta 'product': {eni_id} - Instancia asociada: {instance_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]

    # Leer las credenciales de AWS desde el archivo
    config = configparser.ConfigParser()
    config.read('/Users/rbringas/.aws/credentials')
    aws_access_key = config.get('default', 'aws_access_key_id')
    aws_secret_key = config.get('default', 'aws_secret_access_key')

    # Llamar a la función principal
    list_eni_without_product_tag(region_name, aws_access_key, aws_secret_key)
