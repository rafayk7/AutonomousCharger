from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QLineEdit)
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()        
        self.leftButton = QPushButton("Left")
        self.rightButton = QPushButton("Right")

        self.forwardButton = QPushButton("Forward")
        self.backwardButton = QPushButton("Backward")

        self.rightRotateButton = QPushButton("Rotate Left")
        self.leftRotateButton = QPushButton("Rotate Right")

        self.upButton = QPushButton("Up")
        self.downButton = QPushButton("Down")

        self.stopButton = QPushButton("STOP")


        self.port_textbox = QLineEdit(self)
        self.set_port_button = QPushButton("Set Port")

        Layout = QGridLayout()
        self.setLayout(Layout)

        Layout.addWidget(self.stopButton, 0, 0, 2, 3)
        Layout.addWidget(self.forwardButton,2, 0, 1, 3)
        Layout.addWidget(self.backwardButton,4, 0, 1, 3)

        Layout.addWidget(self.leftButton,3, 0, 1, 1)
        Layout.addWidget(self.rightButton,3, 1, 1, 1)

        Layout.addWidget(self.leftRotateButton,5, 0, 1, 1)
        Layout.addWidget(self.rightRotateButton,5, 1, 1, 1)

        Layout.addWidget(self.upButton,6, 0, 1, 1)
        Layout.addWidget(self.downButton,6, 1, 1, 1)

        Layout.addWidget(self.port_textbox,7, 0, 1, 3)
        Layout.addWidget(self.set_port_button,8, 0, 1, 3)

        
        self.setWindowTitle('Arm Control')