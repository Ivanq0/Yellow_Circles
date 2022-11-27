# -*- coding: utf-8 -*-


################################################################################
## Form generated from reading UI file 'UIWVvtfR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5.QtCore import QSize, QMetaObject, QCoreApplication, QRect
from PyQt5.QtWidgets import QSizePolicy, QWidget, QStatusBar, QPushButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 692)
        MainWindow.setMaximumSize(QSize(800, 692))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(800, 672))
        self.centralwidget.setMaximumSize(QSize(800, 672))
        self.centralwidget.setSizeIncrement(QSize(800, 672))
        self.centralwidget.setBaseSize(QSize(800, 672))
        self.add_circle = QPushButton(self.centralwidget)
        self.add_circle.setObjectName(u"add_circle")
        self.add_circle.setGeometry(QRect(260, 620, 241, 41))
        self.add_circle.setStyleSheet(u"font: 12pt \"Yu Gothic UI\";\n"
                                      "background-color: rgb(255, 178, 83);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u0416\u0451\u043b\u0442\u044b\u0435 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438",
                                                             None))
        self.add_circle.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi
