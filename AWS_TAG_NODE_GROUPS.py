import boto3
import sys
import configparser

def add_tags_to_node_groups(region_name, cluster_name):
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

    # Leer el nombre de los Node Groups desde el archivo NodeGroup.txt
    try:
        with open("NodeGroup.txt", "r") as f:
            node_groups = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Archivo 'NodeGroup.txt' no encontrado.")
        sys.exit(1)

    for node_group in node_groups:
        # Etiquetas comunes para cada Node Group, incluyendo 'Name'
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
            'Name': node_group  # Agregar 'Name' con el nombre del Node Group
        }

        # Obtener el identificador de recurso de EC2 asociado al Node Group
        response = eks_client.describe_nodegroup(
            clusterName=cluster_name,
            nodegroupName=node_group,
        )

        auto_scaling_group_name = response['nodegroup']['resources']['autoScalingGroups'][0]['name']

        # Crear un cliente Auto Scaling
        autoscaling_client = session.client('autoscaling')

        # Obtener el identificador de la instancia EC2 asociada al Auto Scaling Group
        response = autoscaling_client.describe_auto_scaling_groups(
            AutoScalingGroupNames=[auto_scaling_group_name]
        )

        ec2_instance_id = response['AutoScalingGroups'][0]['Instances'][0]['InstanceId']

        # Crear un cliente EC2
        ec2_client = session.client('ec2')

        # Agregar las etiquetas a la instancia EC2
        response = ec2_client.create_tags(
            Resources=[ec2_instance_id],
            Tags=[{'Key': key, 'Value': value} for key, value in common_tags.items()]
        )

        print(f"Etiquetas agregadas al Node Group '{node_group}': {response}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <region_name> <cluster_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    cluster_name = sys.argv[2]
    add_tags_to_node_groups(region_name, cluster_name)
