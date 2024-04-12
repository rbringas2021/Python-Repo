import boto3

def add_owner_tag_to_ec2_instances():
    # Crear un cliente EC2
    ec2 = boto3.client('ec2')

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

            # Verificar si el nombre contiene "B2B"
            if instance_name and 'B2B' not in instance_name:
                # Crear la etiqueta 'OWNER' si no existe
                owner_tag_exists = any(tag['Key'] == 'OWNER' for tag in tags)
                if not owner_tag_exists:
                    # Agregar la etiqueta 'OWNER' a la instancia
                    ec2.create_tags(Resources=[instance_id], Tags=[{'Key': 'OWNER', 'Value': 'a00EE00000YbxIT'}])
                    print(f"Etiqueta 'OWNER' agregada a la instancia '{instance_id}'.")

if __name__ == "__main__":
    add_owner_tag_to_ec2_instances()

#__END__.