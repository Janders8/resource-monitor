# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 818)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 486, 743))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 201, 171))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowserRamUsed = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowserRamUsed.setObjectName("textBrowserRamUsed")
        self.gridLayout.addWidget(self.textBrowserRamUsed, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.textBrowserRamPercent = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowserRamPercent.setObjectName("textBrowserRamPercent")
        self.gridLayout.addWidget(self.textBrowserRamPercent, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.textBrowserRamTotal = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowserRamTotal.setObjectName("textBrowserRamTotal")
        self.gridLayout.addWidget(self.textBrowserRamTotal, 3, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 270, 201, 431))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.textBrowserCpu = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowserCpu.setEnabled(True)
        self.textBrowserCpu.setMouseTracking(False)
        self.textBrowserCpu.setAcceptDrops(False)
        self.textBrowserCpu.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowserCpu.setObjectName("textBrowserCpu")
        self.gridLayout_2.addWidget(self.textBrowserCpu, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.textBrowserCpuTemp = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowserCpuTemp.setEnabled(True)
        self.textBrowserCpuTemp.setMaximumSize(QtCore.QSize(256, 41))
        self.textBrowserCpuTemp.setMouseTracking(False)
        self.textBrowserCpuTemp.setAcceptDrops(False)
        self.textBrowserCpuTemp.setAutoFillBackground(False)
        self.textBrowserCpuTemp.setObjectName("textBrowserCpuTemp")
        self.gridLayout_2.addWidget(self.textBrowserCpuTemp, 2, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setGeometry(QtCore.QRect(220, 290, 251, 241))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setAutoFillBackground(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)
        self.textBrowserDiskWriteSpeed = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowserDiskWriteSpeed.setObjectName("textBrowserDiskWriteSpeed")
        self.gridLayout_3.addWidget(self.textBrowserDiskWriteSpeed, 2, 1, 1, 1)
        self.textBrowserDiskReadSpeed = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowserDiskReadSpeed.setObjectName("textBrowserDiskReadSpeed")
        self.gridLayout_3.addWidget(self.textBrowserDiskReadSpeed, 1, 1, 1, 1)
        self.textBrowserDiskTotalSpeed = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowserDiskTotalSpeed.setObjectName("textBrowserDiskTotalSpeed")
        self.gridLayout_3.addWidget(self.textBrowserDiskTotalSpeed, 3, 1, 1, 1)
        self.textBrowserDiskWaitTime = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowserDiskWaitTime.setObjectName("textBrowserDiskWaitTime")
        self.gridLayout_3.addWidget(self.textBrowserDiskWaitTime, 4, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setAutoFillBackground(False)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setAutoFillBackground(False)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setAutoFillBackground(False)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 3, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setAutoFillBackground(False)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 4, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setGeometry(QtCore.QRect(230, 30, 231, 232))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowserGpuLoad = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowserGpuLoad.setObjectName("textBrowserGpuLoad")
        self.gridLayout_4.addWidget(self.textBrowserGpuLoad, 2, 1, 1, 1)
        self.textBrowserGpuName = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowserGpuName.setObjectName("textBrowserGpuName")
        self.gridLayout_4.addWidget(self.textBrowserGpuName, 1, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 2)
        self.textBrowserGpuMemory = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowserGpuMemory.setObjectName("textBrowserGpuMemory")
        self.gridLayout_4.addWidget(self.textBrowserGpuMemory, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 4, 0, 1, 1)
        self.textBrowserGpuTemp = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowserGpuTemp.setObjectName("textBrowserGpuTemp")
        self.gridLayout_4.addWidget(self.textBrowserGpuTemp, 4, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.StartLogging = QtWidgets.QPushButton(self.centralwidget)
        self.StartLogging.setObjectName("StartLogging")
        self.gridLayout_5.addWidget(self.StartLogging, 0, 1, 1, 1)
        self.EndLogging = QtWidgets.QPushButton(self.centralwidget)
        self.EndLogging.setEnabled(False)
        self.EndLogging.setObjectName("EndLogging")
        self.gridLayout_5.addWidget(self.EndLogging, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Ram"))
        self.label_5.setText(_translate("MainWindow", "used [%]"))
        self.label_4.setText(_translate("MainWindow", "Used [GB]"))
        self.label_6.setText(_translate("MainWindow", "Total [GB"))
        self.label_7.setText(_translate("MainWindow", "Temps [C]"))
        self.label_3.setText(_translate("MainWindow", "Cores [%]"))
        self.label.setText(_translate("MainWindow", "CPU:"))
        self.label_15.setText(_translate("MainWindow", "Read speed [MB/s]"))
        self.label_16.setText(_translate("MainWindow", "Write speed [MB/s]"))
        self.label_18.setText(_translate("MainWindow", "Disk"))
        self.label_17.setText(_translate("MainWindow", "Total speed [MB/s]"))
        self.label_19.setText(_translate("MainWindow", "Wait Time [ms]"))
        self.label_13.setText(_translate("MainWindow", "Memory [%]"))
        self.label_12.setText(_translate("MainWindow", "Load [%]"))
        self.label_11.setText(_translate("MainWindow", "GPU:"))
        self.label_14.setText(_translate("MainWindow", "Temperature [C]"))
        self.StartLogging.setText(_translate("MainWindow", "Start logging"))
        self.EndLogging.setText(_translate("MainWindow", "End logging"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
