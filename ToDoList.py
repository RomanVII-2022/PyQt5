from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(396, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add_it())
        self.addItem_pushButton.setGeometry(QtCore.QRect(10, 70, 101, 41))
        self.addItem_pushButton.setObjectName("addItem_pushButton")
        self.deleteitem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_it())
        self.deleteitem_pushButton.setGeometry(QtCore.QRect(130, 70, 111, 41))
        self.deleteitem_pushButton.setObjectName("deleteitem_pushButton")
        self.clear_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clear_it())
        self.clear_pushButton.setGeometry(QtCore.QRect(264, 70, 111, 41))
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(10, 10, 371, 51))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 130, 371, 261))
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 396, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_it(self):
        item = self.additem_lineEdit.text()
        self.mylist_listWidget.addItem(item)
        self.additem_lineEdit.setText('')

    def clear_it(self):
        self.mylist_listWidget.clear()


    def delete_it(self):
        clicked = self.mylist_listWidget.currentRow()
        self.mylist_listWidget.takeItem(clicked)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.addItem_pushButton.setText(_translate("MainWindow", "Add Item"))
        self.deleteitem_pushButton.setText(_translate("MainWindow", "Delete Item"))
        self.clear_pushButton.setText(_translate("MainWindow", "clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
