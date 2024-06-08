from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)
import icon_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 213)
        MainWindow.setMaximumSize(QSize(700, 213))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "QWidget {background-color: #1e1e1e;font-size: 13pt;}\n"
            "QPushButton {color: white;border: none;padding: 5px;background-color: #2a2a2a;border-radius: 5px;}\n"
            "QPushButton::checked {background-color: #2d5bd4;}\n"
            "QPushButton::pressed {background-color: #2D5BD4;}\n"
            "QLineEdit {border: none;border-radius: 5px;color: #d8d8d8;font-size: 14pt;font-weight: bold;background-color: #404040;padding: 5px;}\n"
            "QSpinBox {border: none;border-radius: 5px;color: #d8d8d8;font-size: 14pt;font-weight: bold;background-color: #404040;padding: 5px;}"
        )
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.lineEdit_password = QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.horizontalLayout.addWidget(self.lineEdit_password)

        self.pushButton_copy = QPushButton(self.centralwidget)
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.pushButton_copy.setEnabled(True)
        self.pushButton_copy.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(
            ":/icon/content_copy_24dp_FILL0_wght400_GRAD0_opsz24.svg",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.pushButton_copy.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton_copy)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, 20)
        self.horizontalSlider_length = QSlider(self.centralwidget)
        self.horizontalSlider_length.setObjectName("horizontalSlider_length")
        self.horizontalSlider_length.setCursor(QCursor(Qt.SizeHorCursor))
        self.horizontalSlider_length.setAutoFillBackground(True)
        self.horizontalSlider_length.setMaximum(100)
        self.horizontalSlider_length.setValue(12)
        self.horizontalSlider_length.setTracking(True)
        self.horizontalSlider_length.setOrientation(Qt.Horizontal)
        self.horizontalSlider_length.setInvertedAppearance(False)
        self.horizontalSlider_length.setInvertedControls(False)
        self.horizontalSlider_length.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_2.addWidget(self.horizontalSlider_length)

        self.spinBox_length = QSpinBox(self.centralwidget)
        self.spinBox_length.setObjectName("spinBox_length")
        self.spinBox_length.setAlignment(Qt.AlignCenter)
        self.spinBox_length.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_length.setMaximum(100)
        self.spinBox_length.setValue(12)

        self.horizontalLayout_2.addWidget(self.spinBox_length)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, 20)
        self.pushButton_lower = QPushButton(self.centralwidget)
        self.pushButton_lower.setObjectName("pushButton_lower")
        self.pushButton_lower.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_lower.setCheckable(True)
        self.pushButton_lower.setChecked(True)

        self.horizontalLayout_3.addWidget(self.pushButton_lower)

        self.pushButton_upper = QPushButton(self.centralwidget)
        self.pushButton_upper.setObjectName("pushButton_upper")
        self.pushButton_upper.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_upper.setCheckable(True)
        self.pushButton_upper.setChecked(True)

        self.horizontalLayout_3.addWidget(self.pushButton_upper)

        self.pushButton_digits = QPushButton(self.centralwidget)
        self.pushButton_digits.setObjectName("pushButton_digits")
        self.pushButton_digits.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_digits.setCheckable(True)
        self.pushButton_digits.setChecked(True)

        self.horizontalLayout_3.addWidget(self.pushButton_digits)

        self.pushButton_symbols = QPushButton(self.centralwidget)
        self.pushButton_symbols.setObjectName("pushButton_symbols")
        self.pushButton_symbols.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_symbols.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton_symbols)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Password Generator", None)
        )
        self.pushButton_copy.setText(
            QCoreApplication.translate("MainWindow", "copy", None)
        )
        self.pushButton_lower.setText(
            QCoreApplication.translate("MainWindow", "a-z", None)
        )
        self.pushButton_upper.setText(
            QCoreApplication.translate("MainWindow", "A-Z", None)
        )
        self.pushButton_digits.setText(
            QCoreApplication.translate("MainWindow", "0-9", None)
        )
        self.pushButton_symbols.setText(
            QCoreApplication.translate("MainWindow", "#$%", None)
        )

    # retranslateUi
