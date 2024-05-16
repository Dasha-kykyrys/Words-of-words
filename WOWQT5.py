import random

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QDesktopWidget
from GUI import Ui_mainmenu, Ui_exit, Ui_pillow, Ui_lose, Ui_win, Ui_marker, Ui_mokasin, Ui_settings, Ui_rule


class Mainmenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mainmenu, self).__init__()
        self.ui_window = Ui_mainmenu()
        self.ui_window.setupUi(self)

        self.ui_window.play.clicked.connect(self.play)
        self.ui_window.settings.clicked.connect(self.settings)
        self.ui_window.rules.clicked.connect(self.rules)
        self.ui_window.exit.clicked.connect(self.exit)

    @staticmethod
    def play():
        if sound_play:
            sound_player.play()
        global number_level
        number_level = random.randint(6, 8)
        widget.setCurrentIndex(widget.currentIndex() + number_level)

    @staticmethod
    def settings():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() + 1)

    @staticmethod
    def rules():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() + 2)

    @staticmethod
    def exit():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() + 3)


class Settings(QtWidgets.QMainWindow):
    def __init__(self):
        super(Settings, self).__init__()
        self.ui_settings = Ui_settings()
        self.ui_settings.setupUi(self)

        self.ui_settings.btnoff.clicked.connect(self.music_off)
        self.ui_settings.btnon.clicked.connect(self.music_on)
        self.ui_settings.btnon.setEnabled(False)

        self.ui_settings.btnoff_2.clicked.connect(self.sound_off)
        self.ui_settings.btnon_2.clicked.connect(self.sound_on)
        self.ui_settings.btnon_2.setEnabled(False)

        self.ui_settings.btnmainmenu.clicked.connect(self.mainmenu)

    @staticmethod
    def mainmenu():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def music_off(self):
        if sound_play:
            sound_player.play()
        media_player.stop()
        self.ui_settings.btnoff.setEnabled(False)
        self.ui_settings.btnon.setEnabled(True)

    def music_on(self):
        if sound_play:
            sound_player.play()
        media_player.play()
        self.ui_settings.btnon.setEnabled(False)
        self.ui_settings.btnoff.setEnabled(True)

    def sound_off(self):
        global sound_play
        if sound_play:
            sound_player.play()
        sound_play = False
        self.ui_settings.btnoff_2.setEnabled(False)
        self.ui_settings.btnon_2.setEnabled(True)

    def sound_on(self):
        global sound_play
        sound_play = True
        self.ui_settings.btnon_2.setEnabled(False)
        self.ui_settings.btnoff_2.setEnabled(True)


class Rules(QtWidgets.QMainWindow):
    def __init__(self):
        super(Rules, self).__init__()
        self.ui_rule = Ui_rule()
        self.ui_rule.setupUi(self)

        self.ui_rule.btnright.clicked.connect(self.right)
        self.ui_rule.btnleft.clicked.connect(self.left)
        self.ui_rule.btnleft.setEnabled(False)
        self.ui_rule.btnmainmenu.clicked.connect(self.mainmenu)

        self.page = 1

    def right(self):
        if sound_play:
            sound_player.play()

        if self.page != 3:
            self.page += 1
        self.setStyleSheet("QMainWindow{\n"
                           "border-image: url(:/back/resources/sprites/rules-" + str(self.page) + ".png);\n"
                           "border-position: center;\n"
                           "}")

        if self.page > 1:
            self.ui_rule.btnleft.setEnabled(True)
        if self.page == 3:
            self.ui_rule.btnright.setEnabled(False)

    def left(self):
        if sound_play:
            sound_player.play()

        if self.page != 1:
            self.page -= 1
        self.setStyleSheet("QMainWindow{\n"
                           "border-image: url(:/back/resources/sprites/rules-" + str(self.page) + ".png);\n"
                           "border-position: center;\n"
                           "}")

        if self.page < 3:
            self.ui_rule.btnright.setEnabled(True)
        if self.page == 1:
            self.ui_rule.btnleft.setEnabled(False)

    def mainmenu(self):
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 2)
        self.ui_rule.btnleft.setEnabled(False)
        self.ui_rule.btnright.setEnabled(True)
        self.page = 1
        self.setStyleSheet("QMainWindow{\n"
                           "border-image: url(:/back/resources/sprites/rules-1.png);\n"
                           "border-position: center;\n"
                           "}")


class Exit(QtWidgets.QMainWindow):
    def __init__(self):
        super(Exit, self).__init__()
        self.ui_exit = Ui_exit()
        self.ui_exit.setupUi(self)

        self.ui_exit.yes.clicked.connect(self.yes)
        self.ui_exit.no.clicked.connect(self.no)

    @staticmethod
    def yes():
        quit()

    @staticmethod
    def no():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 3)


class Marker(QtWidgets.QMainWindow):
    def __init__(self):
        super(Marker, self).__init__()
        self.ui_marker = Ui_marker()
        self.ui_marker.setupUi(self)

        self.ui_marker.btnmainmenu.clicked.connect(self.mainmenu)
        self.ui_marker.cancel.clicked.connect(self.cancel)
        self.ui_marker.confirm.clicked.connect(self.confirm)

        self.ui_marker.btnf.clicked.connect(self.f)
        self.ui_marker.btnl.clicked.connect(self.l)
        self.ui_marker.btno.clicked.connect(self.o)
        self.ui_marker.btnm.clicked.connect(self.m)
        self.ui_marker.btna.clicked.connect(self.a)
        self.ui_marker.btns.clicked.connect(self.s)
        self.ui_marker.btnt.clicked.connect(self.t)
        self.ui_marker.btne.clicked.connect(self.e)
        self.ui_marker.btnr.clicked.connect(self.r)

        self.guessed = []
        self.maxrightWords = 0
        self.double_right = 0
        self.cnt = 0
        self.n = 0

        dictionary = open("Dictionary.txt", "r", encoding="utf-8")
        while True:
            self.words = dictionary.readline()
            self.words = self.words.split()
            if "фломастер" in self.words:
                break
            if not self.words:
                break
        dictionary.close()

    def mainmenu(self):
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 6)
        self.clear_screen()

    def cancel(self):
        if sound_play:
            sound_player.play()
        self.ui_marker.word.setText("")
        self.btn_enable()

    def confirm(self):
        if sound_play:
            sound_player.play()
        if self.ui_marker.word.text() in self.words and self.ui_marker.word.text() != "" and self.ui_marker.word.text() not in self.guessed:
            self.guessed.append(self.ui_marker.word.text())
            self.n += 1
            if self.cnt >= 1:
                self.double_right += 1
            self.ui_marker.count.setText(str(self.n) + "/12 СЛОВ")

            if self.n == 12:
                widget.setCurrentIndex(widget.currentIndex() - 1)
                self.clear_screen()

            elif self.maxrightWords != 6:
                self.ui_marker.rightWords.setText(self.ui_marker.rightWords.text() + self.ui_marker.word.text() + "\n")
                self.maxrightWords += 1
            else:
                self.ui_marker.rightWords_2.setText(
                    self.ui_marker.rightWords_2.text() + self.ui_marker.word.text() + "\n")

            if self.double_right == 2:
                self.double_right = 0
                self.cnt -= 1
                self.ui_marker.cat.setStyleSheet(
                    "background-image: url(:/back/resources/sprites/cat-" + str(self.cnt) + ".png);")

        elif self.ui_marker.word.text() not in self.words:
            if self.cnt < 5:
                self.double_right = 0
                self.cnt += 1
                self.ui_marker.cat.setStyleSheet(
                    "background-image: url(:/back/resources/sprites/cat-" + str(self.cnt) + ".png);")
            else:
                widget.setCurrentIndex(widget.currentIndex() - 2)
                self.clear_screen()

        self.ui_marker.word.setText("")

        self.btn_enable()

    def f(self):
        if sound_play:
            sound_player.play()
        self.ui_marker.word.setText(self.ui_marker.word.text() + "Ф")
        self.ui_marker.btnf.setEnabled(False)

    def l(self):
        if sound_play:
            sound_player.play()
        self.ui_marker.word.setText(self.ui_marker.word.text() + "Л")
        self.ui_marker.btnl.setEnabled(False)

    def o(self):
        if sound_play:
            sound_player.play()
        self.ui_marker.word.setText(self.ui_marker.word.text() + "О")
        self.ui_marker.btno.setEnabled(False)

    def m(self):
        if sound_play:
            sound_player.play()
        self.ui_marker.word.setText(self.ui_marker.word.text() + "М")
        self.ui_marker.btnm.setEnabled(False)

    def a(self):
        if sound_play:
            sound_player.play()
        self.ui_marker.word.setText(self.ui_marker.word.text() + "А")
        self.ui_marker.btna.setEnabled(False)

    def s(self):
        if sound_play:
            sound_player.play()
        self.ui_marker.word.setText(self.ui_marker.word.text() + "С")
        self.ui_marker.btns.setEnabled(False)

    def t(self):
        if sound_play:
            sound_player.play()
        self.ui_marker.word.setText(self.ui_marker.word.text() + "Т")
        self.ui_marker.btnt.setEnabled(False)

    def e(self):
        if sound_play:
            sound_player.play()
        self.ui_marker.word.setText(self.ui_marker.word.text() + "Е")
        self.ui_marker.btne.setEnabled(False)

    def r(self):
        if sound_play:
            sound_player.play()
        self.ui_marker.word.setText(self.ui_marker.word.text() + "Р")
        self.ui_marker.btnr.setEnabled(False)

    def clear_screen(self):
        self.n = 0
        self.double_right = 0
        self.ui_marker.count.setText("0/12 СЛОВ")
        self.cnt = 0
        self.ui_marker.cat.setStyleSheet(
            "background-image: url(:/back/resources/sprites/cat-0.png);")
        self.guessed = []
        self.ui_marker.rightWords.setText("")
        self.ui_marker.rightWords_2.setText("")
        self.maxrightWords = 0
        self.ui_marker.word.setText("")
        self.btn_enable()

    def btn_enable(self):
        self.ui_marker.btnf.setEnabled(True)
        self.ui_marker.btnl.setEnabled(True)
        self.ui_marker.btno.setEnabled(True)
        self.ui_marker.btnm.setEnabled(True)
        self.ui_marker.btna.setEnabled(True)
        self.ui_marker.btns.setEnabled(True)
        self.ui_marker.btnt.setEnabled(True)
        self.ui_marker.btne.setEnabled(True)
        self.ui_marker.btnr.setEnabled(True)


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
        self.maxrightWords = 0
        self.double_right = 0
        self.cnt = 0
        self.n = 0

        dictionary = open("Dictionary.txt", "r", encoding="utf-8")
        while True:
            self.words = dictionary.readline()
            self.words = self.words.split()
            if "подушка" in self.words:
                break
            if not self.words:
                break
        dictionary.close()

    def mainmenu(self):
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 7)
        self.clear_screen()

    def cancel(self):
        if sound_play:
            sound_player.play()
        self.ui_pillow.word.setText("")
        self.btn_enable()

    def confirm(self):
        if sound_play:
            sound_player.play()
        if self.ui_pillow.word.text() in self.words and self.ui_pillow.word.text() != "" and self.ui_pillow.word.text() not in self.guessed:
            self.guessed.append(self.ui_pillow.word.text())
            if self.cnt >= 1:
                self.double_right += 1
            self.n += 1
            self.ui_pillow.count.setText(str(self.n) + "/11 СЛОВ")

            if self.n == 11:
                widget.setCurrentIndex(widget.currentIndex() - 2)
                self.clear_screen()

            elif self.maxrightWords != 6:
                self.ui_pillow.rightWords.setText(self.ui_pillow.rightWords.text() + self.ui_pillow.word.text() + "\n")
                self.maxrightWords += 1
            else:
                self.ui_pillow.rightWords_2.setText(self.ui_pillow.rightWords_2.text() + self.ui_pillow.word.text() + "\n")

            if self.double_right == 2:
                self.double_right = 0
                self.cnt -= 1
                self.ui_pillow.cat.setStyleSheet(
                    "background-image: url(:/back/resources/sprites/cat-" + str(self.cnt) + ".png);")

        elif self.ui_pillow.word.text() not in self.words:
            if self.cnt < 5:
                self.double_right = 0
                self.cnt += 1
                self.ui_pillow.cat.setStyleSheet("background-image: url(:/back/resources/sprites/cat-" + str(self.cnt) + ".png);")
            else:
                widget.setCurrentIndex(widget.currentIndex() - 3)
                self.clear_screen()

        self.ui_pillow.word.setText("")

        self.btn_enable()

    def p(self):
        if sound_play:
            sound_player.play()
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "П")
        self.ui_pillow.btnp.setEnabled(False)

    def o(self):
        if sound_play:
            sound_player.play()
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "О")
        self.ui_pillow.btno.setEnabled(False)

    def d(self):
        if sound_play:
            sound_player.play()
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "Д")
        self.ui_pillow.btnd.setEnabled(False)

    def y(self):
        if sound_play:
            sound_player.play()
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "У")
        self.ui_pillow.btny.setEnabled(False)

    def sh(self):
        if sound_play:
            sound_player.play()
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "Ш")
        self.ui_pillow.btnsh.setEnabled(False)

    def k(self):
        if sound_play:
            sound_player.play()
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "К")
        self.ui_pillow.btnk.setEnabled(False)

    def a(self):
        if sound_play:
            sound_player.play()
        self.ui_pillow.word.setText(self.ui_pillow.word.text() + "А")
        self.ui_pillow.btna.setEnabled(False)

    def clear_screen(self):
        self.n = 0
        self.double_right = 0
        self.ui_pillow.count.setText("0/11 СЛОВ")
        self.cnt = 0
        self.ui_pillow.cat.setStyleSheet("background-image: url(:/back/resources/sprites/cat-0.png);")
        self.guessed = []
        self.ui_pillow.rightWords.setText("")
        self.ui_pillow.rightWords_2.setText("")
        self.maxrightWords = 0
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


class Mokasin(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mokasin, self).__init__()
        self.ui_mokasin = Ui_mokasin()
        self.ui_mokasin.setupUi(self)

        self.ui_mokasin.btnmainmenu.clicked.connect(self.mainmenu)
        self.ui_mokasin.cancel.clicked.connect(self.cancel)
        self.ui_mokasin.confirm.clicked.connect(self.confirm)

        self.ui_mokasin.btnm.clicked.connect(self.m)
        self.ui_mokasin.btno.clicked.connect(self.o)
        self.ui_mokasin.btnk.clicked.connect(self.k)
        self.ui_mokasin.btna.clicked.connect(self.a)
        self.ui_mokasin.btns.clicked.connect(self.s)
        self.ui_mokasin.btni.clicked.connect(self.i)
        self.ui_mokasin.btnn.clicked.connect(self.n)

        self.guessed = []
        self.maxrightWords = 0
        self.double_right = 0
        self.cnt = 0
        self.n = 0

        dictionary = open("Dictionary.txt", "r", encoding="utf-8")
        while True:
            self.words = dictionary.readline()
            self.words = self.words.split()
            if "мокасин" in self.words:
                break
            if not self.words:
                break
        dictionary.close()

    def mainmenu(self):
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 8)
        self.clear_screen()

    def cancel(self):
        if sound_play:
            sound_player.play()
        self.ui_mokasin.word.setText("")
        self.btn_enable()

    def confirm(self):
        if sound_play:
            sound_player.play()
        if self.ui_mokasin.word.text() in self.words and self.ui_mokasin.word.text() != "" and self.ui_mokasin.word.text() not in self.guessed:
            self.guessed.append(self.ui_mokasin.word.text())
            if self.cnt >= 1:
                self.double_right += 1
            self.n += 1
            self.ui_mokasin.count.setText(str(self.n) + "/11 СЛОВ")

            if self.n == 11:
                widget.setCurrentIndex(widget.currentIndex() - 3)
                self.clear_screen()

            elif self.maxrightWords != 6:
                self.ui_mokasin.rightWords.setText(self.ui_mokasin.rightWords.text() + self.ui_mokasin.word.text() + "\n")
                self.maxrightWords += 1
            else:
                self.ui_mokasin.rightWords_2.setText(
                    self.ui_mokasin.rightWords_2.text() + self.ui_mokasin.word.text() + "\n")

            if self.double_right == 2:
                self.double_right = 0
                self.cnt -= 1
                self.ui_mokasin.cat.setStyleSheet(
                    "background-image: url(:/back/resources/sprites/cat-" + str(self.cnt) + ".png);")

        elif self.ui_mokasin.word.text() not in self.words:
            if self.cnt < 5:
                self.double_right = 0
                self.cnt += 1
                self.ui_mokasin.cat.setStyleSheet(
                    "background-image: url(:/back/resources/sprites/cat-" + str(self.cnt) + ".png);")
            else:
                widget.setCurrentIndex(widget.currentIndex() - 4)
                self.clear_screen()

        self.ui_mokasin.word.setText("")

        self.btn_enable()

    def m(self):
        if sound_play:
            sound_player.play()
        self.ui_mokasin.word.setText(self.ui_mokasin.word.text() + "М")
        self.ui_mokasin.btnm.setEnabled(False)

    def o(self):
        if sound_play:
            sound_player.play()
        self.ui_mokasin.word.setText(self.ui_mokasin.word.text() + "О")
        self.ui_mokasin.btno.setEnabled(False)

    def k(self):
        if sound_play:
            sound_player.play()
        self.ui_mokasin.word.setText(self.ui_mokasin.word.text() + "К")
        self.ui_mokasin.btnk.setEnabled(False)

    def a(self):
        if sound_play:
            sound_player.play()
        self.ui_mokasin.word.setText(self.ui_mokasin.word.text() + "А")
        self.ui_mokasin.btna.setEnabled(False)

    def s(self):
        if sound_play:
            sound_player.play()
        self.ui_mokasin.word.setText(self.ui_mokasin.word.text() + "С")
        self.ui_mokasin.btns.setEnabled(False)

    def i(self):
        if sound_play:
            sound_player.play()
        self.ui_mokasin.word.setText(self.ui_mokasin.word.text() + "И")
        self.ui_mokasin.btni.setEnabled(False)

    def n(self):
        if sound_play:
            sound_player.play()
        self.ui_mokasin.word.setText(self.ui_mokasin.word.text() + "Н")
        self.ui_mokasin.btnn.setEnabled(False)

    def clear_screen(self):
        self.n = 0
        self.double_right = 0
        self.ui_mokasin.count.setText("0/11 СЛОВ")
        self.cnt = 0
        self.ui_mokasin.cat.setStyleSheet(
            "background-image: url(:/back/resources/sprites/cat-0.png);")
        self.guessed = []
        self.ui_mokasin.rightWords.setText("")
        self.ui_mokasin.rightWords_2.setText("")
        self.maxrightWords = 0
        self.ui_mokasin.word.setText("")
        self.btn_enable()

    def btn_enable(self):
        self.ui_mokasin.btnm.setEnabled(True)
        self.ui_mokasin.btno.setEnabled(True)
        self.ui_mokasin.btnk.setEnabled(True)
        self.ui_mokasin.btna.setEnabled(True)
        self.ui_mokasin.btns.setEnabled(True)
        self.ui_mokasin.btni.setEnabled(True)
        self.ui_mokasin.btnn.setEnabled(True)
    

class Lose(QtWidgets.QMainWindow):
    def __init__(self):
        super(Lose, self).__init__()
        self.ui_lose = Ui_lose()
        self.ui_lose.setupUi(self)

        self.ui_lose.btnmainmenu.clicked.connect(self.mainmenu)
        self.ui_lose.btnreturne.clicked.connect(self.returne)

    @staticmethod
    def mainmenu():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 4)

    @staticmethod
    def returne():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() + number_level - 4)


class Win(QtWidgets.QMainWindow):
    def __init__(self):
        super(Win, self).__init__()
        self.ui_win = Ui_win()
        self.ui_win.setupUi(self)

        self.ui_win.btnmainmenu.clicked.connect(self.mainmenu)
        self.ui_win.btnreturn.clicked.connect(self.returne)

    @staticmethod
    def mainmenu():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() - 5)

    @staticmethod
    def returne():
        if sound_play:
            sound_player.play()
        widget.setCurrentIndex(widget.currentIndex() + number_level - 5)


def center_widget():
    desktop = QDesktopWidget().screenGeometry()
    x = (desktop.width() - widget.width()) // 2
    y = (desktop.height() - widget.height()) // 2
    widget.move(x, y)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = QtWidgets.QStackedWidget()

    number_level = 0
    sound_play = True

    sound_player = QMediaPlayer()
    sound_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile("resources\\audio\\click.mp3")))

    media_player = QMediaPlayer()
    background_music = QMediaPlaylist()
    background_music.addMedia(QMediaContent(QtCore.QUrl.fromLocalFile("resources\\audio\\Colorful Cat - Rurikon.mp3")))
    background_music.setPlaybackMode(QMediaPlaylist.Loop)
    media_player.setPlaylist(background_music)
    media_player.play()

    mainmenu_screen = Mainmenu()
    settings_screen = Settings()
    rules_screen = Rules()
    exit_screen = Exit()
    lose_screen = Lose()
    win_screen = Win()
    marker_screen = Marker()
    pillow_screen = Pillow()
    mokasin_screen = Mokasin()

    widget.addWidget(mainmenu_screen)   # 0
    widget.addWidget(settings_screen)   # 1
    widget.addWidget(rules_screen)     # 2
    widget.addWidget(exit_screen)   # 3
    widget.addWidget(lose_screen)   # 4
    widget.addWidget(win_screen)    # 5
    widget.addWidget(marker_screen)     # 6
    widget.addWidget(pillow_screen)     # 7
    widget.addWidget(mokasin_screen)    # 8

    widget.show()
    center_widget()
    app.exec()