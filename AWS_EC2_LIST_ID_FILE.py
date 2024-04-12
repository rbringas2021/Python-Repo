import boto3

# Crear un cliente EC2
ec2 = boto3.client('ec2', region_name='us-east-1')

# Obtener todas las instancias
response = ec2.describe_instances()

# Crear un diccionario para almacenar los IDs de las instancias
instance_ids = {}

# Recorrer cada instancia y almacenar su ID en el diccionario
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        for tag in instance.get("Tags", []):
            if tag["Key"] == "Name":
                instance_name = tag["Value"]
                instance_id = instance["InstanceId"]
                instance_ids[instance_name] = instance_id

# Mostrar un cuadro con el nombre de la instancia y su ID
print("Nombre de la Instancia\t\tID de la Instancia")
print("----------------------------\t\t--------------------")
for instance_name, instance_id in instance_ids.items():
    print(f"{instance_name}\t\t\t{instance_id}")
