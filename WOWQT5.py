from PyQt5 import QtWidgets
from GUI import Ui_mainmenu, Ui_exit


class Mainmenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mainmenu, self).__init__()
        self.ui_window = Ui_mainmenu()
        self.ui_window.setupUi(self)

        self.ui_window.Exit.clicked.connect(self.exit)

    def exit(self):
        widget.setCurrentIndex(widget.currentIndex()+1)


class Exit(QtWidgets.QMainWindow):
    def __init__(self):
        super(Exit, self).__init__()
        self.ui_exit = Ui_exit()
        self.ui_exit.setupUi(self)

        self.ui_exit.yes.clicked.connect(self.yes)
        self.ui_exit.no.clicked.connect(self.no)

    def yes(self):
        quit()

    def no(self):
        widget.setCurrentIndex(widget.currentIndex()-1)


app = QtWidgets.QApplication([])
widget = QtWidgets.QStackedWidget()
mainmenu_screen = Mainmenu()
exit_screen = Exit()
widget.addWidget(mainmenu_screen)
widget.addWidget(exit_screen)
widget.showMaximized()
app.exec()
