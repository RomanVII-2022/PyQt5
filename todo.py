from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

#create a database or connect to one
conn = sqlite3.connect('mylist.db')
# create a cursor
c = conn.cursor() 
# create a table 
c.execute("CREATE TABLE if not exists todo_list(list_item text)")

#commit the changes
conn.commit()

#close our connection
conn.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda : self.add_it())
        self.addItem_pushButton.setGeometry(QtCore.QRect(10, 70, 101, 41))
        self.addItem_pushButton.setObjectName("addItem_pushButton")
        self.deleteitem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_it())
        self.deleteitem_pushButton.setGeometry(QtCore.QRect(130, 70, 111, 41))
        self.deleteitem_pushButton.setObjectName("deleteitem_pushButton")
        self.clear_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.clear_it())
        self.clear_pushButton.setGeometry(QtCore.QRect(264, 70, 111, 41))
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(10, 10, 481, 51))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 130, 481, 261))
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        self.save_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.save_it())
        self.save_pushButton.setGeometry(QtCore.QRect(390, 70, 101, 41))
        self.save_pushButton.setObjectName("save_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Grab all the items from the database
        self.grab_all()

    def grab_all(self):
        #create a database or connect to one
        conn = sqlite3.connect('mylist.db')
        # create a cursor
        c = conn.cursor() 
        # Select from a table 
        c.execute('SELECT * FROM todo_list')
        records = c.fetchall()

        #commit the changes
        conn.commit()

        #close our connection
        conn.close()

        #loop thru records and add to screen
        for record in records:
            self.mylist_listWidget.addItem(str(record[0]))

    def add_it(self):
        item = self.additem_lineEdit.text()
        self.mylist_listWidget.addItem(item)
        self.additem_lineEdit.setText('')

    def delete_it(self):
        clicked = self.mylist_listWidget.currentRow()
        self.mylist_listWidget.takeItem(clicked)


    def clear_it(self):
        self.mylist_listWidget.clear()

    def save_it(self):
        #create a database or connect to one
        conn = sqlite3.connect('mylist.db')
        # create a cursor
        c = conn.cursor() 
        # Delete everything from database table 
        c.execute('DELETE FROM todo_list;',)

        items = []
        for index in range(self.mylist_listWidget.count()):
            items.append(self.mylist_listWidget.item(index))
        for item in items:
            c.execute("INSERT INTO todo_list VALUES (:item)",
            {
                'item': item.text(),
            })


        #commit the changes
        conn.commit()

        #close our connection
        conn.close()

        #pop_up message
        msg = QMessageBox()
        msg.setWindowTitle("Saved to Database")
        msg.setText('Your to do List has Been Saved')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.addItem_pushButton.setText(_translate("MainWindow", "Add Item"))
        self.deleteitem_pushButton.setText(_translate("MainWindow", "Delete Item"))
        self.clear_pushButton.setText(_translate("MainWindow", "clear"))
        self.save_pushButton.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
