from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication)
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

        Layout = QGridLayout()
        self.setLayout(Layout)

        Layout.addWidget(self.forwardButton,0, 0, 1, 3)
        Layout.addWidget(self.backwardButton,2, 0, 1, 3)

        Layout.addWidget(self.leftButton,1, 0, 1, 1)
        Layout.addWidget(self.rightButton,1, 1, 1, 1)

        Layout.addWidget(self.leftRotateButton,3, 0, 1, 1)
        Layout.addWidget(self.rightRotateButton,3, 1, 1, 1)

        Layout.addWidget(self.upButton,4, 0, 1, 1)
        Layout.addWidget(self.downButton,4, 1, 1, 1)
        
        self.setWindowTitle('Arm Control')