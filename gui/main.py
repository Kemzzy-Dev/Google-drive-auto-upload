import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto Upload")
        # 

        # Create the general layout
        self.mainDivision = QHBoxLayout()
        self.mainDivision.setGeometry(100, 100, 900, 800)

        # Create the left part
        self.leftDivision = QVBoxLayout()
        self.label = QLabel("Hello, World!")
        self.leftDivision.addWidget(self.label)
        self.mainDivision.addLayout(self.leftDivision)


        # Create the right part
        self.rightDivision = QVBoxLayout() 
        self.button = QPushButton("Click Me")
        self.rightDivision.addWidget(self.button)
        self.mainDivision.addLayout(self.rightDivision)

        self.setLayout(self.mainDivision)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())