import boto3
import sys

# Leer el archivo con los nombres de los secretos
try:
    with open("Secrets.txt", "r") as f:
        secret_names = [line.strip() for line in f]
except FileNotFoundError:
    print("Error: Archivo 'Secrets.txt' no encontrado.")
    sys.exit(1)

# Crear un cliente de Secrets Manager
secrets_manager = boto3.client('secretsmanager', region_name='us-east-1')

for secret_name in secret_names:
    # Crear las etiquetas para cada secreto
    tags = [
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
        {'Key': 'Name', 'Value': secret_name}  # Agregar 'Name' con el nombre del secreto
    ]

    # Agregar las etiquetas al secreto
    response = secrets_manager.tag_resource(
        SecretId=secret_name,
        Tags=tags
    )

    print(f"Etiquetas agregadas al secreto '{secret_name}': {response}")

#__END__.
