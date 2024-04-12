import boto3
import configparser

# Crear una sesión de boto3
config = configparser.ConfigParser()
config.read('/Users/rbringas/.aws/credentials')

aws_access_key = config.get('default', 'aws_access_key_id')
aws_secret_key = config.get('default', 'aws_secret_access_key')

session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name='us-east-1'
)

# Crear un cliente S3
s3 = session.client('s3')

# Preguntar por el nombre del bucket
bucket_name = input("Ingrese el nombre del bucket: ")

# Verificar si existe el bucket
try:
    s3.head_bucket(Bucket=bucket_name)
except s3.exceptions.NoSuchBucket:
    # Crear el bucket
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-1'
        }
    )
    print(f"El bucket '{bucket_name}' ha sido creado.")

# Obtener una lista de objetos en el bucket
objects = s3.list_objects(Bucket=bucket_name)

# Verificar si existen objetos en el bucket
if 'Contents' in objects:
    object_keys = [obj['Key'] for obj in objects['Contents']]

    # Iterar sobre las claves de objeto
    for object_key in object_keys:
        # Crear las etiquetas
        response = s3.put_object_tagging(
            Bucket=bucket_name,
            Key=object_key,
            Tagging={
                'TagSet': [
                    {'Key': 'u_gus_team_id', 'Value': 'a00EE00000YbxIT'},
                    {'Key': 'u_customer_data', 'Value': 'Not Applicable'},
                    {'Key': 'p_confidentiality', 'Value': 'Internal'},
                    {'Key': 'u_service_tier', 'Value': 'Tier 3'},
                    {'Key': 'u_scan_eligibility', 'Value': 'Applicable'}
                ]
            }
        )

        print(f"Etiquetas agregadas al objeto '{object_key}' en el bucket '{bucket_name}': {response}")
else:
    # Crear un objeto llamado 'Test'
    s3.put_object(Bucket=bucket_name, Key='Test')
    print(f"El objeto 'Test' ha sido creado en el bucket '{bucket_name}'.")
    # Crear las etiquetas para el objeto 'Test'
    response = s3.put_object_tagging(
        Bucket=bucket_name,
        Key='Test',
        Tagging={
            'TagSet': [
                {'Key': 'u_gus_team_id', 'Value': 'a00EE00000YbxIT'},
                {'Key': 'u_customer_data', 'Value': 'Not Applicable'},
                {'Key': 'p_confidentiality', 'Value': 'Internal'},
                {'Key': 'u_service_tier', 'Value': 'Tier 3'},
                {'Key': 'u_scan_eligibility', 'Value': 'Applicable'}
            ]
        }
    )

    print(f"Etiquetas agregadas al objeto 'Test' en el bucket '{bucket_name}': {response}")

#__END__.