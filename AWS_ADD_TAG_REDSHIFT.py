import boto3
import sys
import configparser

def add_tags_to_redshift_cluster(region_name, cluster_name):
    # Crear una sesión de boto3
    config = configparser.ConfigParser()
    config.read('/Users/rbringas/.aws/credentials')

    aws_access_key = config.get('default', 'aws_access_key_id')
    aws_secret_key = config.get('default', 'aws_secret_access_key')

    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region_name
    )

    # Crea un cliente Redshift
    redshift = session.client('redshift')

    # Define las TAGS a agregar
    tags_to_add = {
        'u_gus_team_id': 'a00EE00000YbxIT',
        'u_customer_data': 'Not Applicable',
        'p_confidentiality': 'Internal',
        'u_service_tier': '3',
        'u_scan_eligibility': 'Applicable',
        'asset': 'connector',
        'product': 'connectors-test',
        'component': 'connectors-test',
        'service': 'connectivity-connectors-test-service',
        'service-short': 'connectors-test-service',
        'long_running': '2025/12/01',
        'backup': 'yes',
        'Product': 'connectors-test',
        'PROJECT': 'connectors-test',
        'REPO': 'tf-connectors-test',
        'ROLE': 'connectors-test',
        'SERVICE': 'connectors-test',
        'ENV': 'Development',
        'OWNER': 'a00EE00000YbxIT',
        'Name': cluster_name
    }

    # Agrega las TAGS al clúster
    tags = [{'Key': key, 'Value': value} for key, value in tags_to_add.items()]

    redshift.create_tags(
        ResourceName=f'arn:aws:redshift:{region_name}::cluster:{cluster_name}',
        Tags=tags
    )

    print(f'Tags added for Redshift cluster: {cluster_name}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <region_name> <cluster_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    cluster_name = sys.argv[2]
    add_tags_to_redshift_cluster(region_name, cluster_name)

#__END__.