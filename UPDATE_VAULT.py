import paramiko

# Crea un objeto de tipo 'SSHClient'
ssh = paramiko.SSHClient()

# Configura la política para agregar automáticamente la clave de host a la lista de claves conocidas
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Carga la clave privada (.pem)
mykey = paramiko.RSAKey.from_private_key_file('/Users/rbringas/AmazonPEMs/linux-sandbox.pem')

# Conecta al servidor remoto
ssh.connect('ec2-3-208-219-27.compute-1.amazonaws.com', username='ubuntu', pkey=mykey)

# Ejecuta los comandos que necesites
comandos = [
    'echo "INICIANDO SESIÓN EN EL SERVIDOR REMOTO"',
    'sudo su -',
    '',
    'echo "COMPROBANDO EL ESTADO DE VAULT"',
    'systemctl status vault',
    '',
    'echo "EXPORTANDO LA VARIABLE DE ENTORNO VAULT_ADDR"',
    'export VAULT_ADDR="https://vault.connectors.cloud"',
    '',
    'echo "INICIANDO SESIÓN EN VAULT"',
    'vault login s.iMOzTMiDriY2j3f0fVy1Q1iw',
    '',
    'echo "LISTANDO PEERS DE VAULT"',
    'vault operator raft list-peers',
    '',
    'echo "CREANDO UN SNAPSHOT DE VAULT"',
    'vault operator raft snapshot save snapshot-13-04-2023.snap',
    '',
    'echo "ACTUALIZANDO LOS PAQUETES DEL SISTEMA"',
    'apt update',
    '',
    'echo "LISTANDO PAQUETES ACTUALIZABLES"',
    'apt list --upgradable',
    '',
    'echo "DESCARGANDO LA NUEVA KEY PARA EL REPOSITORIO DE HASHICORP"',
    'curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -',
    '',
    'echo "LISTANDO PAQUETES ACTUALIZABLES"',
    'apt list --upgradable',
    ''
]

for comando in comandos:
    stdin, stdout, stderr = ssh.exec_command(comando)
    print(stdout.read().decode())
    print(stderr.read().decode())
    print('\n---------------------------\n')

# Cierra la conexión SSH
ssh.close()

#__END__.