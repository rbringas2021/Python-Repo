import boto3
import sys

# Leer el archivo con los nombres de los buckets
try:
    with open("S3Objects.txt", "r") as f:
        bucket_names = [line.strip() for line in f]
except FileNotFoundError:
    print("Error: Archivo 'S3Objects.txt' no encontrado.")
    sys.exit(1)

# Crear un cliente S3
s3 = boto3.client('s3', region_name='us-east-1')

for bucket_name in bucket_names:
    # Crear las etiquetas para cada bucket
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
        {'Key': 'Name', 'Value': bucket_name}  # Agregar 'Name' con el nombre del bucket
    ]

    # Agregar las etiquetas al bucket
    response = s3.put_bucket_tagging(
        Bucket=bucket_name,
        Tagging={
            'TagSet': tags
        }
    )

    print(f"Etiquetas agregadas al bucket '{bucket_name}': {response}")

#__END__.
