import boto3
import sys

def add_product_tag_to_ec2_instances(product_tag, product_value):
    # Crear un cliente EC2
    ec2 = boto3.client('ec2')

    # Leer el archivo con los nombres de las instancias
    try:
        with open("instance_change0.txt", "r") as f:
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
                # Crear la etiqueta especificada por el usuario si no existe
                product_tag_exists = any(tag['Key'] == product_tag for tag in tags)
                if not product_tag_exists:
                    # Agregar la etiqueta especificada por el usuario a la instancia
                    ec2.create_tags(Resources=[instance_id], Tags=[{'Key': product_tag, 'Value': product_value}])
                    print(f"Etiqueta '{product_tag}' agregada a la instancia '{instance_id}' con el valor '{product_value}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <product_tag> <product_value>")
        sys.exit(1)

    product_tag = sys.argv[1]
    product_value = sys.argv[2]

    add_product_tag_to_ec2_instances(product_tag, product_value)
