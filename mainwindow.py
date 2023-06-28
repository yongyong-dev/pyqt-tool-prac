import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog, QListView, QTableView, \
    QWidget, QHBoxLayout
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Trace Viewer')
        self.resize(800, 600)

        # Create menu bar
        menu_bar = self.menuBar()
        # under this function is for macOS
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('File')

        # Create submenus
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        close_action = QAction('Close', self)
        close_action.triggered.connect(self.close)
        file_menu.addAction(close_action)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.exit_app)
        file_menu.addAction(exit_action)

        # Create list view and table view
        list_view = QListView()
        table_view = QTableView()

        # Set size of list view and table view
        list_view.setMaximumWidth(int(0.25 * self.width()))
        table_view.setMinimumWidth(int(0.75 * self.width()))

        # Set central widget
        central_widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(list_view)
        layout.addWidget(table_view)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def resizeEvent(self, event):
        list_view = self.centralWidget().layout().itemAt(0).widget()
        table_view = self.centralWidget().layout().itemAt(1).widget()

        list_view.setMaximumWidth(int(0.25 * event.size().width()))
        table_view.setMinimumWidth(int(0.75 * event.size().width()))

    def open_file(self):
        home_dir = QFileDialog.getExistingDirectory(self, 'Select Home Directory')
        binary_file_path = QFileDialog.getOpenFileName(self, 'Select Binary File')[0]

    def exit_app(self):
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # Show the window
    window.show()

    # Run the event loop
    sys.exit(app.exec_())