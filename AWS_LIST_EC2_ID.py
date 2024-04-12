import boto3
import sys

def get_instances_by_region(region):
    # Crear un cliente EC2 en la región especificada
    ec2 = boto3.client('ec2', region_name=region)

    # Utilizar el cliente para obtener información sobre las instancias
    response = ec2.describe_instances()

    # Diccionario con los nombres y IDs de las instancias
    instances = {}

    # Recorrer las instancias y almacenar sus nombres e IDs en el diccionario
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_name = "NoName"  # Si no tiene nombre, se asigna "NoName"
            for tag in instance.get("Tags", []):
                if tag["Key"] == "Name":
                    instance_name = tag["Value"]
                    break
            instances[instance_name] = instance["InstanceId"]

    # Imprimir el nombre y la ID de las instancias
    print("Nombre de la Instancia\tID de la Instancia")
    print("----------------------------\t--------------------")
    for name, instance_id in instances.items():
        print(f"{name}\t\t\t{instance_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <region>")
        sys.exit(1)

    region = sys.argv[1]
    get_instances_by_region(region)
