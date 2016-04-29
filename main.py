# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(841, 690)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(90, 60, 661, 401))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(80, 240, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 280, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 320, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 240, 54, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 51, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 320, 54, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(550, 240, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 280, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 320, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 611, 192))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(50)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.QYolk = QtGui.QMenuBar(MainWindow)
        self.QYolk.setGeometry(QtCore.QRect(0, 0, 841, 23))
        self.QYolk.setObjectName(_fromUtf8("QYolk"))
        MainWindow.setMenuBar(self.QYolk)
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.lineEdit_2)
        self.label_3.setBuddy(self.lineEdit_3)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "  name0", None))
        self.label_2.setText(_translate("MainWindow", "name1", None))
        self.label_3.setText(_translate("MainWindow", "name2", None))
        self.pushButton.setText(_translate("MainWindow", "add", None))
        self.pushButton_2.setText(_translate("MainWindow", "save", None))
        self.pushButton_3.setText(_translate("MainWindow", "delete", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "name0", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "name1", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "name2", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "player1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "player2", None))
from PyQt4 import QtCore, QtGui,QtSql
import sys
import time

class StartQt4(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")  #select database type
        self.db.setHostName("localhost")
        self.db.setDatabaseName("test")   #set address
        self.db.setUserName("root")
        self.db.setPassword("")
        self.q=QtSql.QSqlQuery()
        if (self.db.open()):
            self.showdata()
        else:
            print "failed"
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("cellChanged(int, int)"), self.changedata)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.adddata)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.deldata)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.savedata)
        
    def changedata(self,row,col):
        co=self.tableWidget.columnCount()
        row =self.tableWidget.currentRow()
        col=self.tableWidget.currentColumn()
        a=self.tableWidget.horizontalHeaderItem(col).text()
        if (col < (co-1)):
            b=self.tableWidget.horizontalHeaderItem(col+1).text()
            t=self.tableWidget.item(row, col+1).text()
        elif (col == (co-1)):
            b=self.tableWidget.horizontalHeaderItem(col-1).text()
            t=self.tableWidget.item(row, col-1).text()
        dt=self.tableWidget.currentItem().text()
        self.q.exec_("update qiu set %s = '%s' where %s = %s " %(a,dt,b,t))
    
    def savedata(self):
        self.q.exec_("delete from qiu1")
        self.q.exec_("insert into qiu1 select distinct * from qiu")
        
    def deldata(self):
        row=self.tableWidget.currentRow()
        print row
        a=self.tableWidget.horizontalHeaderItem(0).text()
        x=self.tableWidget.item(row,0).text()
        self.q.exec_("delete from qiu where %s = '%s' " %(a,x))
        self.showdata()
    
    def adddata(self):
        name0 = str(self.lineEdit.text()) 
        name1 = str(self.lineEdit_2.text())
        name2 = str(self.lineEdit_3.text())
        self.q.exec_("insert into qiu values ('%s','%s','%s')" %(name0,name1,name2))
        self.showdata()
                
    def  showdata(self):
        self.tableWidget.clearContents()
        self.q.exec_("select * from qiu")
        col=self.tableWidget.columnCount()
        for i in range(0,self.tableWidget.rowCount()):
            self.q.next()
            for j in range(col):
                x=self.q.value(j).toString()
                self.tableWidget.setItem(i, j, QtGui.QTableWidgetItem(x))
              
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())
