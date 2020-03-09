from ui import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
from comm import ArduinoConnection, SSHConnection

port = "/dev/ttyUSB0"
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

    window.forwardButton.clicked.connect(lambda: CommAPI.send('w'))
    window.backwardButton.clicked.connect(lambda: CommAPI.send('s'))

    window.leftButton.clicked.connect(lambda: CommAPI.send('a'))
    window.rightButton.clicked.connect(lambda: CommAPI.send('d'))

    window.leftRotateButton.clicked.connect(lambda: CommAPI.send('l'))
    window.rightRotateButton.clicked.connect(lambda: CommAPI.send('r'))

    window.upButton.clicked.connect(lambda: CommAPI.send('u'))
    window.downButton.clicked.connect(lambda: CommAPI.send('j'))

    window.set_port_button.clicked.connect(set_port)
    window.stopButton.clicked.connect(lambda: CommAPI.send('p'))

    window.show()
    sys.exit(app.exec_())





