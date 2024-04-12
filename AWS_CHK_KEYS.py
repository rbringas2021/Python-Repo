import boto3

def describe_key_pair(key_id, region):
    try:
        ec2 = boto3.client('ec2', region_name=region)
        response = ec2.describe_key_pairs(KeyNames=[key_id])
        key_info = response['KeyPairs'][0]
        print(f"La key '{key_id}' pertenece a: {key_info['KeyName']} en la región {region}")
    except Exception as e:
        print(f"No se pudo encontrar información para la key '{key_id}' en la región {region}: {str(e)}")

def main():
    file_path = 'pp'  # Path al archivo que contiene las keys pairs
    with open(file_path, 'r') as file:
        keys = file.readlines()
        for key in keys:
            key_id, region = key.strip().split(':')
            describe_key_pair(key_id, region)

if __name__ == "__main__":
    main()
