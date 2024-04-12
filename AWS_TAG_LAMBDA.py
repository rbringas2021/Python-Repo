import boto3
import sys
import configparser

def add_tags_to_lambda_functions(region_name):
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

    # Crear un cliente Lambda
    lambda_client = session.client('lambda')

    # Leer el nombre de las funciones desde el archivo Function.txt
    try:
        with open("Function.txt", "r") as f:
            functions = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Archivo 'Function.txt' no encontrado.")
        sys.exit(1)

    for function in functions:
        # Etiquetas comunes para cada función Lambda, incluyendo 'Name'
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
            'Name': function  # Agregar 'Name' con el nombre de la función
        }

        # Agregar las etiquetas a cada función Lambda
        response = lambda_client.tag_resource(
            Resource=lambda_client.get_function(FunctionName=function)['Configuration']['FunctionArn'],
            Tags=common_tags
        )

        print(f"Etiquetas agregadas a la función Lambda '{function}': {response}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    add_tags_to_lambda_functions(region_name)
