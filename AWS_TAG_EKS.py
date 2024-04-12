import boto3
import sys
import configparser

def add_tags_to_eks_cluster(region_name, cluster_name):
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

    # Crear un cliente EKS
    eks_client = session.client('eks')

    # Obtener el ID del EKS Cluster
    response = eks_client.describe_cluster(
        name=cluster_name
    )

    cluster_arn = response['cluster']['arn']

    # Etiquetas comunes para el EKS Cluster, incluyendo 'Name'
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
        'Name': cluster_name  # Agregar 'Name' con el nombre del EKS Cluster
    }

    # Agregar las etiquetas al EKS Cluster
    response = eks_client.tag_resource(
        resourceArn=cluster_arn,
        tags=common_tags
    )

    print(f"Etiquetas agregadas al EKS Cluster '{cluster_name}': {response}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <region_name> <cluster_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    cluster_name = sys.argv[2]
    add_tags_to_eks_cluster(region_name, cluster_name)
