import boto3
import sys

def add_tags_to_rds(region_name):
    # Crear una sesión de boto3
    session = boto3.Session(region_name=region_name)

    # Crear un cliente RDS
    rds = session.client('rds')

    # Obtener la lista de nombres de bases de datos RDS en la región actual
    response = rds.describe_db_instances()
    db_instances = response['DBInstances']

    # Verificar si alguna etiqueta falta y agregarla a las etiquetas comunes
    desired_tags = {
        "u_gus_team_id": "a00EE00000YbxIT",
        "u_customer_data": "Not Applicable",
        "p_confidentiality": "Internal",
        "u_service_tier": "3",
        "u_scan_eligibility": "Applicable",
        "asset": "connector",
        "product": "connectors-test",
        "component": "connectors-test",
        "service": "connectivity-connectors-test-service",
        "service-short": "connectors-test-service",
        "long_running": "2025/12/01",
        "backup": "yes",
        "Product": "connectors-test",
        "PRODUCT": "connectors-test",
        "PROJECT": "connectors-test",
        "REPO": "tf-connectors-test",
        "ROLE": "connectors-test",
        "SERVICE": "connectors-test",
        "ENV": "Development",
        "OWNER": "a00EE00000YbxIT"  # Nueva etiqueta OWNER
    }

    for db_instance in db_instances:
        db_name = db_instance['DBInstanceIdentifier']
        # Etiquetas comunes para cada base de datos
        common_tags = [{'Key': key, 'Value': value} for key, value in desired_tags.items()]
        # Agregar el identificador único como el valor de la etiqueta 'Name'
        common_tags.append({'Key': 'Name', 'Value': db_name})

        # Crear las etiquetas
        response = rds.add_tags_to_resource(
            ResourceName=f'arn:aws:rds:{region_name}:480410955647:db:{db_name}',
            Tags=common_tags
        )

        print(f"Etiquetas agregadas a la base de datos RDS '{db_name}' en la región '{region_name}': {response}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    add_tags_to_rds(region_name)

#__END__.