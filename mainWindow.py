from PySide6.QtWidgets import QWidget
from ui_mainWindow import Ui_Widget

from appWindow import AppWindow
from dialogWindow import DialogWindow
from widgetWindow import WidgetWindow

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_Widget()
        self.setupUi(self)

        self.btn_mainWindow.clicked.connect(self.btn_mainWindow_clicked)
        self.btn_dialogWindow.clicked.connect(self.btn_dialogWindow_clicked)
        self.btn_widgetWindow.clicked.connect(self.btn_widgetWindow_clicked)

        # Reference the APPLICATION window AppWindow
        self.app_window = AppWindow()

        # Reference the DIALOG window DialogWindow
        self.dialog_window = DialogWindow()

        # Reference the application window appWindow
        self.widget_window = WidgetWindow()

    def btn_mainWindow_clicked(self):
        print("btn_mainWindow_clicked")
        self.app_window.show()

    def btn_dialogWindow_clicked(self):
        print("btn_dialogWindow_clicked")
        # self.dialog_window.exec() # Should be using open()
        self.dialog_window.open()

    def btn_widgetWindow_clicked(self):
        print("btn_widgetWindow_clicked")
        self.widget_window.show()
