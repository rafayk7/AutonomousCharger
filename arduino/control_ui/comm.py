import serial
import paramiko

class ArduinoConnection:
    def __init__(self, port, baud_rate=None):
        self.serial = serial.Serial(port)
        self.baud_rate = baud_rate
        
        self.serial.baudrate = self.baud_rate

    def send(self, message):
        print(message)
        print(self.serial.name)
        print(self.serial.is_open)
        self.serial.write(message)

class SSHConnection:
    def __init__(self, path_to_keys):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.data = []

        with open(path_to_keys) as f:
            self.data = [x.split("=")[1].strip() for x in f.readlines()]
        
        self.server = self.data[0]
        self.username = self.data[1]
        self.password = self.data[2]

        # ssh.load_system_host_keys()
        self.ssh.connect(self.server, username=self.username,password=self.password)

    def send(self, command):
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(command)

        print(ssh_stdin)
        print(ssh_stdout.readlines())
        print(ssh_stderr)
    
config_path = "/Users/rafaykalim/University-BS/praxis_III/aruco/keys.txt"
conn = SSHConnection(config_path)
conn.send("ls")
