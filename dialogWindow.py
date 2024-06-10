from PySide6.QtWidgets import QDialog
#from ui_mainWindow import Ui_Widget
from ui_dialogWindow import Ui_Dialog

class DialogWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
