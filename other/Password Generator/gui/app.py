import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from password_generator_gui import Ui_MainWindow


class PasswordGenerator(QMainWindow):
    def __init__(self):
        super(PasswordGenerator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PasswordGenerator()
    window.show()

    sys.exit(app.exec())
