import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QCloseEvent

from password_generator_gui import Ui_MainWindow

import buttons
import password


class PasswordGenerator(QMainWindow):
    def __init__(self):
        super(PasswordGenerator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect_slider_to_spinbox()
        self.set_password()
        self.ui.pushButton_copy.clicked.connect(self.copy_to_clipboard)

    def connect_slider_to_spinbox(self) -> None:
        self.ui.horizontalSlider_length.valueChanged.connect(
            self.ui.spinBox_length.setValue
        )
        self.ui.spinBox_length.valueChanged.connect(
            self.ui.horizontalSlider_length.setValue
        )
        self.ui.spinBox_length.valueChanged.connect(self.set_password)

    def get_characters(self) -> str:
        chars = ""
        for btn in buttons.Characters:
            if getattr(self.ui, btn.name).isChecked():
                chars += btn.value
        return chars

    def set_password(self) -> None:
        try:
            self.ui.lineEdit_password.setText(
                password.create_new(
                    length=self.ui.horizontalSlider_length.value(),
                    characters=self.get_characters(),
                )
            )
        except IndexError:
            self.ui.lineEdit_password.clear()

    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.ui.lineEdit_password.text())

    def closeEvent(self, event: QCloseEvent()) -> None:
        QApplication.clipboard().clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PasswordGenerator()
    window.show()

    sys.exit(app.exec())
