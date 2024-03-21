from PyQt5 import QtWidgets
from GUI import Ui_mainmenu, Ui_exit, Ui_pillow, Ui_lose, Ui_win


class Mainmenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mainmenu, self).__init__()
        self.ui_window = Ui_mainmenu()
        self.ui_window.setupUi(self)

        self.ui_window.play.clicked.connect(self.play)
        self.ui_window.exit.clicked.connect(self.exit)

    def play(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

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


class Pillow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Pillow, self).__init__()
        self.ui_pillow = Ui_pillow()
        self.ui_pillow.setupUi(self)

        self.ui_pillow.btnmainmenu.clicked.connect(self.mainmenu)
        self.ui_pillow.cancel.clicked.connect(self.cancel)
        self.ui_pillow.confirm.clicked.connect(self.confirm)

        self.ui_pillow.btnp.clicked.connect(self.p)
        self.ui_pillow.btno.clicked.connect(self.o)
        self.ui_pillow.btnd.clicked.connect(self.d)
        self.ui_pillow.btny.clicked.connect(self.y)
        self.ui_pillow.btnsh.clicked.connect(self.sh)
        self.ui_pillow.btnk.clicked.connect(self.k)
        self.ui_pillow.btna.clicked.connect(self.a)

        self.guessed = []

    def mainmenu(self):
        widget.setCurrentIndex(widget.currentIndex() - 2)
        self.clear_screen()

    def cancel(self):
        self.ui_pillow.word.setText("")
        self.btn_enable()

    def confirm(self):
        self.dictionary = open("Dictionary.txt", "r", encoding="utf-8")
        while True:
            self.words = self.dictionary.readline()
            self.words = self.words.split()
            if "подушка" in self.words:
                break
            if not self.words:
                break
        self.dictionary.close()

        if self.ui_pillow.word.text() in self.words and self.ui_pillow.word.text() != "" and self.ui_pillow.word.text() not in self.guessed:
            self.guessed.append(self.ui_pillow.word.text())
            self.ui_pillow.n += 1
            self.ui_pillow.count.setText(str(self.ui_pillow.n) + "/11 СЛОВ")
            if self.ui_pillow.n == 11:
                widget.setCurrentIndex(widget.currentIndex() + 2)
                self.clear_screen()

        elif self.ui_pillow.word.text() not in self.words:
            if self.ui_pillow.cnt < 5:
                self.ui_pillow.cnt += 1
                self.ui_pillow.cat.setStyleSheet("background-image: url(:/back/sprites/cat-" + str(self.ui_pillow.cnt) + ".png);")
            else:
                widget.setCurrentIndex(widget.currentIndex() + 1)
                self.clear_screen()

        self.ui_pillow.word.setText("")

        self.btn_enable()

    def p(self):
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "П")
        self.ui_pillow.btnp.setEnabled(False)
    def o(self):
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "О")
        self.ui_pillow.btno.setEnabled(False)
    def d(self):
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "Д")
        self.ui_pillow.btnd.setEnabled(False)
    def y(self):
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "У")
        self.ui_pillow.btny.setEnabled(False)
    def sh(self):
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "Ш")
        self.ui_pillow.btnsh.setEnabled(False)
    def k(self):
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "К")
        self.ui_pillow.btnk.setEnabled(False)
    def a(self):
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "А")
        self.ui_pillow.btna.setEnabled(False)

    def clear_screen(self):
        self.ui_pillow.n = 0
        self.ui_pillow.count.setText(str(self.ui_pillow.n) + "/11 СЛОВ")
        self.ui_pillow.cnt = 1
        self.ui_pillow.cat.setStyleSheet("background-image: url(:/back/sprites/cat-" + str(self.ui_pillow.cnt) + ".png);")
        self.guessed = []
        self.ui_pillow.word.setText("")
        self.btn_enable()

    def btn_enable(self):
        self.ui_pillow.btnp.setEnabled(True)
        self.ui_pillow.btno.setEnabled(True)
        self.ui_pillow.btnd.setEnabled(True)
        self.ui_pillow.btny.setEnabled(True)
        self.ui_pillow.btnsh.setEnabled(True)
        self.ui_pillow.btnk.setEnabled(True)
        self.ui_pillow.btna.setEnabled(True)

class Lose(QtWidgets.QMainWindow):
    def __init__(self):
        super(Lose, self).__init__()
        self.ui_lose = Ui_lose()
        self.ui_lose.setupUi(self)

        self.ui_lose.btnmainmenu.clicked.connect(self.mainmenu)
        self.ui_lose.btnreturne.clicked.connect(self.returne)

    def mainmenu(self):
        widget.setCurrentIndex(widget.currentIndex() - 3)

    def returne(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

class Win(QtWidgets.QMainWindow):
    def __init__(self):
        super(Win, self).__init__()
        self.ui_win = Ui_win()
        self.ui_win.setupUi(self)

        self.ui_win.btnmainmenu.clicked.connect(self.mainmenu)
        self.ui_win.btnreturn.clicked.connect(self.returne)

    def mainmenu(self):
        widget.setCurrentIndex(widget.currentIndex() - 4)

    def returne(self):
        widget.setCurrentIndex(widget.currentIndex() - 2)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = QtWidgets.QStackedWidget()
    mainmenu_screen = Mainmenu()
    exit_screen = Exit()
    pillow_screen = Pillow()
    lose_screen = Lose()
    win_screen = Win()
    widget.addWidget(mainmenu_screen)
    widget.addWidget(exit_screen)
    widget.addWidget(pillow_screen)
    widget.addWidget(lose_screen)
    widget.addWidget(win_screen)
    widget.show()
    app.exec()
