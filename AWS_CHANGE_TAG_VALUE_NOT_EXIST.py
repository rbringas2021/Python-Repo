import boto3
import sys
import configparser
import os
from botocore.exceptions import ClientError

# Definir la función para obtener las credenciales de AWS
def get_aws_credentials():
    # Obtener las credenciales de AWS
    config = configparser.ConfigParser()
    config.read(os.path.expanduser("~/.aws/credentials"))

    aws_access_key = config.get('default', 'aws_access_key_id')
    aws_secret_key = config.get('default', 'aws_secret_access_key')

    return aws_access_key, aws_secret_key

# Definir la función para actualizar la etiqueta del bucket
def update_bucket_tag(bucket_name, tag_to_update, new_tag_value):
    # Obtener las credenciales de AWS
    aws_access_key, aws_secret_key = get_aws_credentials()

    # Crear un cliente S3
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key,
                      aws_secret_access_key=aws_secret_key)

    try:
        # Obtener las etiquetas actuales del bucket
        response = s3.get_bucket_tagging(Bucket=bucket_name)
        existing_tags = response['TagSet']
        
        # Verificar si la etiqueta a actualizar ya existe
        tag_exists = any(tag['Key'] == tag_to_update for tag in existing_tags)

        if tag_exists:
            # Actualizar el valor de la etiqueta existente
            existing_tags = [{'Key': tag['Key'], 'Value': new_tag_value} if tag['Key'] == tag_to_update else tag for tag in existing_tags]
        else:
            # Agregar la nueva etiqueta
            existing_tags.append({'Key': tag_to_update, 'Value': new_tag_value})

        # Actualizar la etiqueta del bucket
        s3.put_bucket_tagging(
            Bucket=bucket_name,
            Tagging={'TagSet': existing_tags}
        )

        print(f"Etiqueta '{tag_to_update}' actualizada para el bucket '{bucket_name}' a '{new_tag_value}'.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchTagSet':
            print(f"El bucket '{bucket_name}' no tiene etiquetas.")
            # Código para crear nuevas etiquetas en el bucket si no existen
            s3.put_bucket_tagging(
                Bucket=bucket_name,
                Tagging={'TagSet': [{'Key': tag_to_update, 'Value': new_tag_value}]}
            )
            print(f"Se han creado etiquetas para el bucket '{bucket_name}'.")
        else:
            print(f"Error al actualizar las etiquetas del bucket '{bucket_name}': {str(e)}")

# Resto del código...

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <tag_to_update> <new_tag_value>")
        sys.exit(1)

    tag_to_update = sys.argv[1]
    new_tag_value = sys.argv[2]

    try:
        with open("Bucket.txt", "r") as f:
            bucket_names = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Archivo 'Bucket.txt' no encontrado.")
        sys.exit(1)

    # Crear un cliente S3
    s3 = boto3.client('s3')

    # Iterar sobre los nombres de los buckets y actualizar las etiquetas
    for bucket_name in bucket_names:
        update_bucket_tag(bucket_name, tag_to_update, new_tag_value)
