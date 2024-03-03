from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainmenu(object):
    def setupUi(self, mainmenu):
        mainmenu.setObjectName("mainmenu")
        mainmenu.resize(1440, 1024)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainmenu.sizePolicy().hasHeightForWidth())
        mainmenu.setSizePolicy(sizePolicy)
        mainmenu.setMinimumSize(QtCore.QSize(1440, 1024))
        mainmenu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        mainmenu.setFocusPolicy(QtCore.Qt.NoFocus)
        mainmenu.setAutoFillBackground(False)
        mainmenu.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/sprites/mainmenu.png);\n"
"border-position:center;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainmenu)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, 11, -1, 12)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(27)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 10, 0, 1, 1)
        self.Settings = QtWidgets.QPushButton(self.centralwidget)
        self.Settings.setMinimumSize(QtCore.QSize(329, 89))
        self.Settings.setMaximumSize(QtCore.QSize(329, 89))
        self.Settings.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/btsettings.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressbtsettings.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}")
        self.Settings.setText("")
        self.Settings.setObjectName("Settings")
        self.gridLayout.addWidget(self.Settings, 7, 0, 1, 1)
        self.Rules = QtWidgets.QPushButton(self.centralwidget)
        self.Rules.setMinimumSize(QtCore.QSize(329, 89))
        self.Rules.setMaximumSize(QtCore.QSize(329, 89))
        self.Rules.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/btrules.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressbtrules.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}")
        self.Rules.setText("")
        self.Rules.setObjectName("Rules")
        self.gridLayout.addWidget(self.Rules, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setMinimumSize(QtCore.QSize(329, 89))
        self.Exit.setMaximumSize(QtCore.QSize(329, 89))
        self.Exit.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/btexit.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressbtexit.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}")
        self.Exit.setText("")
        self.Exit.setObjectName("Exit")
        self.gridLayout.addWidget(self.Exit, 9, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setMinimumSize(QtCore.QSize(329, 89))
        self.Play.setMaximumSize(QtCore.QSize(329, 89))
        self.Play.setAutoFillBackground(False)
        self.Play.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/btplay.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressbtplay.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"")
        self.Play.setText("")
        self.Play.setObjectName("Play")
        self.gridLayout.addWidget(self.Play, 6, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 1)
        mainmenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainmenu)
        QtCore.QMetaObject.connectSlotsByName(mainmenu)

    def retranslateUi(self, mainmenu):
        _translate = QtCore.QCoreApplication.translate
        mainmenu.setWindowTitle(_translate("mainmenu", "Подушечки из котиков"))

class Ui_exit(object):
    def setupUi(self, exit):
        exit.setObjectName("exit")
        exit.resize(1440, 1024)
        exit.setMinimumSize(QtCore.QSize(1440, 1024))
        exit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        exit.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/sprites/exit.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(exit)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, 140, -1, 0)
        self.gridLayout.setHorizontalSpacing(80)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.yes = QtWidgets.QPushButton(self.centralwidget)
        self.yes.setMinimumSize(QtCore.QSize(144, 67))
        self.yes.setMaximumSize(QtCore.QSize(144, 67))
        self.yes.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/Yes.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressYes.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"")
        self.yes.setText("")
        self.yes.setObjectName("yes")
        self.gridLayout.addWidget(self.yes, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.no = QtWidgets.QPushButton(self.centralwidget)
        self.no.setMinimumSize(QtCore.QSize(144, 67))
        self.no.setMaximumSize(QtCore.QSize(144, 67))
        self.no.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/No.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressNo.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"")
        self.no.setText("")
        self.no.setObjectName("no")
        self.gridLayout.addWidget(self.no, 1, 2, 1, 1)
        exit.setCentralWidget(self.centralwidget)

        self.retranslateUi(exit)
        QtCore.QMetaObject.connectSlotsByName(exit)

    def retranslateUi(self, exit):
        _translate = QtCore.QCoreApplication.translate
        exit.setWindowTitle(_translate("exit", "MainWindow"))

import background
