from ui import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
from comm import ArduinoConnection, SSHConnection

port = "/dev/tty.HC-05-SPPDev"
baud_rate = 38400 
config_path = "/Users/rafaykalim/University-BS/praxis_III/aruco/keys.txt"


# CommAPI = ArduinoConnection(port, baud_rate=baud_rate)
CommAPI = SSHConnection(config_path, port)
CommAPI.get_available_ports()

app = QApplication(sys.argv)
window = MainWindow()

def set_port():
    new_port = window.port_textbox.text().strip()
    CommAPI.port = new_port

    print("Port changed to {}".format(new_port))

if __name__ == '__main__':

    window.forwardButton.clicked.connect(lambda: CommAPI.send(0))
    window.backwardButton.clicked.connect(lambda: CommAPI.send(1))

    window.leftButton.clicked.connect(lambda: CommAPI.send(2))
    window.rightButton.clicked.connect(lambda: CommAPI.send(3))

    window.leftRotateButton.clicked.connect(lambda: CommAPI.send(4))
    window.rightRotateButton.clicked.connect(lambda: CommAPI.send(5))

    window.upButton.clicked.connect(lambda: CommAPI.send(6))
    window.downButton.clicked.connect(lambda: CommAPI.send(7))

    window.set_port_button.clicked.connect(set_port)

    window.show()
    sys.exit(app.exec_())





