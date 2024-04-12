import boto3
import sys

def list_dynamodb_tables(region_name):
    # Crear una sesión de boto3
    session = boto3.Session(region_name=region_name)

    # Crear un cliente DynamoDB
    dynamodb = session.client('dynamodb')

    # Obtener una lista de tablas DynamoDB
    response = dynamodb.list_tables()
    tables = response['TableNames']

    print("Lista de tablas DynamoDB:")
    for table in tables:
        print(table)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    list_dynamodb_tables(region_name)

#__END__