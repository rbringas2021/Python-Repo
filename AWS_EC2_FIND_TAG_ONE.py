import boto3
import sys

def update_u_service_tier(ec2):
    # Leer el archivo con los nombres de las instancias
    try:
        with open("Instance.txt", "r") as f:
            instance_names = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Archivo 'Instance.txt' no encontrado.")
        sys.exit(1)

    # Obtener información sobre todas las instancias EC2
    response = ec2.describe_instances()
    reservations = response['Reservations']

    for reservation in reservations:
        instances = reservation['Instances']
        for instance in instances:
            # Obtener el instance_id y el nombre de la instancia
            instance_id = instance['InstanceId']
            tags = instance.get('Tags', [])
            instance_name = None

            # Buscar el nombre de la instancia en las etiquetas
            for tag in tags:
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
                    break

            # Verificar si el nombre está en la lista de instancias
            if instance_name and instance_name in instance_names:
                # Actualizar la etiqueta 'u_service_tier' a 3 si existe
                for tag in tags:
                    if tag['Key'] == 'u_service_tier':
                        tag['Value'] = '3'
                        ec2.create_tags(Resources=[instance_id], Tags=[{'Key': 'u_service_tier', 'Value': '3'}])
                        print(f"Etiqueta 'u_service_tier' actualizada a '3' para la instancia '{instance_id}'.")

if __name__ == "__main__":
    # Crear un cliente EC2
    ec2 = boto3.client('ec2')

    update_u_service_tier(ec2)

#__END__.