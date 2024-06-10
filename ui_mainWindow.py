# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(536, 225)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 20, 291, 16))
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 40, 521, 181))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_mainWindow = QPushButton(self.groupBox)
        self.btn_mainWindow.setObjectName(u"btn_mainWindow")

        self.horizontalLayout.addWidget(self.btn_mainWindow)

        self.btn_dialogWindow = QPushButton(self.groupBox)
        self.btn_dialogWindow.setObjectName(u"btn_dialogWindow")

        self.horizontalLayout.addWidget(self.btn_dialogWindow)

        self.btn_widgetWindow = QPushButton(self.groupBox)
        self.btn_widgetWindow.setObjectName(u"btn_widgetWindow")

        self.horizontalLayout.addWidget(self.btn_widgetWindow)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"This is a Widget Window called : mainWindow.py", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"just a label", None))
        self.btn_mainWindow.setText(QCoreApplication.translate("Widget", u"Main Window", None))
        self.btn_dialogWindow.setText(QCoreApplication.translate("Widget", u"Dialog Window", None))
        self.btn_widgetWindow.setText(QCoreApplication.translate("Widget", u"Widget Window", None))
    # retranslateUi

