import serial

class ArduinoConnection:
    def __init__(self, port):
        self.serial = serial.Serial(port)
        self.baud_rate = None

    def send(self, message):
        self.serial.write(message)
