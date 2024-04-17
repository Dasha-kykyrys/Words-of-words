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
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setMinimumSize(QtCore.QSize(329, 89))
        self.settings.setMaximumSize(QtCore.QSize(329, 89))
        self.settings.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/btsettings.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressbtsettings.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}")
        self.settings.setText("")
        self.settings.setObjectName("settings")
        self.gridLayout.addWidget(self.settings, 7, 0, 1, 1)
        self.rules = QtWidgets.QPushButton(self.centralwidget)
        self.rules.setMinimumSize(QtCore.QSize(329, 89))
        self.rules.setMaximumSize(QtCore.QSize(329, 89))
        self.rules.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/btrules.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressbtrules.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}")
        self.rules.setText("")
        self.rules.setObjectName("rules")
        self.gridLayout.addWidget(self.rules, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setMinimumSize(QtCore.QSize(329, 89))
        self.exit.setMaximumSize(QtCore.QSize(329, 89))
        self.exit.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/btexit.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressbtexit.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}")
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.gridLayout.addWidget(self.exit, 9, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setMinimumSize(QtCore.QSize(329, 89))
        self.play.setMaximumSize(QtCore.QSize(329, 89))
        self.play.setAutoFillBackground(False)
        self.play.setStyleSheet("QPushButton{\n"
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
        self.play.setText("")
        self.play.setObjectName("play")
        self.gridLayout.addWidget(self.play, 6, 0, 1, 1)
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

class Ui_rule_1(object):
    def setupUi(self, rule_1):
        rule_1.setObjectName("rule_1")
        rule_1.resize(1440, 1024)
        rule_1.setMinimumSize(QtCore.QSize(1440, 1024))
        rule_1.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/sprites/rules-1.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(rule_1)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(31)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(85, 77))
        self.label.setMaximumSize(QtCore.QSize(85, 77))
        self.label.setStyleSheet("background-image: url(:/back/sprites/leftoff.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.btnrigth = QtWidgets.QPushButton(self.centralwidget)
        self.btnrigth.setMinimumSize(QtCore.QSize(85, 77))
        self.btnrigth.setMaximumSize(QtCore.QSize(85, 77))
        self.btnrigth.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/right.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressright.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnrigth.setText("")
        self.btnrigth.setObjectName("btnrigth")
        self.horizontalLayout.addWidget(self.btnrigth)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout_2.addWidget(self.btnmainmenu)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        rule_1.setCentralWidget(self.centralwidget)

        self.retranslateUi(rule_1)
        QtCore.QMetaObject.connectSlotsByName(rule_1)

    def retranslateUi(self, rule_1):
        _translate = QtCore.QCoreApplication.translate
        rule_1.setWindowTitle(_translate("rule_1", "MainWindow"))
        self.btnmainmenu.setToolTip(_translate("rule_1", "меню"))

class Ui_rule_2(object):
    def setupUi(self, rule_2):
        rule_2.setObjectName("rule_2")
        rule_2.resize(1440, 1024)
        rule_2.setMinimumSize(QtCore.QSize(1440, 1024))
        rule_2.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/sprites/rules-2.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(rule_2)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(31)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnleft = QtWidgets.QPushButton(self.centralwidget)
        self.btnleft.setMinimumSize(QtCore.QSize(85, 77))
        self.btnleft.setMaximumSize(QtCore.QSize(85, 77))
        self.btnleft.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/left.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressleft.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}")
        self.btnleft.setText("")
        self.btnleft.setObjectName("btnleft")
        self.horizontalLayout.addWidget(self.btnleft)
        self.btnright = QtWidgets.QPushButton(self.centralwidget)
        self.btnright.setMinimumSize(QtCore.QSize(85, 77))
        self.btnright.setMaximumSize(QtCore.QSize(85, 77))
        self.btnright.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/right.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressright.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnright.setText("")
        self.btnright.setObjectName("btnright")
        self.horizontalLayout.addWidget(self.btnright)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout_2.addWidget(self.btnmainmenu)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        rule_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(rule_2)
        QtCore.QMetaObject.connectSlotsByName(rule_2)

    def retranslateUi(self, rule_2):
        _translate = QtCore.QCoreApplication.translate
        rule_2.setWindowTitle(_translate("rule_2", "MainWindow"))
        self.btnmainmenu.setToolTip(_translate("rule_2", "меню"))

class Ui_rule_3(object):
    def setupUi(self, rule_3):
        rule_3.setObjectName("rule_3")
        rule_3.resize(1440, 1024)
        rule_3.setMinimumSize(QtCore.QSize(1440, 1024))
        rule_3.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/sprites/rules-3.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(rule_3)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(31)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnleft = QtWidgets.QPushButton(self.centralwidget)
        self.btnleft.setMinimumSize(QtCore.QSize(85, 77))
        self.btnleft.setMaximumSize(QtCore.QSize(85, 77))
        self.btnleft.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/left.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressleft.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}")
        self.btnleft.setText("")
        self.btnleft.setObjectName("btnleft")
        self.horizontalLayout.addWidget(self.btnleft)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(85, 77))
        self.label.setMaximumSize(QtCore.QSize(85, 77))
        self.label.setStyleSheet("background-image: url(:/back/sprites/rightoff.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout_2.addWidget(self.btnmainmenu)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        rule_3.setCentralWidget(self.centralwidget)

        self.retranslateUi(rule_3)
        QtCore.QMetaObject.connectSlotsByName(rule_3)

    def retranslateUi(self, rule_3):
        _translate = QtCore.QCoreApplication.translate
        rule_3.setWindowTitle(_translate("rule_3", "MainWindow"))
        self.btnmainmenu.setToolTip(_translate("rule_3", "меню"))

class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(1440, 1024)
        settings.setMinimumSize(QtCore.QSize(1440, 1024))
        settings.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/sprites/settings.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(settings)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(440, 5, 440, 200)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnon = QtWidgets.QPushButton(self.centralwidget)
        self.btnon.setMinimumSize(QtCore.QSize(182, 84))
        self.btnon.setMaximumSize(QtCore.QSize(182, 84))
        self.btnon.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/On.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressOn.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"")
        self.btnon.setText("")
        self.btnon.setObjectName("btnon")
        self.horizontalLayout.addWidget(self.btnon)
        self.btnoff = QtWidgets.QPushButton(self.centralwidget)
        self.btnoff.setMinimumSize(QtCore.QSize(182, 84))
        self.btnoff.setMaximumSize(QtCore.QSize(182, 84))
        self.btnoff.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/Off.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressOff.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"")
        self.btnoff.setText("")
        self.btnoff.setObjectName("btnoff")
        self.horizontalLayout.addWidget(self.btnoff)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 0, 0, 6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout_4.addWidget(self.btnmainmenu)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(440, 80, 440, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnon_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnon_2.setMinimumSize(QtCore.QSize(182, 84))
        self.btnon_2.setMaximumSize(QtCore.QSize(182, 84))
        self.btnon_2.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/On.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressOn.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"")
        self.btnon_2.setText("")
        self.btnon_2.setObjectName("btnon_2")
        self.horizontalLayout_3.addWidget(self.btnon_2)
        self.btnoff_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnoff_2.setMinimumSize(QtCore.QSize(182, 84))
        self.btnoff_2.setMaximumSize(QtCore.QSize(182, 84))
        self.btnoff_2.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/Off.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressOff.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"")
        self.btnoff_2.setText("")
        self.btnoff_2.setObjectName("btnoff_2")
        self.horizontalLayout_3.addWidget(self.btnoff_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "MainWindow"))
        self.btnmainmenu.setToolTip(_translate("settings", "меню"))

class Ui_marker(object):
    def setupUi(self, marker):
        marker.setObjectName("marker")
        marker.resize(1440, 1024)
        marker.setMinimumSize(QtCore.QSize(1440, 1024))
        marker.setToolTip("")
        marker.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/sprites/level.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(marker)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.rightWords_2 = QtWidgets.QLabel(self.centralwidget)
        self.rightWords_2.setMinimumSize(QtCore.QSize(200, 525))
        self.rightWords_2.setMaximumSize(QtCore.QSize(200, 525))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.rightWords_2.setFont(font)
        self.rightWords_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.rightWords_2.setText("")
        self.rightWords_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rightWords_2.setObjectName("rightWords_2")
        self.gridLayout_2.addWidget(self.rightWords_2, 1, 1, 1, 1)
        self.rightWords = QtWidgets.QLabel(self.centralwidget)
        self.rightWords.setMinimumSize(QtCore.QSize(200, 525))
        self.rightWords.setMaximumSize(QtCore.QSize(200, 525))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.rightWords.setFont(font)
        self.rightWords.setStyleSheet("color: rgb(255, 255, 255);")
        self.rightWords.setText("")
        self.rightWords.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rightWords.setObjectName("rightWords")
        self.gridLayout_2.addWidget(self.rightWords, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 2, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.cat = QtWidgets.QLabel(self.centralwidget)
        self.cat.setMinimumSize(QtCore.QSize(627, 636))
        self.cat.setMaximumSize(QtCore.QSize(627, 636))
        self.cnt = 0
        self.cat.setStyleSheet("background-image: url(:/back/sprites/cat-" + str(self.cnt) + ".png);")
        self.cat.setText("")
        self.cat.setObjectName("cat")
        self.horizontalLayout_3.addWidget(self.cat)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 7, -1, -1)
        self.horizontalLayout.setSpacing(34)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnf = QtWidgets.QPushButton(self.centralwidget)
        self.btnf.setMinimumSize(QtCore.QSize(107, 95))
        self.btnf.setMaximumSize(QtCore.QSize(107, 95))
        self.btnf.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/f.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressf.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnf.setText("")
        self.btnf.setObjectName("btnf")
        self.horizontalLayout.addWidget(self.btnf)
        self.btnl = QtWidgets.QPushButton(self.centralwidget)
        self.btnl.setMinimumSize(QtCore.QSize(107, 95))
        self.btnl.setMaximumSize(QtCore.QSize(107, 95))
        self.btnl.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/l.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressl.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnl.setText("")
        self.btnl.setObjectName("btnl")
        self.horizontalLayout.addWidget(self.btnl)
        self.btno = QtWidgets.QPushButton(self.centralwidget)
        self.btno.setMinimumSize(QtCore.QSize(107, 95))
        self.btno.setMaximumSize(QtCore.QSize(107, 95))
        self.btno.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/o.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/presso.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btno.setText("")
        self.btno.setObjectName("btno")
        self.horizontalLayout.addWidget(self.btno)
        self.btnm = QtWidgets.QPushButton(self.centralwidget)
        self.btnm.setMinimumSize(QtCore.QSize(107, 95))
        self.btnm.setMaximumSize(QtCore.QSize(107, 95))
        self.btnm.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/m.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressm.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnm.setText("")
        self.btnm.setObjectName("btnm")
        self.horizontalLayout.addWidget(self.btnm)
        self.btna = QtWidgets.QPushButton(self.centralwidget)
        self.btna.setMinimumSize(QtCore.QSize(107, 95))
        self.btna.setMaximumSize(QtCore.QSize(107, 95))
        self.btna.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/a.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressa.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btna.setText("")
        self.btna.setObjectName("btna")
        self.horizontalLayout.addWidget(self.btna)
        self.btns = QtWidgets.QPushButton(self.centralwidget)
        self.btns.setMinimumSize(QtCore.QSize(107, 95))
        self.btns.setMaximumSize(QtCore.QSize(107, 95))
        self.btns.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/s.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/presss.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btns.setText("")
        self.btns.setObjectName("btnc")
        self.horizontalLayout.addWidget(self.btns)
        self.btnt = QtWidgets.QPushButton(self.centralwidget)
        self.btnt.setMinimumSize(QtCore.QSize(107, 95))
        self.btnt.setMaximumSize(QtCore.QSize(107, 95))
        self.btnt.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/t.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/presst.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnt.setText("")
        self.btnt.setObjectName("btnt")
        self.horizontalLayout.addWidget(self.btnt)
        self.btne = QtWidgets.QPushButton(self.centralwidget)
        self.btne.setMinimumSize(QtCore.QSize(107, 95))
        self.btne.setMaximumSize(QtCore.QSize(107, 95))
        self.btne.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/e.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/presse.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btne.setText("")
        self.btne.setObjectName("btne")
        self.horizontalLayout.addWidget(self.btne)
        self.btnr = QtWidgets.QPushButton(self.centralwidget)
        self.btnr.setMinimumSize(QtCore.QSize(107, 95))
        self.btnr.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/r.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressr.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnr.setText("")
        self.btnr.setObjectName("btnr")
        self.horizontalLayout.addWidget(self.btnr)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout_4.addWidget(self.btnmainmenu)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.count = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.count.setFont(font)
        self.count.setStyleSheet("color: rgb(255, 255, 255);")
        self.count.setObjectName("count")
        self.horizontalLayout_4.addWidget(self.count)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setMinimumSize(QtCore.QSize(360, 95))
        self.word.setMaximumSize(QtCore.QSize(360, 95))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.word.setFont(font)
        self.word.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.word.setStyleSheet("color: rgb(255, 255, 255);")
        self.word.setAlignment(QtCore.Qt.AlignCenter)
        self.word.setObjectName("word")
        self.horizontalLayout_6.addWidget(self.word)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(27, 0, 27, 0)
        self.horizontalLayout_2.setSpacing(34)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.confirm = QtWidgets.QPushButton(self.centralwidget)
        self.confirm.setMinimumSize(QtCore.QSize(107, 95))
        self.confirm.setMaximumSize(QtCore.QSize(107, 95))
        self.confirm.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/confirm.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressconfirm.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.confirm.setText("")
        self.confirm.setObjectName("confirm")
        self.horizontalLayout_2.addWidget(self.confirm)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setMinimumSize(QtCore.QSize(107, 95))
        self.cancel.setMaximumSize(QtCore.QSize(107, 95))
        self.cancel.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/cancel.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/presscancel.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.cancel.setText("")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 6, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 2, 0, 1, 1)
        marker.setCentralWidget(self.centralwidget)

        self.retranslateUi(marker)
        QtCore.QMetaObject.connectSlotsByName(marker)

    def retranslateUi(self, marker):
        _translate = QtCore.QCoreApplication.translate
        marker.setWindowTitle(_translate("marker", "MainWindow"))
        self.label.setText(_translate("marker", "ОТГАДАНО:"))
        self.n = 0
        self.count.setText(_translate("pillow", str(self.n) + "/11 СЛОВ"))
        self.confirm.setToolTip(_translate("marker", "подтверждение"))
        self.cancel.setToolTip(_translate("marker", "отмена"))
        self.btnmainmenu.setToolTip(_translate("settings", "меню"))


class Ui_pillow(object):
    def setupUi(self, pillow):
        pillow.setObjectName("pillow")
        pillow.resize(1440, 1024)
        pillow.setMinimumSize(QtCore.QSize(1440, 1024))
        pillow.setToolTip("")
        pillow.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/sprites/level.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(pillow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setMinimumSize(QtCore.QSize(360, 95))
        self.word.setMaximumSize(QtCore.QSize(360, 95))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.word.setFont(font)
        self.word.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.word.setStyleSheet("color: rgb(255, 255, 255);")
        self.word.setAlignment(QtCore.Qt.AlignCenter)
        self.word.setObjectName("word")
        self.horizontalLayout_6.addWidget(self.word)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(27, 0, 27, 0)
        self.horizontalLayout_2.setSpacing(34)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.confirm = QtWidgets.QPushButton(self.centralwidget)
        self.confirm.setMinimumSize(QtCore.QSize(107, 95))
        self.confirm.setMaximumSize(QtCore.QSize(107, 95))
        self.confirm.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/confirm.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressconfirm.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.confirm.setText("")
        self.confirm.setObjectName("confirm")
        self.horizontalLayout_2.addWidget(self.confirm)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setMinimumSize(QtCore.QSize(107, 95))
        self.cancel.setMaximumSize(QtCore.QSize(107, 95))
        self.cancel.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/cancel.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/presscancel.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.cancel.setText("")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(10, 43, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rightWords = QtWidgets.QLabel(self.centralwidget)
        self.rightWords.setMinimumSize(QtCore.QSize(200, 525))
        self.rightWords.setMaximumSize(QtCore.QSize(200, 525))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.rightWords.setFont(font)
        self.rightWords.setMouseTracking(False)
        self.rightWords.setStyleSheet("color: rgb(255, 255, 255);")
        self.rightWords.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rightWords.setObjectName("rightWords")
        self.gridLayout_2.addWidget(self.rightWords, 1, 0, 2, 1)
        self.rightWords_2 = QtWidgets.QLabel(self.centralwidget)
        self.rightWords_2.setMinimumSize(QtCore.QSize(200, 525))
        self.rightWords_2.setMaximumSize(QtCore.QSize(200, 525))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.rightWords_2.setFont(font)
        self.rightWords_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.rightWords_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rightWords_2.setObjectName("rightWords_2")
        self.gridLayout_2.addWidget(self.rightWords_2, 1, 1, 2, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 2, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.cat = QtWidgets.QLabel(self.centralwidget)
        self.cat.setMinimumSize(QtCore.QSize(627, 636))
        self.cat.setMaximumSize(QtCore.QSize(627, 636))
        self.cnt = 0
        self.cat.setStyleSheet("background-image: url(:/back/sprites/cat-" + str(self.cnt) + ".png);")
        self.cat.setText("")
        self.cat.setObjectName("cat")
        self.horizontalLayout_3.addWidget(self.cat)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 7, -1, -1)
        self.horizontalLayout.setSpacing(34)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.btnp = QtWidgets.QPushButton(self.centralwidget)
        self.btnp.setMinimumSize(QtCore.QSize(107, 95))
        self.btnp.setMaximumSize(QtCore.QSize(107, 95))
        self.btnp.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/p.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressp.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnp.setText("")
        self.btnp.setObjectName("btnp")
        self.horizontalLayout.addWidget(self.btnp)
        self.btno = QtWidgets.QPushButton(self.centralwidget)
        self.btno.setMinimumSize(QtCore.QSize(107, 95))
        self.btno.setMaximumSize(QtCore.QSize(107, 95))
        self.btno.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/o.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/presso.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btno.setText("")
        self.btno.setObjectName("btno")
        self.horizontalLayout.addWidget(self.btno)
        self.btnd = QtWidgets.QPushButton(self.centralwidget)
        self.btnd.setMinimumSize(QtCore.QSize(107, 95))
        self.btnd.setMaximumSize(QtCore.QSize(107, 95))
        self.btnd.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/d.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressd.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnd.setText("")
        self.btnd.setObjectName("btnd")
        self.horizontalLayout.addWidget(self.btnd)
        self.btny = QtWidgets.QPushButton(self.centralwidget)
        self.btny.setMinimumSize(QtCore.QSize(107, 95))
        self.btny.setMaximumSize(QtCore.QSize(107, 95))
        self.btny.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/y.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressy.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btny.setText("")
        self.btny.setObjectName("btny")
        self.horizontalLayout.addWidget(self.btny)
        self.btnsh = QtWidgets.QPushButton(self.centralwidget)
        self.btnsh.setMinimumSize(QtCore.QSize(107, 95))
        self.btnsh.setMaximumSize(QtCore.QSize(107, 95))
        self.btnsh.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/sh.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/presssh.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnsh.setText("")
        self.btnsh.setObjectName("btnsh")
        self.horizontalLayout.addWidget(self.btnsh)
        self.btnk = QtWidgets.QPushButton(self.centralwidget)
        self.btnk.setMinimumSize(QtCore.QSize(107, 95))
        self.btnk.setMaximumSize(QtCore.QSize(107, 95))
        self.btnk.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/k.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressk.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnk.setText("")
        self.btnk.setObjectName("btnk")
        self.horizontalLayout.addWidget(self.btnk)
        self.btna = QtWidgets.QPushButton(self.centralwidget)
        self.btna.setMinimumSize(QtCore.QSize(107, 95))
        self.btna.setMaximumSize(QtCore.QSize(107, 95))
        self.btna.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/a.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressa.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btna.setText("")
        self.btna.setObjectName("btna")
        self.horizontalLayout.addWidget(self.btna)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout_4.addWidget(self.btnmainmenu)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.count = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.count.setFont(font)
        self.count.setStyleSheet("color: rgb(255, 255, 255);")
        self.count.setObjectName("count")
        self.horizontalLayout_4.addWidget(self.count)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        pillow.setCentralWidget(self.centralwidget)

        self.retranslateUi(pillow)
        QtCore.QMetaObject.connectSlotsByName(pillow)

    def retranslateUi(self, pillow):
        _translate = QtCore.QCoreApplication.translate
        pillow.setWindowTitle(_translate("pillow", "MainWindow"))
        self.label.setText(_translate("pillow", "ОТГАДАНО:"))
        self.n = 0
        self.count.setText(_translate("pillow", str(self.n) + "/11 СЛОВ"))
        self.confirm.setToolTip(_translate("pillow", "подтверждение"))
        self.cancel.setToolTip(_translate("pillow", "отмена"))
        self.btnmainmenu.setToolTip(_translate("settings", "меню"))

class Ui_mokasin(object):
    def setupUi(self, mokasin):
        mokasin.setObjectName("mokasin")
        mokasin.resize(1440, 1024)
        mokasin.setMinimumSize(QtCore.QSize(1440, 1024))
        mokasin.setToolTip("")
        mokasin.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/sprites/level.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(mokasin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setMinimumSize(QtCore.QSize(360, 95))
        self.word.setMaximumSize(QtCore.QSize(360, 95))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.word.setFont(font)
        self.word.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.word.setStyleSheet("color: rgb(255, 255, 255);")
        self.word.setAlignment(QtCore.Qt.AlignCenter)
        self.word.setObjectName("word")
        self.horizontalLayout_6.addWidget(self.word)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(27, 0, 27, 0)
        self.horizontalLayout_2.setSpacing(34)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.confirm = QtWidgets.QPushButton(self.centralwidget)
        self.confirm.setMinimumSize(QtCore.QSize(107, 95))
        self.confirm.setMaximumSize(QtCore.QSize(107, 95))
        self.confirm.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/confirm.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressconfirm.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.confirm.setText("")
        self.confirm.setObjectName("confirm")
        self.horizontalLayout_2.addWidget(self.confirm)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setMinimumSize(QtCore.QSize(107, 95))
        self.cancel.setMaximumSize(QtCore.QSize(107, 95))
        self.cancel.setToolTipDuration(-1)
        self.cancel.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/cancel.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/presscancel.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.cancel.setText("")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(10, 43, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rightWords = QtWidgets.QLabel(self.centralwidget)
        self.rightWords.setMinimumSize(QtCore.QSize(200, 525))
        self.rightWords.setMaximumSize(QtCore.QSize(200, 525))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.rightWords.setFont(font)
        self.rightWords.setMouseTracking(False)
        self.rightWords.setStyleSheet("color: rgb(255, 255, 255);")
        self.rightWords.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rightWords.setObjectName("rightWords")
        self.gridLayout_2.addWidget(self.rightWords, 1, 0, 2, 1)
        self.rightWords_2 = QtWidgets.QLabel(self.centralwidget)
        self.rightWords_2.setMinimumSize(QtCore.QSize(200, 525))
        self.rightWords_2.setMaximumSize(QtCore.QSize(200, 525))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.rightWords_2.setFont(font)
        self.rightWords_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.rightWords_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rightWords_2.setObjectName("rightWords_2")
        self.gridLayout_2.addWidget(self.rightWords_2, 1, 1, 2, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(400, 60))
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 2, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.cat = QtWidgets.QLabel(self.centralwidget)
        self.cat.setMinimumSize(QtCore.QSize(627, 636))
        self.cat.setMaximumSize(QtCore.QSize(627, 636))
        self.cnt = 0
        self.cat.setStyleSheet("background-image: url(:/back/sprites/cat-" + str(self.cnt) + ".png);")
        self.cat.setText("")
        self.cat.setObjectName("cat")
        self.horizontalLayout_3.addWidget(self.cat)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 7, -1, -1)
        self.horizontalLayout.setSpacing(34)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.btnm = QtWidgets.QPushButton(self.centralwidget)
        self.btnm.setMinimumSize(QtCore.QSize(107, 95))
        self.btnm.setMaximumSize(QtCore.QSize(107, 95))
        self.btnm.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/m.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressm.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnm.setText("")
        self.btnm.setObjectName("btnm")
        self.horizontalLayout.addWidget(self.btnm)
        self.btno = QtWidgets.QPushButton(self.centralwidget)
        self.btno.setMinimumSize(QtCore.QSize(107, 95))
        self.btno.setMaximumSize(QtCore.QSize(107, 95))
        self.btno.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/o.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/presso.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btno.setText("")
        self.btno.setObjectName("btno")
        self.horizontalLayout.addWidget(self.btno)
        self.btnk = QtWidgets.QPushButton(self.centralwidget)
        self.btnk.setMinimumSize(QtCore.QSize(107, 95))
        self.btnk.setMaximumSize(QtCore.QSize(107, 95))
        self.btnk.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/k.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressk.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnk.setText("")
        self.btnk.setObjectName("btnk")
        self.horizontalLayout.addWidget(self.btnk)
        self.btna = QtWidgets.QPushButton(self.centralwidget)
        self.btna.setMinimumSize(QtCore.QSize(107, 95))
        self.btna.setMaximumSize(QtCore.QSize(107, 95))
        self.btna.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/a.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressa.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btna.setText("")
        self.btna.setObjectName("btna")
        self.horizontalLayout.addWidget(self.btna)
        self.btns = QtWidgets.QPushButton(self.centralwidget)
        self.btns.setMinimumSize(QtCore.QSize(107, 95))
        self.btns.setMaximumSize(QtCore.QSize(107, 95))
        self.btns.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/s.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/presss.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btns.setText("")
        self.btns.setObjectName("btns")
        self.horizontalLayout.addWidget(self.btns)
        self.btni = QtWidgets.QPushButton(self.centralwidget)
        self.btni.setMinimumSize(QtCore.QSize(107, 95))
        self.btni.setMaximumSize(QtCore.QSize(107, 95))
        self.btni.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/i.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressi.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btni.setText("")
        self.btni.setObjectName("btni")
        self.horizontalLayout.addWidget(self.btni)
        self.btnn = QtWidgets.QPushButton(self.centralwidget)
        self.btnn.setMinimumSize(QtCore.QSize(107, 95))
        self.btnn.setMaximumSize(QtCore.QSize(107, 95))
        self.btnn.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/n.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressn.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnn.setText("")
        self.btnn.setObjectName("btnn")
        self.horizontalLayout.addWidget(self.btnn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout_4.addWidget(self.btnmainmenu)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.count = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Amatic SC")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.count.setFont(font)
        self.count.setStyleSheet("color: rgb(255, 255, 255);")
        self.count.setObjectName("count")
        self.horizontalLayout_4.addWidget(self.count)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        mokasin.setCentralWidget(self.centralwidget)

        self.retranslateUi(mokasin)
        QtCore.QMetaObject.connectSlotsByName(mokasin)

    def retranslateUi(self, mokasin):
        _translate = QtCore.QCoreApplication.translate
        mokasin.setWindowTitle(_translate("mokasin", "MainWindow"))
        self.confirm.setToolTip(_translate("mokasin", "подтверждение"))
        self.cancel.setToolTip(_translate("mokasin", "отмена"))
        self.btnmainmenu.setToolTip(_translate("settings", "меню"))
        self.label.setText(_translate("mokasin", "ОТГАДАНО:"))
        self.n = 0
        self.count.setText(_translate("pillow", str(self.n) + "/11 СЛОВ"))

class Ui_lose(object):
    def setupUi(self, lose):
        lose.setObjectName("lose")
        lose.resize(1440, 1024)
        lose.setMinimumSize(QtCore.QSize(1440, 1024))
        lose.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/sprites/goLose.png);\n"
"border-position:center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(lose)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 300, -1, 0)
        self.horizontalLayout.setSpacing(143)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnreturne = QtWidgets.QPushButton(self.centralwidget)
        self.btnreturne.setMinimumSize(QtCore.QSize(107, 95))
        self.btnreturne.setMaximumSize(QtCore.QSize(107, 95))
        self.btnreturne.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/repeat.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressrepeat.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnreturne.setText("")
        self.btnreturne.setObjectName("btnreturne")
        self.horizontalLayout.addWidget(self.btnreturne)
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout.addWidget(self.btnmainmenu)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        lose.setCentralWidget(self.centralwidget)

        self.retranslateUi(lose)
        QtCore.QMetaObject.connectSlotsByName(lose)

    def retranslateUi(self, lose):
        _translate = QtCore.QCoreApplication.translate
        lose.setWindowTitle(_translate("lose", "MainWindow"))
        self.btnmainmenu.setToolTip(_translate("settings", "меню"))
        self.btnreturne.setToolTip(_translate("settings", "повторить"))

class Ui_win(object):
    def setupUi(self, win):
        win.setObjectName("win")
        win.resize(1440, 1024)
        win.setMinimumSize(QtCore.QSize(1440, 1024))
        win.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/sprites/goWin.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(win)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 300, -1, -1)
        self.horizontalLayout.setSpacing(143)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnreturn = QtWidgets.QPushButton(self.centralwidget)
        self.btnreturn.setMinimumSize(QtCore.QSize(107, 95))
        self.btnreturn.setMaximumSize(QtCore.QSize(107, 95))
        self.btnreturn.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/repeat.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressrepeat.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnreturn.setText("")
        self.btnreturn.setObjectName("btnreturn")
        self.horizontalLayout.addWidget(self.btnreturn)
        self.btnmainmenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnmainmenu.setMinimumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setMaximumSize(QtCore.QSize(107, 95))
        self.btnmainmenu.setStyleSheet("QPushButton{\n"
"border-image: url(:/back/sprites/btmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-image: url(:/back/sprites/pressbtmainmenu.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btnmainmenu.setText("")
        self.btnmainmenu.setObjectName("btnmainmenu")
        self.horizontalLayout.addWidget(self.btnmainmenu)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        win.setCentralWidget(self.centralwidget)

        self.retranslateUi(win)
        QtCore.QMetaObject.connectSlotsByName(win)

    def retranslateUi(self, win):
        _translate = QtCore.QCoreApplication.translate
        win.setWindowTitle(_translate("win", "MainWindow"))
        self.btnmainmenu.setToolTip(_translate("settings", "меню"))
        self.btnreturn.setToolTip(_translate("settings", "повторить"))


import background
