from ui import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
from comm import ArduinoConnection

port = "/dev/tty.HC-05-SPPDev"
baud_rate = 38400 

CommAPI = ArduinoConnection(port, baud_rate=baud_rate)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.forwardButton.clicked.connect(lambda: CommAPI.send(0))
    window.backwardButton.clicked.connect(lambda: CommAPI.send(1))

    window.leftButton.clicked.connect(lambda: CommAPI.send(2))
    window.rightButton.clicked.connect(lambda: CommAPI.send(3))

    window.leftRotateButton.clicked.connect(lambda: CommAPI.send(4))
    window.rightRotateButton.clicked.connect(lambda: CommAPI.send(5))

    window.upButton.clicked.connect(lambda: CommAPI.send(6))
    window.downButton.clicked.connect(lambda: CommAPI.send(7))


    window.show()
    sys.exit(app.exec_())

