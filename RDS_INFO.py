import boto3
import configparser
import datetime

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

# Crear un cliente de Amazon RDS
rds_client = boto3.client('rds',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name='us-east-1'
)

# Obtener una lista de todas las bases de datos RDS
databases = rds_client.describe_db_instances()

# Imprimir el nombre, el tiempo de creación y el número de conexiones activas de cada base de datos
for database in databases['DBInstances']:
    db_instance_identifier = database['DBInstanceIdentifier']
    created_time = database['InstanceCreateTime'].strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nNombre de base de datos: {db_instance_identifier}")
    print(f"Tiempo de creación: {created_time}")

    cloudwatch_client = boto3.client('cloudwatch',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name='us-east-1'
    )

    end_time = datetime.datetime.utcnow()
    start_time = end_time - datetime.timedelta(seconds=300)

    result = cloudwatch_client.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'm1',
                'MetricStat': {
                    'Metric': {
                        'Namespace': 'AWS/RDS',
                        'MetricName': 'DatabaseConnections',
                        'Dimensions': [
                            {
                                'Name': 'DBInstanceIdentifier',
                                'Value': db_instance_identifier
                            },
                        ]
                    },
                    'Period': 300,
                    'Stat': 'Average'
                },
                'ReturnData': True
            },
        ],
        StartTime=start_time,
        EndTime=end_time
    )

    if result['MetricDataResults'][0]['Values']:
        active_connections = result['MetricDataResults'][0]['Values'][0]
        print(f"Número de conexiones activas: {active_connections}")
    else:
        print("No se encontraron valores para las conexiones activas.")

#__END__.


