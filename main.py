import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from show_scenery_rank.UI import showScenery

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = showScenery.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())