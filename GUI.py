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


class Ui_pillow(object):
    def setupUi(self, pillow):
        pillow.setObjectName("pillow")
        pillow.resize(1440, 1024)
        pillow.setMinimumSize(QtCore.QSize(1440, 1024))
        pillow.setStyleSheet("QMainWindow{\n"
"border-image: url(:/back/sprites/level.png);\n"
"border-position: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(pillow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cat = QtWidgets.QLabel(self.centralwidget)
        self.cat.setMinimumSize(QtCore.QSize(627, 636))
        self.cat.setMaximumSize(QtCore.QSize(627, 636))
        self.cnt = 0
        self.cat.setStyleSheet("background-image: url(:/back/sprites/cat-" + str(self.cnt) + ".png);")
        self.cat.setText("")
        self.cat.setObjectName("cat")
        self.horizontalLayout_3.addWidget(self.cat)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 7, -1, -1)
        self.horizontalLayout.setSpacing(34)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnp = QtWidgets.QPushButton(self.centralwidget)
        self.btnp.setMinimumSize(QtCore.QSize(107, 95))
        self.btnp.setMaximumSize(QtCore.QSize(107, 95))
        self.btnp.setStyleSheet("QPushButton{\n"
"background-image: url(:/back/sprites/п.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressп.png);\n"
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
"background-image: url(:/back/sprites/о.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressо.png);\n"
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
"background-image: url(:/back/sprites/д.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressд.png);\n"
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
"background-image: url(:/back/sprites/у.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressу.png);\n"
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
"background-image: url(:/back/sprites/ш.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressш.png);\n"
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
"background-image: url(:/back/sprites/к.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressк.png);\n"
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
"background-image: url(:/back/sprites/а.png);\n"
"border: none;\n"
"border-radus: 9px;}\n"
"\n"
"QPushButton:hover{\n"
"background-image: url(:/back/sprites/pressа.png);\n"
"border: none;\n"
"border-radus: 9px;\n"
"}\n"
"")
        self.btna.setText("")
        self.btna.setObjectName("btna")
        self.horizontalLayout.addWidget(self.btna)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
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
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
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
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 6, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 2, 0, 1, 1)
        pillow.setCentralWidget(self.centralwidget)

        self.retranslateUi(pillow)
        QtCore.QMetaObject.connectSlotsByName(pillow)

    def retranslateUi(self, pillow):
        _translate = QtCore.QCoreApplication.translate
        pillow.setWindowTitle(_translate("pillow", "MainWindow"))
        self.n = 0
        self.count.setText(_translate("pillow", str(self.n) + "/11 СЛОВ"))
        self.word.setText(_translate("pillow", ""))

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


import background
