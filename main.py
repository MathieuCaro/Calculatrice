import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QtAligment

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculatrice")
        self.setGeometry(700,300,500,500)
        
        label = QLabel("Hello",self)
        label.setFont(QFont("Arial",30))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: blue;"
                            "background-color:red;"
                            "font-weight:bold;"
                            "font-style:italic;")
        label.setAligment
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
    