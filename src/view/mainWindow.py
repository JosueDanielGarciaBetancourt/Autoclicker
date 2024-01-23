# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(363, 259)
        MainWindow.setMinimumSize(QtCore.QSize(290, 218))
        MainWindow.setMaximumSize(QtCore.QSize(500, 260))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Programas propios/Python/Autoclicker/src/view/Autoclicker_Icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("\n"
"QMenuBar { color: black;}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 331, 211))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setMidLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.page_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 321, 171))
        self.groupBox_2.setStyleSheet("QGroupBox { border: 0; }")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: red;")
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.groupBox = QtWidgets.QGroupBox(parent=self.page_4)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 351, 91))
        self.groupBox.setStyleSheet("QGroupBox { border: 0; }")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.doubleSpinBoxInterval = QtWidgets.QDoubleSpinBox(parent=self.groupBox)
        self.doubleSpinBoxInterval.setGeometry(QtCore.QRect(210, 10, 62, 22))
        self.doubleSpinBoxInterval.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.doubleSpinBoxInterval.setAccelerated(False)
        self.doubleSpinBoxInterval.setProperty("showGroupSeparator", False)
        self.doubleSpinBoxInterval.setMaximum(10.0)
        self.doubleSpinBoxInterval.setSingleStep(1.0)
        self.doubleSpinBoxInterval.setStepType(QtWidgets.QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.doubleSpinBoxInterval.setObjectName("doubleSpinBoxInterval")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(280, 10, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 60, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBoxKey = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBoxKey.setGeometry(QtCore.QRect(130, 60, 101, 22))
        self.comboBoxKey.setObjectName("comboBoxKey")
        self.comboBoxKey.addItem("")
        self.comboBoxKey.addItem("")
        self.pushButtonDetectarTecla = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonDetectarTecla.setGeometry(QtCore.QRect(250, 50, 61, 41))
        self.pushButtonDetectarTecla.setObjectName("pushButtonDetectarTecla")
        self.groupBox2 = QtWidgets.QGroupBox(parent=self.page_4)
        self.groupBox2.setGeometry(QtCore.QRect(80, 110, 161, 91))
        self.groupBox2.setStyleSheet("QGroupBox { border: 0; }")
        self.groupBox2.setTitle("")
        self.groupBox2.setObjectName("groupBox2")
        self.pushButtonEmpezar = QtWidgets.QPushButton(parent=self.groupBox2)
        self.pushButtonEmpezar.setGeometry(QtCore.QRect(10, 30, 61, 31))
        self.pushButtonEmpezar.setObjectName("pushButtonEmpezar")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.groupBox2)
        self.groupBox_4.setGeometry(QtCore.QRect(270, 90, 321, 91))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(parent=self.groupBox_4)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(210, 10, 62, 22))
        self.doubleSpinBox_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.doubleSpinBox_4.setAccelerated(False)
        self.doubleSpinBox_4.setProperty("showGroupSeparator", False)
        self.doubleSpinBox_4.setStepType(QtWidgets.QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(280, 10, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.groupBox_4)
        self.comboBox_4.setGeometry(QtCore.QRect(130, 50, 81, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 40, 61, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButtonPausar = QtWidgets.QPushButton(parent=self.groupBox2)
        self.pushButtonPausar.setGeometry(QtCore.QRect(90, 30, 61, 31))
        self.pushButtonPausar.setObjectName("pushButtonPausar")
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 363, 22))
        self.menubar.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuInicio = QtWidgets.QMenu(parent=self.menubar)
        self.menuInicio.setTearOffEnabled(False)
        self.menuInicio.setSeparatorsCollapsible(False)
        self.menuInicio.setToolTipsVisible(False)
        self.menuInicio.setObjectName("menuInicio")
        MainWindow.setMenuBar(self.menubar)
        self.actionInicio = QtGui.QAction(parent=MainWindow)
        self.actionInicio.setCheckable(False)
        self.actionInicio.setChecked(False)
        self.actionInicio.setShortcutContext(QtCore.Qt.ShortcutContext.WindowShortcut)
        self.actionInicio.setObjectName("actionInicio")
        self.actionAcercaDe = QtGui.QAction(parent=MainWindow)
        self.actionAcercaDe.setObjectName("actionAcercaDe")
        self.menuInicio.addAction(self.actionInicio)
        self.menuInicio.addSeparator()
        self.menuInicio.addAction(self.actionAcercaDe)
        self.menubar.addAction(self.menuInicio.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.comboBoxKey.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Autoclicker "))
        self.label_4.setText(_translate("MainWindow", "Autor"))
        self.label_5.setText(_translate("MainWindow", "Cualquier uso fuera de las políticas y/o reglas \n"
"de otros programas, queda bajo la responsabilidad \n"
"del usuario."))
        self.label_6.setText(_translate("MainWindow", " josueelpapi123"))
        self.label_7.setText(_translate("MainWindow", "Advertencia"))
        self.label_2.setText(_translate("MainWindow", "Intervalo de click  (sugerido 0.05):"))
        self.label_3.setText(_translate("MainWindow", "seg"))
        self.label.setText(_translate("MainWindow", "Tecla de activación:"))
        self.comboBoxKey.setItemText(0, _translate("MainWindow", "H"))
        self.comboBoxKey.setItemText(1, _translate("MainWindow", "Y"))
        self.pushButtonDetectarTecla.setText(_translate("MainWindow", "Detectar \n"
"tecla"))
        self.pushButtonEmpezar.setText(_translate("MainWindow", "Empezar"))
        self.label_10.setText(_translate("MainWindow", "Intervalo de click  (sugerido 0.05):"))
        self.label_11.setText(_translate("MainWindow", "seg"))
        self.label_12.setText(_translate("MainWindow", "Tecla de activación:"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Scroll click"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "H"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Y"))
        self.pushButton_4.setText(_translate("MainWindow", "Detectar \n"
"tecla"))
        self.pushButtonPausar.setText(_translate("MainWindow", "Pausar"))
        self.menuInicio.setTitle(_translate("MainWindow", "Menú"))
        self.actionInicio.setText(_translate("MainWindow", "Inicio"))
        self.actionAcercaDe.setText(_translate("MainWindow", "Acerca de"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
