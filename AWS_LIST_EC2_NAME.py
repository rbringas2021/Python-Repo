import boto3
import sys

sys.stdout = open("instancias1.txt", "w")

# Crea un cliente EC2
ec2 = boto3.client('ec2', region_name='us-east-1')

# Utiliza el cliente para obtener información sobre las instancias
response = ec2.describe_instances()

# Recorre las instancias y las imprime
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                print(tag['Value'])

#__END__.