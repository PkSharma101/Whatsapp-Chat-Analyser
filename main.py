# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import _thread
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import subprocess
import analysis as ais
import pdfkit
from stemplate import *

class Ui_MainWindow(object):
    chatfile = ""
    resultfile = ""
    report = "Report/"
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 536)
        MainWindow.setMinimumSize(QtCore.QSize(600, 536))
        MainWindow.setMaximumSize(QtCore.QSize(600, 536))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 281, 331))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 40, 251, 23))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 100, 241, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 70, 261, 23))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 130, 241, 23))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 160, 241, 23))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 190, 241, 23))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 220, 241, 23))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 250, 241, 23))
        self.checkBox_8.setObjectName("checkBox_8")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox_2)
        self.buttonBox.setGeometry(QtCore.QRect(170, 290, 81, 25))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 311, 251))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(300, 270, 301, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(290, 0, 20, 281))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(300, 390, 291, 101))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 141, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 60, 101, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 67, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(80, 30, 191, 17))
        self.label_8.setObjectName("label_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 281, 131))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(150, 40, 101, 25))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 40, 131, 21))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 141, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(160, 90, 111, 17))
        self.label_4.setObjectName("label_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(300, 290, 291, 91))
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 271, 51))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Whatsapp Chat Analysis"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Select the Options for Analysis"))
        self.checkBox.setText(_translate("MainWindow", "Rate of Messages wrt date"))
        self.checkBox_2.setText(_translate("MainWindow", "Top 10 Emoji Usage"))
        self.checkBox_3.setText(_translate("MainWindow", "Rate of Messages wrt time"))
        self.checkBox_4.setText(_translate("MainWindow", "List of people"))
        self.checkBox_5.setText(_translate("MainWindow", "List of URL "))
        self.checkBox_6.setText(_translate("MainWindow", "List of Numbers "))
        self.checkBox_7.setText(_translate("MainWindow", "Count of Image FIles"))
        self.checkBox_8.setText(_translate("MainWindow", "Word Cloud of messages"))
        self.groupBox.setTitle(_translate("MainWindow", "Results"))
        self.label_6.setText(_translate("MainWindow", "Click here to open : "))
        self.pushButton_2.setText(_translate("MainWindow", "Open"))
        self.pushButton_2.clicked.connect(self.result)

        self.label_7.setText(_translate("MainWindow", "Status : "))
        self.label_8.setText(_translate("MainWindow", "N/A"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Chat selection"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton.clicked.connect(self.filesys)

        self.label.setText(_translate("MainWindow", "Select the txt file :"))
        self.label_3.setText(_translate("MainWindow", "The selected file is :"))
        self.label_4.setText(_translate("MainWindow", "N/A"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Method to Export chart"))
        self.label_5.setText(_translate("MainWindow", "More > Export Chat > Without Media"))
        self.buttonBox.clicked.connect(self.option)

    def analyze(self,op):
        doc = header
        if self.chatfile:
            if 1 in op:
                ais.plot_rate_date(self.chatfile)
                doc+=rmd
            if 2 in op:
                ais.plot_rate_time(self.chatfile)
                doc+=rmt
            if 3 in op:
                ais.plot_emoji(self.chatfile)
                doc+=emoji_start
            if 4 in op:
                _,fname = ais.unq_people(self.chatfile)
                doc+=up_start
                fname_std = " ".join("<li>"+name+"</li>" for name in fname)
                doc= doc + fname_std + up_end
            if 5 in op:
                _,lurl = ais.get_url(self.chatfile)
                
                doc += url_start
                lurl_std = " ".join("<li>"+name_url+" : "+xurl+"</li>" for name_url,xurl in lurl)
                doc= doc + lurl_std + up_end
            if 6 in op:
                numberdb,_ = ais.get_number(self.chatfile)
                doc += phn_start
                fphn = []
                for phn_list in numberdb.values():
                    for num in phn_list:
                        if len(num)>5:
                            fphn.append(num)
                lurl_std = " ".join("<li>"+phn+"</li>" for phn in fphn)
                doc= doc + lurl_std + up_end
            if 7 in op:
                ais.image_count(self.chatfile)
                doc+=media
            if 8 in op:
                cfiles, names = ais.get_cloud(self.chatfile)
                doc += wc_start
                lurl_std = " ".join("<h5>"+ wc_name+"</h5><img src="+wc+"><br>" for wc, wc_name in zip(cfiles, names))
                doc= doc + lurl_std + up_end
            doc+=footer
            cname = self.chatfile.split(".")[0].split("/")[-1]    
            self.resultfile = "output_"+cname+".pdf"
            with open("temp.html","w") as file:
                file.write(doc)
            self.export()
        else:
            self.label_8.setText("Select the File")

    def export(self): 
        #print("Resultttttttttttttt   ",self.resultfile)
        pdfkit.from_file('temp.html', "Report/"+self.resultfile)
        os.remove('temp.html')
        self.label_8.setText("Ready") 
    
    def filesys(self):
        fname = QtWidgets.QFileDialog.getOpenFileName()
        name = fname[0].split("/")[-1]
        self.chatfile = fname[0]
        self.label_4.setText(name)
    
    def result(self):
        if self.resultfile:
            subprocess.Popen("evince Report/'%s'" % self.resultfile,shell=True)
        else:
            self.label_8.setText("Select Options first")
    
    def option(self):
        op = []
        if self.checkBox.isChecked():
            op.append(1)
        if self.checkBox_2.isChecked():
            op.append(3)
        if self.checkBox_3.isChecked():
            op.append(2)
        if self.checkBox_4.isChecked():
            op.append(4)
        if self.checkBox_5.isChecked():
            op.append(5)
        if self.checkBox_6.isChecked():
            op.append(6)
        if self.checkBox_7.isChecked():
            op.append(7)
        if self.checkBox_8.isChecked():
            op.append(8)
        self.label_8.setText("Processing....")
        _thread.start_new_thread( self.analyze,(op,))

        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
