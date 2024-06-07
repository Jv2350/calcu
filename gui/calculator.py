from sympy import sympify
from sympy.core.sympify import SympifyError


class Calculator:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.eval_string = ""
        self.memory = 0  # To store memory values

    def show_output(self, text):
        self.ui.FinalResult.setText(text)

    def show_input(self, text):
        if text in "+-*/" and (not self.eval_string or self.eval_string[-1] in "+-*/"):
            return
        self.eval_string += text
        self.ui.Calculation.setText(self.eval_string)

    def clear(self):
        self.eval_string = ""
        self.ui.Calculation.setText("0")
        self.ui.FinalResult.setText("0")

    def clear_last_entry(self):
        self.eval_string = self.eval_string[:-1]
        self.ui.Calculation.setText(self.eval_string if self.eval_string else "0")

    def evaluate(self):
        try:
            result = sympify(self.eval_string)
            self.show_output(str(result))
        except (SympifyError, ZeroDivisionError):
            self.show_output("Error")

    def set_event_listeners(self):
        self.ui.pushButton_ac.clicked.connect(lambda: self.clear())
        self.ui.pushButton_ce.clicked.connect(lambda: self.clear_last_entry())
        self.ui.pushButton_percentage.clicked.connect(lambda: self.show_input("*0.01"))
        self.ui.pushButton_div.clicked.connect(lambda: self.show_input("/"))
        self.ui.pushButton_7.clicked.connect(lambda: self.show_input("7"))
        self.ui.pushButton_8.clicked.connect(lambda: self.show_input("8"))
        self.ui.pushButton_9.clicked.connect(lambda: self.show_input("9"))
        self.ui.pushButton_mul.clicked.connect(lambda: self.show_input("*"))
        self.ui.pushButton_4.clicked.connect(lambda: self.show_input("4"))
        self.ui.pushButton_5.clicked.connect(lambda: self.show_input("5"))
        self.ui.pushButton_6.clicked.connect(lambda: self.show_input("6"))
        self.ui.pushButton_sub.clicked.connect(lambda: self.show_input("-"))
        self.ui.pushButton_1.clicked.connect(lambda: self.show_input("1"))
        self.ui.pushButton_2.clicked.connect(lambda: self.show_input("2"))
        self.ui.pushButton_3.clicked.connect(lambda: self.show_input("3"))
        self.ui.pushButton_add.clicked.connect(lambda: self.show_input("+"))
        self.ui.pushButton_0.clicked.connect(lambda: self.show_input("0"))
        self.ui.pushButton_dot.clicked.connect(lambda: self.show_input("."))
        self.ui.pushButton_equal.clicked.connect(lambda: self.evaluate())
