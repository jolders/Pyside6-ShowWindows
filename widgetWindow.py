from PySide6.QtWidgets import QWidget
from ui_widgetWindow import Ui_Form

class WidgetWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
