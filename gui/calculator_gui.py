from PyQt5 import QtCore, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        number_button_style = "background-color: #fff; color:#000; border:1px solid #000; font-size:25px; border-radius:20px; font-weight:600;"
        operation_button_style = "background-color: #286090; color:#fff; font-size:25px; border-radius:20px; font-weight:600;"
        
        Calculator.setObjectName("Calculator")
        Calculator.resize(438, 697)
        Calculator.setMaximumSize(QtCore.QSize(438, 697))

        self.verticalLayout = QtWidgets.QVBoxLayout(Calculator)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.Container = QtWidgets.QFrame(Calculator)
        self.Container.setStyleSheet("background-color: #fff")
        self.Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Container.setObjectName("Container")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Container)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.Display1 = QtWidgets.QFrame(self.Container)
        self.Display1.setMinimumSize(QtCore.QSize(0, 90))
        self.Display1.setMaximumSize(QtCore.QSize(16777215, 90))
        self.Display1.setStyleSheet("background-color: #fff")
        self.Display1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Display1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Display1.setObjectName("Display1")
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Display1)
        self.horizontalLayout_3.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.FinalResult = QtWidgets.QLabel(self.Display1)
        self.FinalResult.setStyleSheet("border:5px solid #d9d9d9;font: 30px 'Oswald'}")
        self.FinalResult.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.FinalResult.setObjectName("FinalResult")
        self.horizontalLayout_3.addWidget(self.FinalResult)
        self.verticalLayout_2.addWidget(self.Display1)
        
        self.Display2 = QtWidgets.QFrame(self.Container)
        self.Display2.setMinimumSize(QtCore.QSize(0, 60))
        self.Display2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.Display2.setStyleSheet("background-color: #fff")
        self.Display2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Display2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Display2.setObjectName("Display2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Display2)
        self.horizontalLayout_2.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.Calculation = QtWidgets.QLabel(self.Display2)
        self.Calculation.setStyleSheet("border:5px solid #d9d9d9; font: 20px 'Oswald'")
        self.Calculation.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.Calculation.setObjectName("Calculation")
        self.horizontalLayout_2.addWidget(self.Calculation)
        self.verticalLayout_2.addWidget(self.Display2)
        
        self.Keys = QtWidgets.QFrame(self.Container)
        self.Keys.setStyleSheet("background-color: #fff")
        self.Keys.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Keys.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Keys.setObjectName("Keys")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Keys)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.key_container1 = QtWidgets.QFrame(self.Keys)
        self.key_container1.setStyleSheet("background-color: #fff")
        self.key_container1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.key_container1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.key_container1.setObjectName("key_container1")

        self.gridLayout = QtWidgets.QGridLayout(self.key_container1)
        self.gridLayout.setContentsMargins(9, 9, 9, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_ac = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_ac.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_ac.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_ac.setStyleSheet(
            "background-color: #c9302c; color:#fff; font-size:25px; border-radius:20px; font-weight:600; "
        )
        self.pushButton_ac.setObjectName("pushButton_ac")
        self.gridLayout.addWidget(self.pushButton_ac, 0, 0, 1, 1)

        self.pushButton_ce = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_ce.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_ce.setStyleSheet(
            "background-color: #c9302c; color:#fff; font-size:25px; border-radius:20px; font-weight:600; "
        )
        self.pushButton_ce.setObjectName("pushButton_ce")
        self.gridLayout.addWidget(self.pushButton_ce, 0, 1, 1, 1)

        self.pushButton_percentage = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_percentage.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_percentage.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_percentage.setStyleSheet(operation_button_style)
        self.pushButton_percentage.setObjectName("pushButton_percentage")
        self.gridLayout.addWidget(self.pushButton_percentage, 0, 2, 1, 1)

        self.pushButton_div = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_div.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_div.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_div.setStyleSheet(operation_button_style)
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout.addWidget(self.pushButton_div, 0, 3, 1, 1)

        self.pushButton_7 = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_7.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_7.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_7.setStyleSheet(number_button_style)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_8 = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_8.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_8.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_8.setStyleSheet(number_button_style)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_9 = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_9.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_9.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_9.setStyleSheet(number_button_style)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_mul = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_mul.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_mul.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_mul.setStyleSheet(operation_button_style)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout.addWidget(self.pushButton_mul, 1, 3, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_4.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_4.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_4.setStyleSheet(number_button_style)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_5.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_5.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_5.setStyleSheet(number_button_style)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_6 = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_6.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_6.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_6.setStyleSheet(number_button_style)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_sub = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_sub.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_sub.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_sub.setStyleSheet(operation_button_style)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout.addWidget(self.pushButton_sub, 2, 3, 1, 1)

        self.pushButton_1 = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_1.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_1.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_1.setStyleSheet(number_button_style)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_2.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_2.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_2.setStyleSheet(number_button_style)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_3.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_3.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_3.setStyleSheet(number_button_style)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_add = QtWidgets.QPushButton(self.key_container1)
        self.pushButton_add.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_add.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_add.setStyleSheet(operation_button_style)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 3, 3, 1, 1)

        self.verticalLayout_3.addWidget(self.key_container1)
        self.key_container2 = QtWidgets.QFrame(self.Keys)
        self.key_container2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.key_container2.setStyleSheet("background-color: #fff")
        self.key_container2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.key_container2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.key_container2.setObjectName("key_container2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.key_container2)
        self.horizontalLayout.setContentsMargins(-1, 0, 9, -1)

        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_0 = QtWidgets.QPushButton(self.key_container2)
        self.pushButton_0.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_0.setMaximumSize(QtCore.QSize(300, 90))
        self.pushButton_0.setStyleSheet(number_button_style)
        self.pushButton_0.setObjectName("pushButton_0")
        self.horizontalLayout.addWidget(self.pushButton_0)

        self.pushButton_dot = QtWidgets.QPushButton(self.key_container2)
        self.pushButton_dot.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_dot.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_dot.setStyleSheet(number_button_style)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.horizontalLayout.addWidget(self.pushButton_dot)

        self.pushButton_equal = QtWidgets.QPushButton(self.key_container2)
        self.pushButton_equal.setMinimumSize(QtCore.QSize(90, 90))
        self.pushButton_equal.setMaximumSize(QtCore.QSize(90, 90))
        self.pushButton_equal.setStyleSheet(
            "background-color: #31b0d5; color:#fff; font-size:25px; border-radius:20px; font-weight:600; "
        )
        self.pushButton_equal.setObjectName("pushButton_equal")

        self.horizontalLayout.addWidget(self.pushButton_equal)
        self.verticalLayout_3.addWidget(self.key_container2)
        self.verticalLayout_2.addWidget(self.Keys)
        self.verticalLayout.addWidget(self.Container)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Form"))
        self.FinalResult.setText(_translate("Calculator", "0"))
        self.Calculation.setText(_translate("Calculator", "0"))
        self.pushButton_ac.setText(_translate("Calculator", "AC"))
        self.pushButton_percentage.setText(_translate("Calculator", "⁒"))
        self.pushButton_div.setText(_translate("Calculator", "÷"))
        self.pushButton_7.setText(_translate("Calculator", "7"))
        self.pushButton_8.setText(_translate("Calculator", "8"))
        self.pushButton_9.setText(_translate("Calculator", "9"))
        self.pushButton_mul.setText(_translate("Calculator", "×"))
        self.pushButton_4.setText(_translate("Calculator", "4"))
        self.pushButton_5.setText(_translate("Calculator", "5"))
        self.pushButton_6.setText(_translate("Calculator", "6"))
        self.pushButton_sub.setText(_translate("Calculator", "−"))
        self.pushButton_1.setText(_translate("Calculator", "1"))
        self.pushButton_2.setText(_translate("Calculator", "2"))
        self.pushButton_3.setText(_translate("Calculator", "3"))
        self.pushButton_add.setText(_translate("Calculator", "+"))
        self.pushButton_ce.setText(_translate("Calculator", "CE"))
        self.pushButton_0.setText(_translate("Calculator", "0"))
        self.pushButton_dot.setText(_translate("Calculator", "•"))
        self.pushButton_equal.setText(_translate("Calculator", "="))
