# Form implementation generated from reading ui file 'dialogDetectarTecla.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dialogDetectarTecla(object):
    def setupUi(self, dialogDetectarTecla):
        dialogDetectarTecla.setObjectName("dialogDetectarTecla")
        dialogDetectarTecla.resize(256, 65)
        self.label_2 = QtWidgets.QLabel(parent=dialogDetectarTecla)
        self.label_2.setGeometry(QtCore.QRect(10, -10, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(dialogDetectarTecla)
        QtCore.QMetaObject.connectSlotsByName(dialogDetectarTecla)

    def retranslateUi(self, dialogDetectarTecla):
        _translate = QtCore.QCoreApplication.translate
        dialogDetectarTecla.setWindowTitle(_translate("dialogDetectarTecla", "Detectar tecla"))
        self.label_2.setText(_translate("dialogDetectarTecla", "Presione cualquier tecla o click (no left click)\n"
"para asignarla como tecla de activación"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogDetectarTecla = QtWidgets.QDialog()
    ui = Ui_dialogDetectarTecla()
    ui.setupUi(dialogDetectarTecla)
    dialogDetectarTecla.show()
    sys.exit(app.exec())
