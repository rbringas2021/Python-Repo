import boto3
import sys

def list_load_balancers(region_name):
    # Crear una sesión de boto3
    session = boto3.Session(region_name=region_name)

    # Crear un cliente ELB
    elb = session.client('elbv2')

    # Obtener una lista de load balancers
    response = elb.describe_load_balancers()
    load_balancers = response['LoadBalancers']

    print("Load Balancers en la región:")
    for lb in load_balancers:
        print(f"Load Balancer ARN: {lb['LoadBalancerArn']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <region_name>")
        sys.exit(1)

    region_name = sys.argv[1]
    list_load_balancers(region_name)

#__END__.