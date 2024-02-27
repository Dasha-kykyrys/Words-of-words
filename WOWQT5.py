from PyQt5 import QtWidgets
from mainmenu import Ui_mainmenu

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_mainmenu()
        self.ui.setupUi(self)

        #self.ui.Play.clicked.connect(self.lvlmenu)

    #def lvlmenu(self):
       # self.ui = Ui_Levelmenu()
       # self.ui.setupUi(self)




app = QtWidgets.QApplication([])
application = Window()
application.show()
app.exec()
