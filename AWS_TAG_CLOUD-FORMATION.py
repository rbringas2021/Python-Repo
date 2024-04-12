import boto3
import sys
import configparser

def add_tags_to_cloudformation_stack(region_name):
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

    # Crear un cliente CloudFormation
    cloudformation_client = session.client('cloudformation')

    # Leer el nombre de las pilas desde el archivo Stack.txt
    try:
        with open("Stack.txt", "r") as f:
            stacks = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Archivo 'Stack.txt' no encontrado.")
        sys.exit(1)

    for stack_name in stacks:
        # Etiquetas comunes para cada pila de CloudFormation, incluyendo 'Name'
        common_tags = [
            {'Key': 'u_gus_team_id', 'Value': 'a00EE00000YbxIT'},
            {'Key': 'u_customer_data', 'Value': 'Not Applicable'},
            {'Key': 'p_confidentiality', 'Value': 'Internal'},
            {'Key': 'u_service_tier', 'Value': '3'},
            {'Key': 'u_scan_eligibility', 'Value': 'Applicable'},
            {'Key': 'asset', 'Value': 'connector'},
            {'Key': 'product', 'Value': 'Connectors Commons'},
            {'Key': 'component', 'Value': 'connectors-test'},
            {'Key': 'service', 'Value': 'connectivity-connectors-test-service'},
            {'Key': 'service-short', 'Value': 'connectors-test-service'},
            {'Key': 'long_running', 'Value': '2025/12/01'},
            {'Key': 'backup', 'Value': 'yes'},
            {'Key': 'PRODUCT', 'Value': 'connectors-test'},
            {'Key': 'PROJECT', 'Value': 'connectors-test'},
            {'Key': 'REPO', 'Value': 'tf-connectors-test'},
            {'Key': 'ROLE', 'Value': 'connectors-test'},
            {'Key': 'SERVICE', 'Value': 'connectors-test'},
            {'Key': 'ENV', 'Value': 'Development'},
            {'Key': 'OWNER', 'Value': 'a00EE00000YbxIT'},
            {'Key': 'Name', 'Value': stack_name}  # Agregar 'Name' con el nombre de la pila
        ]

        # Obtener la configuración actual de la pila
        try:
            response = cloudformation_client.describe_stacks(
                StackName=stack_name
            )
            current_tags = response['Stacks'][0].get('Tags', [])
        except cloudformation_client.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'ValidationError' and 'does not exist' in e.response['Error']['Message']:
                print(f"La pila '{stack_name}' no existe.")
                continue
            else:
                raise

        # Agregar las etiquetas comunes a las actuales
        updated_tags = current_tags + common_tags

        # Actualizar las etiquetas de la pila
        cloudformation_client.update_stack(
            StackName=stack_name,
            UsePreviousTemplate=True,
            Tags=updated_tags
        )

        print(f"Etiquetas actualizadas para la pila '{stack_name}': {updated_tags}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    add_tags_to_cloudformation_stack(region_name)
