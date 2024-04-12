import boto3
import configparser

# Crear una sesión de boto3
config = configparser.ConfigParser()
config.read('/Users/rbringas/.aws/credentials')

aws_access_key = config.get('default', 'aws_access_key_id')
aws_secret_key = config.get('default', 'aws_secret_access_key')

# Cambiar la región a 'eu-west-1'
session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name='eu-west-1'
)

# Crear un cliente RDS
rds = session.client('rds')

# Leer el archivo RDS.txt
with open("RDS.txt", "r") as f:
    db_names = [line.strip() for line in f]

# Etiquetas comunes para todas las bases de datos
common_tags = [
    {'Key': 'u_gus_team_id', 'Value': 'a00EE00000YbxIT'},
    {'Key': 'u_customer_data', 'Value': 'Not Applicable'},
    {'Key': 'p_confidentiality', 'Value': 'Internal'},
    {'Key': 'u_service_tier', 'Value': '3'},  # Cambiado a '3'
    {'Key': 'u_scan_eligibility', 'Value': 'Applicable'},
    {'Key': 'asset', 'Value': 'connector'},
    {'Key': 'product', 'Value': 'connectors-test'},
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
    {'Key': 'OWNER', 'Value': 'a00EE00000YbxIT'}  # Nueva etiqueta OWNER
]

# Recorrer los nombres de las bases de datos y agregar etiquetas
for db_name in db_names:
    # Combinar etiquetas comunes con las específicas de cada base de datos
    tags = common_tags

    # Crear las etiquetas
    response = rds.add_tags_to_resource(
        ResourceName=f'arn:aws:rds:{session.region_name}:480410955647:db:{db_name}',
        Tags=tags
    )

    print(f"Etiquetas agregadas a la base de datos RDS '{db_name}': {response}")

# __END__