# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eediter.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("IML Encryption Editor")
        Form.resize(478, 316)
        Form.setStyleSheet("selection-background-color: rgb(0, 0, 0);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.save_btn = QtWidgets.QPushButton(Form)
        self.save_btn.setMinimumSize(QtCore.QSize(10, 50))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.save_btn.setFont(font)
        self.save_btn.setObjectName("save_btn")
        self.gridLayout.addWidget(self.save_btn, 1, 1, 1, 1)
        self.load_btn = QtWidgets.QPushButton(Form)
        self.load_btn.setMinimumSize(QtCore.QSize(10, 50))
        font = QtGui.QFont()
        font.setFamily("휴먼엑스포")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.load_btn.setFont(font)
        self.load_btn.setObjectName("load_btn")
        self.gridLayout.addWidget(self.load_btn, 1, 2, 1, 1)
        self.edit = QtWidgets.QPlainTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(13)
        self.edit.setFont(font)
        self.edit.setObjectName("edit")
        self.gridLayout.addWidget(self.edit, 2, 1, 1, 2)

        self.retranslateUi(Form)
        self.save_btn.clicked.connect(Form.slot1_save)
        self.load_btn.clicked.connect(Form.slot2_load)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("IML Encryption Editor", "IML Encryption Editor - New"))
        self.save_btn.setText(_translate("Form", "Save"))
        self.load_btn.setText(_translate("Form", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

