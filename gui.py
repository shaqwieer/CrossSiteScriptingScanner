# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from operator import index
import PyQt5 
from PyQt5 import QtCore, QtGui, QtWidgets

import Crawler as cr
import Scanner as scan
import Encoding as en
import Encryption as crypt
import Browser as br
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time
import threading



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.found= []
        self.links = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 616))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Crawl_input = QtWidgets.QLineEdit(self.tab)
        self.Crawl_input.setGeometry(QtCore.QRect(10, 40, 541, 36))
        self.Crawl_input.setObjectName("Crawl_input")
        self.numberofsites = QtWidgets.QLCDNumber(self.tab)
        self.numberofsites.setGeometry(QtCore.QRect(485, 85, 66, 21))
        self.numberofsites.setObjectName("numberofsites")
        self.crawl_btn = QtWidgets.QPushButton(self.tab)
        self.crawl_btn.setGeometry(QtCore.QRect(595, 75, 121, 31))
        self.crawl_btn.setObjectName("crawl_btn")
        self.Craw_output = QtWidgets.QPlainTextEdit(self.tab)
        self.Craw_output.setGeometry(QtCore.QRect(10, 120, 766, 356))
        self.Craw_output.setPlainText("")
        self.Craw_output.setObjectName("Craw_output")
        self.depth_select = QtWidgets.QSpinBox(self.tab)
        self.depth_select.setGeometry(QtCore.QRect(595, 40, 51, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.depth_select.setFont(font)
        self.depth_select.setObjectName("depth_select")
        self.coutfile = QtWidgets.QLineEdit(self.tab)
        self.coutfile.setGeometry(QtCore.QRect(200, 505, 361, 20))
        self.coutfile.setObjectName("coutfile")
        self.file_browse = QtWidgets.QPushButton(self.tab)
        self.file_browse.setGeometry(QtCore.QRect(575, 505, 75, 23))
        self.file_browse.setObjectName("file_browse")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(136, 510, 61, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(655, 45, 66, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(430, 90, 51, 10))
        self.label_4.setObjectName("label_4")
        self.crawl_save = QtWidgets.QPushButton(self.tab)
        self.crawl_save.setGeometry(QtCore.QRect(355, 535, 75, 23))
        self.crawl_save.setObjectName("crawl_save")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scaninputselect = QtWidgets.QComboBox(self.tab_3)
        self.scaninputselect.setGeometry(QtCore.QRect(30, 55, 91, 22))
        self.scaninputselect.setObjectName("scaninputselect")
        self.scaninputselect.addItems(["single url","file"])
        self.Scanner_input = QtWidgets.QLineEdit(self.tab_3)
        self.Scanner_input.setGeometry(QtCore.QRect(145, 55, 421, 20))
        self.Scanner_input.setObjectName("Scanner_input")
        self.scanfileselect = QtWidgets.QPushButton(self.tab_3)
        self.scanfileselect.setGeometry(QtCore.QRect(585, 55, 75, 23))
        self.scanfileselect.setObjectName("scanfileselect")
        self.find_forms_btn = QtWidgets.QPushButton(self.tab_3)
        self.find_forms_btn.setGeometry(QtCore.QRect(30, 95, 96, 23))
        self.find_forms_btn.setObjectName("find_forms_btn")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(145, 40, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.listWidget = QtWidgets.QListWidget(self.tab_3)
        self.listWidget.setGeometry(QtCore.QRect(25, 135, 531, 411))
        self.listWidget.setObjectName("listWidget")
        self.scanner_start_btn = QtWidgets.QPushButton(self.tab_3)
        self.scanner_start_btn.setGeometry(QtCore.QRect(590, 300, 181, 46))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scanner_start_btn.setFont(font)
        self.scanner_start_btn.setObjectName("scanner_start_btn")
        self.scan_status = QtWidgets.QLabel(self.tab_3)
        self.scan_status.setGeometry(QtCore.QRect(600, 355, 180, 180))
        self.scan_status.setObjectName("scan_status")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(575, 140, 91, 16))
        self.label_8.setObjectName("label_8")
        self.payload_select = QtWidgets.QComboBox(self.tab_3)
        self.payload_select.setGeometry(QtCore.QRect(665, 135, 101, 22))
        self.payload_select.setObjectName("payload_select")
        self.payload_select.addItems(["XSS single payload","SQLi single payload","XSS payload file","SQLi payload file"])
        self.payload_input = QtWidgets.QLineEdit(self.tab_3)
        self.payload_input.setGeometry(QtCore.QRect(570, 185, 201, 20))
        self.payload_input.setObjectName("payload_input")
        self.payload_file_input = QtWidgets.QPushButton(self.tab_3)
        self.payload_file_input.setGeometry(QtCore.QRect(570, 215, 75, 23))
        self.payload_file_input.setObjectName("payload_file_input")
        self.payload_file_input.setEnabled(False)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.encode_input = QtWidgets.QPlainTextEdit(self.tab_4)
        self.encode_input.setGeometry(QtCore.QRect(20, 85, 576, 176))
        self.encode_input.setObjectName("encode_input")
        self.encode_output = QtWidgets.QPlainTextEdit(self.tab_4)
        self.encode_output.setGeometry(QtCore.QRect(20, 330, 576, 176))
        self.encode_output.setObjectName("encode_output")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(25, 50, 76, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(20, 295, 76, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.encode_type = QtWidgets.QComboBox(self.tab_4)
        self.encode_type.setGeometry(QtCore.QRect(630, 165, 136, 22))
        self.encode_type.setObjectName("encode_type")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(630, 145, 106, 16))
        self.label_11.setObjectName("label_11")
        self.encode = QtWidgets.QRadioButton(self.tab_4)
        self.encode.setGeometry(QtCore.QRect(630, 110, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.encode.setFont(font)
        self.encode.setObjectName("encode")
        self.decode = QtWidgets.QRadioButton(self.tab_4)
        self.decode.setGeometry(QtCore.QRect(709, 110, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.decode.setFont(font)
        self.decode.setObjectName("decode")
        self.encode_start = QtWidgets.QPushButton(self.tab_4)
        self.encode_start.setGeometry(QtCore.QRect(660, 205, 75, 23))
        self.encode_start.setObjectName("encode_start")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.enc_output = QtWidgets.QPlainTextEdit(self.tab_5)
        self.enc_output.setGeometry(QtCore.QRect(20, 330, 576, 176))
        self.enc_output.setObjectName("enc_output")
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setGeometry(QtCore.QRect(25, 50, 76, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.encrypt_type = QtWidgets.QComboBox(self.tab_5)
        self.encrypt_type.setGeometry(QtCore.QRect(630, 165, 136, 22))
        self.encrypt_type.setObjectName("encrypt_type")
        self.enc_input = QtWidgets.QPlainTextEdit(self.tab_5)
        self.enc_input.setGeometry(QtCore.QRect(20, 85, 576, 176))
        self.enc_input.setObjectName("enc_input")
        self.decrypt = QtWidgets.QRadioButton(self.tab_5)
        self.decrypt.setGeometry(QtCore.QRect(710, 110, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.decrypt.setFont(font)
        self.decrypt.setObjectName("decrypt")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(20, 295, 76, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.encrypt = QtWidgets.QRadioButton(self.tab_5)
        self.encrypt.setGeometry(QtCore.QRect(630, 110, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.encrypt.setFont(font)
        self.encrypt.setObjectName("encrypt")
        self.label_14 = QtWidgets.QLabel(self.tab_5)
        self.label_14.setGeometry(QtCore.QRect(630, 145, 106, 16))
        self.label_14.setObjectName("label_14")
        self.encrypt_start = QtWidgets.QPushButton(self.tab_5)
        self.encrypt_start.setGeometry(QtCore.QRect(660, 205, 75, 23))
        self.encrypt_start.setObjectName("encrypt_start")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.hash_input = QtWidgets.QPlainTextEdit(self.tab_2)
        self.hash_input.setGeometry(QtCore.QRect(20, 85, 576, 176))
        self.hash_input.setObjectName("hash_input")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(20, 295, 76, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.hash_output = QtWidgets.QPlainTextEdit(self.tab_2)
        self.hash_output.setGeometry(QtCore.QRect(20, 330, 576, 176))
        self.hash_output.setObjectName("hash_output")
        self.hash_type = QtWidgets.QComboBox(self.tab_2)
        self.hash_type.setGeometry(QtCore.QRect(630, 165, 136, 22))
        self.hash_type.setObjectName("hash_type")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(630, 145, 106, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(25, 50, 76, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.hash_start = QtWidgets.QPushButton(self.tab_2)
        self.hash_start.setGeometry(QtCore.QRect(660, 205, 75, 23))
        self.hash_start.setObjectName("hash_start")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton = QtWidgets.QPushButton(self.tab_6)
        self.pushButton.setGeometry(QtCore.QRect(490, 100, 106, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.tab_6)
        self.label_5.setGeometry(QtCore.QRect(35, 60, 586, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setLineWidth(7)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        self.label_7.setGeometry(QtCore.QRect(35, 95, 576, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)
        self.label_20 = QtWidgets.QLabel(self.tab_7)
        self.label_20.setGeometry(QtCore.QRect(35, 60, 586, 410))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setLineWidth(7)
        self.label_20.setObjectName("label_20")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Website Analysis & Penetration Testing"))
        self.crawl_btn.setText(_translate("MainWindow", "Crawl"))
        self.file_browse.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "URL:"))
        self.label_2.setText(_translate("MainWindow", "Output File:"))
        self.label_3.setText(_translate("MainWindow", "Crawl Depth"))
        self.label_4.setText(_translate("MainWindow", "No of links"))
        self.crawl_save.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Crawler"))
        self.scanfileselect.setText(_translate("MainWindow", "Browse"))
        self.scanfileselect.setEnabled(False)
        self.find_forms_btn.setText(_translate("MainWindow", "Find Forms"))
        self.label_6.setText(_translate("MainWindow", "URL:"))
        self.scanner_start_btn.setText(_translate("MainWindow", "Scan"))
        self.scan_status.setText(_translate("MainWindow", "STATUS:"))
        self.label_8.setText(_translate("MainWindow", "Choose Payload:"))
        self.payload_file_input.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Scanner"))
        self.label_9.setText(_translate("MainWindow", "Input:"))
        self.label_10.setText(_translate("MainWindow", "Output:"))
        self.label_11.setText(_translate("MainWindow", "choose the type:"))
        self.encode.setText(_translate("MainWindow", "Encode"))
        self.decode.setText(_translate("MainWindow", "Decode"))
        self.encode_start.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "encoder/decoder"))
        self.label_12.setText(_translate("MainWindow", "Input:"))
        self.decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.label_13.setText(_translate("MainWindow", "Output:"))
        self.encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.label_14.setText(_translate("MainWindow", "choose the type:"))
        self.encrypt_start.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "encryption"))
        self.label_15.setText(_translate("MainWindow", "Output:"))
        self.label_16.setText(_translate("MainWindow", "choose the type:"))
        self.label_17.setText(_translate("MainWindow", "Input:"))
        self.hash_start.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "hashing"))
        self.pushButton.setText(_translate("MainWindow", "Open Browser"))
        self.label_5.setText(_translate("MainWindow", "To help you in your testing and keep results away from your Browser"))
        self.label_20.setText(_translate("MainWindow", "\t\t\tMilitary Technical College\n\t\t         Electrical Engineering Branch\n\t\t\t      A Major Project\n\t\t\t\t    on\n\t\t  “Website Analysis & Penetration Testing”\n\t\t\t  Submitted in fulfillment\n\t\t         For the award of the Degree of\n\t\t\t     Bachelor of Science\n\t       In Computer and Artificial Intelligence Department\n\n\nSubmitted by Cadets:\nAhmed Ehab Kamel Abousaif\nMohamed Khaled Shaqwieer\nHamdy Nasser Ahmed\nBadr el-din El-sayed El-Moghazi\nOsama Radwan Borhan El-Din\nUnder Supervision: Col. Dr. Khaled AbdelFatah "))
        self.label_7.setText(_translate("MainWindow", " we have provided our own safe browser for testing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "help"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "about us"))
        self.crawl_btn.clicked.connect(self.crawling)
        self.file_browse.clicked.connect(self.browse)
        self.scaninputselect.currentIndexChanged.connect(self.selectionchange1)
        self.payload_select.currentIndexChanged.connect(self.selectionchange2)
        self.scanfileselect.clicked.connect(self.get_links)
        self.find_forms_btn.clicked.connect(self.find_forms)
        self.scanner_start_btn.clicked.connect(self.scan)

    def crawler(self,MainWindow,start_domain,found_urls, depth):
        if (start_domain not in found_urls) and (len(urlparse(start_domain).path.split('/'))<=depth): #checking if url is already found and verifying its depth
            start = time.time() #a timer to close the connection
            while(True and (time.time()-start<10)):
                try:
                    req = Request(start_domain) #open the url
                    html = urlopen(req).read().decode('utf-8',"ignore")
                    found_urls.append(start_domain) #add to found_urls
                    MainWindow.Craw_output.insertPlainText(start_domain+"\n")
                    self.numberofsites.display(len(self.found))
                    self.numberofsites.update()
                    print(start_domain)
                    break
                except Exception as e:
                    print(e)
                    continue
            domain_html= BeautifulSoup(html,'html5lib')
            tags = domain_html.find_all("a",{"href": True}) #find all a tags with href values in them
            hrefs = []
            for tag in tags: #going through each tag and extracting the href
                href = tag['href']
                href_netloc = urlparse(href).netloc 
                if (href != '#'): #checking if href is local
                    if (href_netloc == '' or href_netloc == urlparse(start_domain).netloc ): #checking if href is a path or if it is or another domain
                        if(href_netloc == ''):
                            href_new = urljoin(start_domain,href) # joining the path to the original domain
                            if href_new not in hrefs:    
                                hrefs.append(href_new)
                        elif href not in hrefs:    
                            hrefs.append(href)
            for href in hrefs:                    
                self.crawler(self,href,found_urls,depth) #recursion

    def crawling(self):
        url = self.Crawl_input.text()
        domain = urlparse(url).netloc
        x = "http://"+domain
        depth = self.depth_select.value()
        self.found= []
        depth+=2
        threading.Thread(target=self.crawler,args=(self,x,self.found,depth)).start()
        # for url in self.found:
        #     self.Craw_output.insertPlainText(url+"\n")
        self.numberofsites.display(len(self.found))
        self.numberofsites.update()
        
    def browse(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self.centralwidget, 'Save File')
        try:
            file = open(name[0]+".txt",'w')
            file.write("\n".join(self.found))
            file.close()
        except Exception as e:
            print(e)
    def selectionchange1(self):
        if(self.scaninputselect.currentText() == "single url"):
            self.scanfileselect.setEnabled(False)
            self.Scanner_input.setEnabled(True)
        else:
            self.scanfileselect.setEnabled(True)
            self.Scanner_input.setEnabled(False)
    def selectionchange2(self):
        if(self.payload_select.currentText() == "XSS single payload" or self.payload_select.currentText() == "SQLi single payload"):
            self.payload_file_input.setEnabled(False)
            self.payload_input.setEnabled(True)
        else:
            self.payload_file_input.setEnabled(True)
            self.payload_input.setEnabled(False)
    
    def get_links(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, 'open File')
        try:
            file = open(name[0],'r')
            self.links = file.read().splitlines()
            file.close()
        except Exception as e:
            print(e)

    def find_forms(self):
        if(self.scaninputselect.currentText() == "single url"):
            url = self.Scanner_input.text()
            forms = scan.get_forms(url)
            print(forms)
            forms = scan.get_forms(url)
            for i in range(len(forms["forms"])):
                self.listWidget.addItem(url+","+"#"+str(i+1))
        else:
            forms=[]
            for url in self.links:
                forms = scan.get_forms(url)
                for i in range(len(forms["forms"])):
                    self.listWidget.addItem(url+","+"#"+str(i+1))
    def scan(self):
        url = self.listWidget.selectedItems()[0].text()
        url , index = url.split(",#")[0] , int(url.split(",#")[1])
        if(self.payload_select.currentText() == "XSS single payload" or self.payload_select.currentText() == "SQLi single payload"):
            payload = self.payload_input.text()
            if(self.payload_select.currentText() == "XSS single payload"):
                result = scan.xss(scan.get_forms(url)["url"],scan.get_forms(url)["forms"][index-1],payload)
            else:
                result = scan.sqli_forms(scan.get_forms(url)["url"],scan.get_forms(url)["forms"][index-1])
            if(result):
                self.scan_status.setFont(QtGui.QFont('Arial', 18))
                self.scan_status.setStyleSheet("color: red")
                self.scan_status.setText("Vulnerable")
            else:
                self.scan_status.setFont(QtGui.QFont('Arial', 18))
                self.scan_status.setStyleSheet("color: green")
                self.scan_status.setText("Safe")

        else:
            self.payload_file_input.setEnabled(True)
            self.payload_input.setEnabled(False)
        
    

                
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())