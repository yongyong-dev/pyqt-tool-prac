from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QMenuBar

import sys
from qt_material import apply_stylesheet

screen_width = 500
screen_height = 300


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setup_main_ui()
        self.setWindowTitle("Debug Tool")

        self.show()

    def setup_main_ui(self):
        self.resize(screen_width, screen_height)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
