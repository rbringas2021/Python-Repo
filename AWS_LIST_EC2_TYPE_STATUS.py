import boto3
import sys

sys.stdout = open("instances_type.txt", "w")

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
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                instance_name = tag["Value"]
        instances_info.append((instance_name, instance_type, instance_state))

# Ordena la lista por nombre de instancia en orden alfabético
instances_info.sort()

# Imprime la información de instancia en el archivo de texto
for instance_info in instances_info:
    print("{:40}, {:20}, {:10}".format(*instance_info))

sys.stdout.close()

#__END__.