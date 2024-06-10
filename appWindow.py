from PySide6.QtWidgets import QMainWindow
#from ui_mainWindow import Ui_Widget
from ui_appWindow import Ui_MainWindow

class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_Widget()
        self.setupUi(self)


