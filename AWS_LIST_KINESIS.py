import boto3
import sys
import configparser

def list_kinesis_streams(region_name):
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

    sys.stdout = open("kinesis.txt", "w")

    # Crea un cliente Kinesis
    kinesis = session.client('kinesis')

    # Obtiene una lista de nombres de los streams de Kinesis
    response = kinesis.list_streams()

    # Imprime los nombres de los streams
    for stream_name in response['StreamNames']:
        print(stream_name)

    # Cierra el archivo de salida
    sys.stdout.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    list_kinesis_streams(region_name)

    #__END__.