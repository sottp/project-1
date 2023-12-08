# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(180, 227)
        MainWindow.setMinimumSize(QtCore.QSize(180, 227))
        MainWindow.setMaximumSize(QtCore.QSize(180, 227))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 100, 62, 14))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 120, 62, 14))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 160, 62, 14))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 140, 62, 14))
        self.radioButton_4.setObjectName("radioButton_4")
        self.calcbutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calcbutton.setGeometry(QtCore.QRect(100, 140, 61, 31))
        self.calcbutton.setObjectName("calcbutton")
        self.signspot = QtWidgets.QLabel(parent=self.centralwidget)
        self.signspot.setGeometry(QtCore.QRect(80, 40, 21, 21))
        self.signspot.setText("")
        self.signspot.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.signspot.setObjectName("signspot")
        self.input1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input1.setGeometry(QtCore.QRect(20, 40, 61, 20))
        self.input1.setObjectName("input1")
        self.input2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input2.setGeometry(QtCore.QRect(100, 40, 61, 21))
        self.input2.setObjectName("input2")
        self.clearbutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clearbutton.setGeometry(QtCore.QRect(100, 100, 61, 31))
        self.clearbutton.setObjectName("clearbutton")
        self.output = QtWidgets.QLabel(parent=self.centralwidget)
        self.output.setGeometry(QtCore.QRect(20, 70, 141, 21))
        self.output.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.output.setObjectName("output")
        self.biglabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.biglabel.setGeometry(QtCore.QRect(20, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(18)
        self.biglabel.setFont(font)
        self.biglabel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.biglabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.biglabel.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.biglabel.setLineWidth(1)
        self.biglabel.setScaledContents(False)
        self.biglabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.biglabel.setObjectName("biglabel")
        self.errorout = QtWidgets.QLabel(parent=self.centralwidget)
        self.errorout.setGeometry(QtCore.QRect(10, 170, 161, 21))
        self.errorout.setText("")
        self.errorout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.errorout.setObjectName("errorout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 180, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CALCULATER"))
        self.radioButton.setText(_translate("MainWindow", "Add"))
        self.radioButton_2.setText(_translate("MainWindow", "Subtract"))
        self.radioButton_3.setText(_translate("MainWindow", "Divide"))
        self.radioButton_4.setText(_translate("MainWindow", "Multiply"))
        self.calcbutton.setText(_translate("MainWindow", "Calculate"))
        self.clearbutton.setText(_translate("MainWindow", "Clear"))
        self.output.setText(_translate("MainWindow", "Result: "))
        self.biglabel.setText(_translate("MainWindow", "Calculater"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
