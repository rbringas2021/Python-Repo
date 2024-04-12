import boto3
import sys

# Leer el archivo con los nombres de los buckets y sus tags
try:
    with open("PP", "r") as f:
        bucket_tags = [line.strip().split() for line in f]
except FileNotFoundError:
    print("Error: Archivo 'PP' no encontrado.")
    sys.exit(1)

# Crear un cliente S3
s3 = boto3.client('s3', region_name='us-east-1')

for bucket_name, tag_value in bucket_tags:
    # Crear las etiquetas para cada bucket
    tags = [
        {'Key': 'asset', 'Value': 'connector'},
        {'Key': 'product', 'Value': tag_value},
        {'Key': 'component', 'Value': 'connectors-test'},
        {'Key': 'service', 'Value': f'{tag_value}-connectors-test-service'},
        {'Key': 'service-short', 'Value': 'connectors-test-service'},
        {'Key': 'long_running', 'Value': '2025/12/01'},
        {'Key': 'backup', 'Value': 'yes'},
        {'Key': 'Product', 'Value': tag_value},
        {'Key': 'PRODUCT', 'Value': tag_value},
        {'Key': 'PROJECT', 'Value': tag_value},
        {'Key': 'REPO', 'Value': 'tf-connectors-test'},
        {'Key': 'ROLE', 'Value': tag_value},
        {'Key': 'SERVICE', 'Value': tag_value},
        {'Key': 'ENV', 'Value': 'Development'},
        {'Key': 'u_gus_team_id', 'Value': 'a00EE00000YbxIT'},
        {'Key': 'u_customer_data', 'Value': 'Not Applicable'},
        {'Key': 'p_confidentiality', 'Value': 'Internal'},
        {'Key': 'u_service_tier', 'Value': '3'},
        {'Key': 'u_scan_eligibility', 'Value': 'Applicable'},
        {'Key': 'OWNER', 'Value': 'a00EE00000YbxIT'},
        {'Key': 'Name', 'Value': bucket_name}  # Agregar la etiqueta 'Name' con el valor del nombre del bucket
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