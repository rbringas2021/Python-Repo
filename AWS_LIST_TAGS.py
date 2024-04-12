import boto3
import sys

sys.stdout = open("instances_tags.txt", "w")

# Crea un cliente EC2
ec2 = boto3.client('ec2', region_name='us-east-1')

# Utiliza el cliente para obtener información sobre las instancias
response = ec2.describe_instances()

# Crea una lista vacía para almacenar información de instancia
instances_info = []

# Recorre las instancias y las agrega a la lista
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_name = ""
        instance_type = instance["InstanceType"]
        instance_state = instance["State"]["Name"]
        instance_tags = []  # Crear una lista para almacenar las TAGs de la instancia
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                instance_name = tag["Value"]
            else:
                instance_tags.append(tag['Key'] + ': ' + tag['Value'])  # Agregar la TAG a la lista
        instances_info.append((instance_name, instance_type, instance_state, instance_tags)) # Agregar la lista de TAGs a la tupla

# Ordena la lista por nombre de instancia en orden alfabético
instances_info.sort()

# Imprime la información de instancia en el archivo de texto
for instance_info in instances_info:
    tags = ', '.join(instance_info[3])  # Convertir la lista de TAGs en un string separado por comas
    print("{:40}, {:20}, {:10}, {}".format(instance_info[0], instance_info[1], instance_info[2], tags))

sys.stdout.close()

#__END__.