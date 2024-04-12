import boto3
import sys
import configparser

def add_tags_to_kinesis_stream(region_name, stream_name):
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

    # Crea un cliente Kinesis
    kinesis = session.client('kinesis')

    # Lista de TAGS a agregar
    tags = {
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
        'Name': stream_name  # Agregar 'Name' con el nombre del Data Stream
    }

    # Agregar las TAGS al Data Stream
    kinesis.add_tags_to_stream(
        StreamName=stream_name,
        Tags=tags
    )

    print(f"Se agregaron las etiquetas al Data Stream '{stream_name}' en la región '{region_name}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <region_name> <stream_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    stream_name = sys.argv[2]
    add_tags_to_kinesis_stream(region_name, stream_name)
