import sys
from PyQt5.QtWidgets import QDialog, QApplication
from calculator_gui import Ui_Calculator
from calculator import Calculator


class CalculatorWindow(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        calc_obj = Calculator(self.ui)
        calc_obj.set_event_listeners()
        self.show()


app = QApplication(sys.argv)
window = CalculatorWindow()
window.show()
sys.exit(app.exec_())
