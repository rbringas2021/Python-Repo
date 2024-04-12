import boto3
import sys
import configparser

def list_redshift_clusters(region_name):
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

    sys.stdout = open("redshift.txt", "w")

    # Crea un cliente Redshift
    redshift = session.client('redshift')

    # Obtiene una lista de clústeres de Redshift
    response = redshift.describe_clusters()

    # Imprime los nombres de los clústeres
    for cluster in response['Clusters']:
        print(cluster['ClusterIdentifier'])

    # Cierra el archivo de salida
    sys.stdout.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    list_redshift_clusters(region_name)

#__END__.