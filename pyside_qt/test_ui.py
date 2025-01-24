import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from ui_view_ui import Ui_MainWindow


class MyWindow(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
 
 
if __name__ == '__main__':
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec()
