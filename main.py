import sys
from PySide6.QtWidgets import QApplication, QWidget
from mainWindow import Widget

#     pyside6-uic form.ui -o ui_form.py

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
