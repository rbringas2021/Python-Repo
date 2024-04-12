import boto3

# Establece la región de AWS que deseas utilizar
region = 'us-east-1'

# Crea una instancia de cliente EC2
ec2 = boto3.client('ec2', region_name=region)

# Solicita al usuario que ingrese el nombre de la instancia
instance_name = input("Ingresa el nombre de la instancia EC2 que deseas detener: ")

# Obtiene información sobre todas las instancias con el nombre proporcionado
response = ec2.describe_instances(
    Filters=[
        {'Name': 'tag:Name', 'Values': [instance_name]}
    ]
)

# Verifica que se encontró al menos una instancia con el nombre proporcionado
if len(response['Reservations']) == 0:
    print('No se encontró ninguna instancia con el nombre {}.'.format(instance_name))
    exit()

# Obtiene la ID de la instancia
instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']

# Detiene la instancia
ec2.stop_instances(InstanceIds=[instance_id])

print('La instancia {} se detuvo correctamente.'.format(instance_name))

#__END__.