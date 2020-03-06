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
    def __init__(self, path_to_keys, port):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.data = []
        self.port = port

        with open(path_to_keys) as f:
            self.data = [x.split("=")[1].strip() for x in f.readlines()]
        
        self.server = self.data[0]
        self.username = self.data[1]
        self.password = self.data[2]

        # ssh.load_system_host_keys()
        self.ssh.connect(self.server, username=self.username,password=self.password)

    def get_available_ports(self):
        cmd_todev = "cd /dev/ && ls"

        _, ports, _ = self.ssh.exec_command(str(cmd_todev))

        with open("ports_on_pi.txt", "w+") as f:
            for line in ports.readlines():
                f.write(line)
        # _, ports, _ = self.ssh.exec_command(str(cmd_list))

        return

    def send(self, command):
        send_command = "python3 send_to_arduino.py prod {} {}".format(self.port, str(command).strip())
        print("Sent: {}".format(send_command))
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(str(send_command))

        # print(ssh_stdin)
        print("Received: {}".format(ssh_stdout.readlines()))
        # print(ssh_stderr)
    
# Make "test" prod to execute
