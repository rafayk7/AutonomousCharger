import serial

class ArduinoConnection:
    def __init__(self, port):
        self.serial = serial.Serial(port)
        self.baud_rate = None

    def send(self, message):
        self.serial.write(message)
        

# Stepper for up/down, and servo for M1
arduino_one_name = ""

# Servo for M2 and M3, and button pressing
arduino_two_name = ""

ar1_serial = serial.Serial(arduino_one_name)
ar2_serial = serial.Serial(arduino_two_name)



