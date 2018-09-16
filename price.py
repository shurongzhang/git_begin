# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'price.ui'
#
# Created: Sat Sep 15 18:17:47 2018
#      by: PyQt5 UI code generator 5.0
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.price_box = QtWidgets.QTextEdit(self.centralwidget)
        self.price_box.setGeometry(QtCore.QRect(160, 140, 131, 51))
        self.price_box.setObjectName("price_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 160, 81, 21))
        self.label.setStyleSheet("color: rgb(255, 0, 255);\n"
"font: 75 24pt \"Aharoni\";")
        self.label.setObjectName("label")
        self.tax_rate = QtWidgets.QSpinBox(self.centralwidget)
        self.tax_rate.setGeometry(QtCore.QRect(150, 220, 42, 22))
        self.tax_rate.setProperty("value", 20)
        self.tax_rate.setObjectName("tax_rate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 220, 54, 12))
        self.label_2.setObjectName("label_2")
        self.PuahButton = QtWidgets.QPushButton(self.centralwidget)
        self.PuahButton.setGeometry(QtCore.QRect(150, 270, 131, 61))
        self.PuahButton.setObjectName("PuahButton")
        self.results_window = QtWidgets.QTextEdit(self.centralwidget)
        self.results_window.setGeometry(QtCore.QRect(400, 200, 261, 71))
        self.results_window.setObjectName("results_window")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 50, 301, 31))
        self.label_3.setStyleSheet("color: rgb(255, 0, 255);\n"
"font: 75 24pt \"Aharoni\";")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.PuahButton.clicked.connect(self.CalculateTax)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Price"))
        self.label_2.setText(_translate("MainWindow", "tax_rate"))
        self.PuahButton.setText(_translate("MainWindow", "calc_tax_button"))
        self.label_3.setText(_translate("MainWindow", "sale box caculator"))
        #self.price_box.setText("helloworld")
        #self.results_window.setText("helloworld")
        # price= (self.price_box.toPlainText())
        # tax = str(self.tax_rate.value())
        # self.results_window.setText(tax)
    def CalculateTax(self):
        #self.price_box.setText("helloworld")
        #self.results_window.setText("helloworld")
        price= int(self.price_box.toPlainText())
        tax = int(self.tax_rate.value())
        total_price = str(price * tax)
        self.results_window.setText(total_price)
        #total_price = (price + ((tax / 100) * price))
        
        #total_price_string = "The total price with tax is: " + str(total_price)
 #定义槽函数	
		
		
		#price = int(self.price_box.toPlainText())

   #def CalculateTax(self, MainWindow):
        # price = int(self.price_box.toPlainText())
        # tax = (self.tax_rate.value())
        # total_price = price  + ((tax / 100) * price)
        # total_price_string = "The total price with tax is: " + str(total_price)
        # self.results_window.setText(total_price_string)            

        
if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
       ng=QtGui.QPixmap('/home/capture/Pictures/Selection_026.png')
    File = open('/home/capture/eric6_test/auto_k2_all/test1.log')
    ui.setupUi(Form) 
    Form.show()
    sys.exit(app.exec_())


