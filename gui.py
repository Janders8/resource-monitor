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
        MainWindow.resize(866, 664)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 842, 589))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 280, 30))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 73, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.textBrowserRamPercent = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserRamPercent.setGeometry(QtCore.QRect(120, 60, 200, 30))
        self.textBrowserRamPercent.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserRamPercent.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserRamPercent.setFont(font)
        self.textBrowserRamPercent.setObjectName("textBrowserRamPercent")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 73, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.textBrowserRamUsed = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserRamUsed.setGeometry(QtCore.QRect(120, 100, 200, 30))
        self.textBrowserRamUsed.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserRamUsed.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserRamUsed.setFont(font)
        self.textBrowserRamUsed.setObjectName("textBrowserRamUsed")
        self.textBrowserRamTotal = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserRamTotal.setGeometry(QtCore.QRect(120, 140, 200, 30))
        self.textBrowserRamTotal.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserRamTotal.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserRamTotal.setFont(font)
        self.textBrowserRamTotal.setObjectName("textBrowserRamTotal")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 73, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(30, 180, 280, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowserCpu = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserCpu.setEnabled(True)
        self.textBrowserCpu.setGeometry(QtCore.QRect(120, 210, 200, 331))
        self.textBrowserCpu.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserCpu.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserCpu.setFont(font)
        self.textBrowserCpu.setMouseTracking(False)
        self.textBrowserCpu.setAcceptDrops(False)
        self.textBrowserCpu.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowserCpu.setObjectName("textBrowserCpu")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 73, 311))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setGeometry(QtCore.QRect(20, 550, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textBrowserCpuTemp = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserCpuTemp.setEnabled(True)
        self.textBrowserCpuTemp.setGeometry(QtCore.QRect(120, 550, 200, 30))
        self.textBrowserCpuTemp.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserCpuTemp.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserCpuTemp.setFont(font)
        self.textBrowserCpuTemp.setMouseTracking(False)
        self.textBrowserCpuTemp.setAcceptDrops(False)
        self.textBrowserCpuTemp.setAutoFillBackground(False)
        self.textBrowserCpuTemp.setObjectName("textBrowserCpuTemp")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setGeometry(QtCore.QRect(310, 30, 344, 16))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setGeometry(QtCore.QRect(360, 140, 100, 30))
        self.label_12.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_12.setFont(font)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.textBrowserGpuLoad = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserGpuLoad.setGeometry(QtCore.QRect(480, 140, 141, 30))
        self.textBrowserGpuLoad.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserGpuLoad.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserGpuLoad.setFont(font)
        self.textBrowserGpuLoad.setObjectName("textBrowserGpuLoad")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setGeometry(QtCore.QRect(360, 180, 100, 30))
        self.label_13.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_13.setFont(font)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.textBrowserGpuMemory = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserGpuMemory.setGeometry(QtCore.QRect(480, 180, 141, 30))
        self.textBrowserGpuMemory.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserGpuMemory.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserGpuMemory.setFont(font)
        self.textBrowserGpuMemory.setObjectName("textBrowserGpuMemory")
        self.textBrowserGpuName = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserGpuName.setGeometry(QtCore.QRect(340, 60, 281, 60))
        self.textBrowserGpuName.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserGpuName.setMaximumSize(QtCore.QSize(500, 60))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserGpuName.setFont(font)
        self.textBrowserGpuName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowserGpuName.setObjectName("textBrowserGpuName")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setGeometry(QtCore.QRect(360, 220, 100, 30))
        self.label_14.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_14.setFont(font)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.textBrowserGpuTemp = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserGpuTemp.setGeometry(QtCore.QRect(480, 220, 141, 30))
        self.textBrowserGpuTemp.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserGpuTemp.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserGpuTemp.setFont(font)
        self.textBrowserGpuTemp.setObjectName("textBrowserGpuTemp")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setGeometry(QtCore.QRect(330, 260, 320, 22))
        self.label_18.setAutoFillBackground(False)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.textBrowserDiskModel = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserDiskModel.setGeometry(QtCore.QRect(340, 290, 281, 50))
        self.textBrowserDiskModel.setMinimumSize(QtCore.QSize(250, 0))
        self.textBrowserDiskModel.setMaximumSize(QtCore.QSize(300, 50))
        self.textBrowserDiskModel.setBaseSize(QtCore.QSize(0, 0))
        self.textBrowserDiskModel.setObjectName("textBrowserDiskModel")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setGeometry(QtCore.QRect(360, 350, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_21.setFont(font)
        self.label_21.setAutoFillBackground(False)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.textBrowserDiskUsage = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserDiskUsage.setGeometry(QtCore.QRect(490, 350, 130, 30))
        self.textBrowserDiskUsage.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserDiskUsage.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserDiskUsage.setFont(font)
        self.textBrowserDiskUsage.setObjectName("textBrowserDiskUsage")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setGeometry(QtCore.QRect(360, 430, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_16.setFont(font)
        self.label_16.setAutoFillBackground(False)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.textBrowserDiskReadSpeed = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserDiskReadSpeed.setGeometry(QtCore.QRect(490, 390, 130, 30))
        self.textBrowserDiskReadSpeed.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserDiskReadSpeed.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserDiskReadSpeed.setFont(font)
        self.textBrowserDiskReadSpeed.setObjectName("textBrowserDiskReadSpeed")
        self.textBrowserDiskTotalSpeed = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserDiskTotalSpeed.setGeometry(QtCore.QRect(490, 470, 130, 30))
        self.textBrowserDiskTotalSpeed.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserDiskTotalSpeed.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserDiskTotalSpeed.setFont(font)
        self.textBrowserDiskTotalSpeed.setObjectName("textBrowserDiskTotalSpeed")
        self.textBrowserDiskQueue = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserDiskQueue.setGeometry(QtCore.QRect(490, 550, 130, 30))
        self.textBrowserDiskQueue.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserDiskQueue.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserDiskQueue.setFont(font)
        self.textBrowserDiskQueue.setObjectName("textBrowserDiskQueue")
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setGeometry(QtCore.QRect(360, 550, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_20.setFont(font)
        self.label_20.setAutoFillBackground(False)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setGeometry(QtCore.QRect(360, 510, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_19.setFont(font)
        self.label_19.setAutoFillBackground(False)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setGeometry(QtCore.QRect(360, 390, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_15.setFont(font)
        self.label_15.setAutoFillBackground(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.textBrowserDiskWriteSpeed = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserDiskWriteSpeed.setGeometry(QtCore.QRect(490, 430, 130, 30))
        self.textBrowserDiskWriteSpeed.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserDiskWriteSpeed.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserDiskWriteSpeed.setFont(font)
        self.textBrowserDiskWriteSpeed.setObjectName("textBrowserDiskWriteSpeed")
        self.textBrowserDiskWaitTime = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserDiskWaitTime.setGeometry(QtCore.QRect(490, 510, 130, 30))
        self.textBrowserDiskWaitTime.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowserDiskWaitTime.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowserDiskWaitTime.setFont(font)
        self.textBrowserDiskWaitTime.setObjectName("textBrowserDiskWaitTime")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setGeometry(QtCore.QRect(360, 470, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_17.setFont(font)
        self.label_17.setAutoFillBackground(False)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setGeometry(QtCore.QRect(650, 20, 171, 16))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_9.setObjectName("label_9")
        self.comboBoxTests = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBoxTests.setGeometry(QtCore.QRect(650, 60, 171, 22))
        self.comboBoxTests.setMaximumSize(QtCore.QSize(16777215, 40))
        self.comboBoxTests.setObjectName("comboBoxTests")
        self.startTest = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.startTest.setGeometry(QtCore.QRect(650, 90, 171, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTest.sizePolicy().hasHeightForWidth())
        self.startTest.setSizePolicy(sizePolicy)
        self.startTest.setMaximumSize(QtCore.QSize(16777215, 40))
        self.startTest.setObjectName("startTest")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setGeometry(QtCore.QRect(650, 160, 171, 16))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_8.setObjectName("label_8")
        self.textBrowserTestTime = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserTestTime.setGeometry(QtCore.QRect(650, 190, 176, 30))
        self.textBrowserTestTime.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textBrowserTestTime.setObjectName("textBrowserTestTime")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setGeometry(QtCore.QRect(650, 300, 171, 16))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_10.setObjectName("label_10")
        self.textBrowserWHEA = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowserWHEA.setGeometry(QtCore.QRect(650, 340, 176, 30))
        self.textBrowserWHEA.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textBrowserWHEA.setObjectName("textBrowserWHEA")
        self.EndLogging = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.EndLogging.setEnabled(False)
        self.EndLogging.setGeometry(QtCore.QRect(740, 550, 85, 28))
        self.EndLogging.setObjectName("EndLogging")
        self.StartLogging = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.StartLogging.setGeometry(QtCore.QRect(649, 550, 85, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartLogging.sizePolicy().hasHeightForWidth())
        self.StartLogging.setSizePolicy(sizePolicy)
        self.StartLogging.setObjectName("StartLogging")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_8.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 866, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resource monitor"))
        self.label_2.setText(_translate("MainWindow", "RAM"))
        self.label_5.setText(_translate("MainWindow", "Used [%]"))
        self.label_4.setText(_translate("MainWindow", "Used [GB]"))
        self.label_6.setText(_translate("MainWindow", "Total [GB]"))
        self.label.setText(_translate("MainWindow", "CPU:"))
        self.label_3.setText(_translate("MainWindow", "Threads [%]"))
        self.label_7.setText(_translate("MainWindow", "Temperature [C]"))
        self.label_11.setText(_translate("MainWindow", "GPU:"))
        self.label_12.setText(_translate("MainWindow", "Load [%]"))
        self.label_13.setText(_translate("MainWindow", "Memory [%]"))
        self.label_14.setText(_translate("MainWindow", "Temperature [C]"))
        self.label_18.setText(_translate("MainWindow", "Disk"))
        self.label_21.setText(_translate("MainWindow", "Disk usage [%]"))
        self.label_16.setText(_translate("MainWindow", "Write speed [MB/s]"))
        self.label_20.setText(_translate("MainWindow", "Disk queue"))
        self.label_19.setText(_translate("MainWindow", "Wait Time [ms]"))
        self.label_15.setText(_translate("MainWindow", "Read speed [MB/s]"))
        self.label_17.setText(_translate("MainWindow", "Total speed [MB/s]"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Available tests</p></body></html>"))
        self.startTest.setText(_translate("MainWindow", "Start Test"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Time of executing test:</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">WHEA Error:</p></body></html>"))
        self.EndLogging.setText(_translate("MainWindow", "End logging"))
        self.StartLogging.setText(_translate("MainWindow", "Start logging"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
