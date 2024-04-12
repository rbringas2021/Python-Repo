import boto3
import sys

def add_tags_to_load_balancers(region_name):
    # Crear una sesión de boto3
    session = boto3.Session(region_name=region_name)

    # Crear un cliente ELB
    elb = session.client('elbv2')

    # Obtener una lista de load balancers
    response = elb.describe_load_balancers()
    load_balancers = response['LoadBalancers']

    # Etiquetas comunes para cada load balancer
    common_tags = [
        {'Key': 'u_gus_team_id', 'Value': 'a00EE00000YbxIT'},
        {'Key': 'u_customer_data', 'Value': 'Not Applicable'},
        {'Key': 'p_confidentiality', 'Value': 'Internal'},
        {'Key': 'u_service_tier', 'Value': '3'},
        {'Key': 'u_scan_eligibility', 'Value': 'Applicable'},
        {'Key': 'asset', 'Value': 'connector'},
        {'Key': 'product', 'Value': 'connectors-test'},
        {'Key': 'component', 'Value': 'connectors-test'},
        {'Key': 'service', 'Value': 'connectivity-connectors-test-service'},
        {'Key': 'service-short', 'Value': 'connectors-test-service'},
        {'Key': 'long_running', 'Value': '2025/12/01'},
        {'Key': 'backup', 'Value': 'yes'},
        {'Key': 'Product', 'Value': 'connectors-test'},
        {'Key': 'PROJECT', 'Value': 'connectors-test'},
        {'Key': 'REPO', 'Value': 'tf-connectors-test'},
        {'Key': 'ROLE', 'Value': 'connectors-test'},
        {'Key': 'SERVICE', 'Value': 'connectors-test'},
        {'Key': 'ENV', 'Value': 'Development'},
        {'Key': 'OWNER', 'Value': 'a00EE00000YbxIT'}
    ]

    for lb in load_balancers:
        lb_arn = lb['LoadBalancerArn']
        # Agregar las etiquetas a cada load balancer
        response = elb.add_tags(ResourceArns=[lb_arn], Tags=common_tags)

        print(f"Etiquetas agregadas al Load Balancer '{lb_arn}': {response}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    add_tags_to_load_balancers(region_name)

#__END__.