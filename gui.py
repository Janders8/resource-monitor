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
        MainWindow.resize(699, 818)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 475, 743))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 230, 221, 431))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayoutCpu = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayoutCpu.setContentsMargins(0, 0, 0, 0)
        self.formLayoutCpu.setObjectName("formLayoutCpu")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayoutCpu.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textBrowserCpu = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowserCpu.setEnabled(True)
        self.textBrowserCpu.setMouseTracking(False)
        self.textBrowserCpu.setAcceptDrops(False)
        self.textBrowserCpu.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowserCpu.setObjectName("textBrowserCpu")
        self.formLayoutCpu.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textBrowserCpu)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayoutCpu.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.textBrowserCpuTemp = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.textBrowserCpuTemp.setEnabled(True)
        self.textBrowserCpuTemp.setMouseTracking(False)
        self.textBrowserCpuTemp.setAcceptDrops(False)
        self.textBrowserCpuTemp.setObjectName("textBrowserCpuTemp")
        self.formLayoutCpu.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textBrowserCpuTemp)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutCpu.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 171, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayoutRam = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayoutRam.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayoutRam.setContentsMargins(0, 0, 0, 0)
        self.formLayoutRam.setObjectName("formLayoutRam")
        self.textBrowserRamUsed = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowserRamUsed.setObjectName("textBrowserRamUsed")
        self.formLayoutRam.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textBrowserRamUsed)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayoutRam.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayoutRam.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.textBrowserRamTotal = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowserRamTotal.setObjectName("textBrowserRamTotal")
        self.formLayoutRam.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textBrowserRamTotal)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formLayoutRam.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.textBrowserRamPercent = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowserRamPercent.setObjectName("textBrowserRamPercent")
        self.formLayoutRam.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textBrowserRamPercent)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayoutRam.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(240, 20, 171, 161))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayoutGpu = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayoutGpu.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayoutGpu.setContentsMargins(0, 0, 0, 0)
        self.formLayoutGpu.setObjectName("formLayoutGpu")
        self.textBrowserGpuLoad = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.textBrowserGpuLoad.setObjectName("textBrowserGpuLoad")
        self.formLayoutGpu.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textBrowserGpuLoad)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.formLayoutGpu.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.textBrowserGpuMemory = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.textBrowserGpuMemory.setObjectName("textBrowserGpuMemory")
        self.formLayoutGpu.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textBrowserGpuMemory)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.formLayoutGpu.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.textBrowserGpuTemp = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.textBrowserGpuTemp.setObjectName("textBrowserGpuTemp")
        self.formLayoutGpu.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textBrowserGpuTemp)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.formLayoutGpu.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.textBrowserGpuName = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.textBrowserGpuName.setObjectName("textBrowserGpuName")
        self.formLayoutGpu.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.textBrowserGpuName)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.formLayoutGpu.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_11)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(270, 250, 171, 394))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayoutDisk = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayoutDisk.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayoutDisk.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayoutDisk.setContentsMargins(0, 0, 0, 0)
        self.formLayoutDisk.setObjectName("formLayoutDisk")
        self.textBrowserDiskName = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.textBrowserDiskName.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowserDiskName.setObjectName("textBrowserDiskName")
        self.formLayoutDisk.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.textBrowserDiskName)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_15.setAutoFillBackground(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.formLayoutDisk.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.textBrowserDiskReadActivity = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.textBrowserDiskReadActivity.setObjectName("textBrowserDiskReadActivity")
        self.formLayoutDisk.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textBrowserDiskReadActivity)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_16.setAutoFillBackground(False)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.formLayoutDisk.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.textBrowserDiskWriteActivity = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.textBrowserDiskWriteActivity.setObjectName("textBrowserDiskWriteActivity")
        self.formLayoutDisk.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textBrowserDiskWriteActivity)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_17.setAutoFillBackground(False)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.formLayoutDisk.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.textBrowserDiskTotalActivity = QtWidgets.QTextBrowser(self.formLayoutWidget_3)
        self.textBrowserDiskTotalActivity.setObjectName("textBrowserDiskTotalActivity")
        self.formLayoutDisk.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textBrowserDiskTotalActivity)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_18.setAutoFillBackground(False)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.formLayoutDisk.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_18)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.StartLogging = QtWidgets.QPushButton(self.centralwidget)
        self.StartLogging.setObjectName("StartLogging")
        self.horizontalLayout.addWidget(self.StartLogging)
        self.EndLogging = QtWidgets.QPushButton(self.centralwidget)
        self.EndLogging.setEnabled(False)
        self.EndLogging.setObjectName("EndLogging")
        self.horizontalLayout.addWidget(self.EndLogging)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 26))
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
        self.label_3.setText(_translate("MainWindow", "Cores"))
        self.label_7.setText(_translate("MainWindow", "Temps:"))
        self.label.setText(_translate("MainWindow", "CPU:"))
        self.label_4.setText(_translate("MainWindow", "Used"))
        self.label_5.setText(_translate("MainWindow", "% used"))
        self.label_6.setText(_translate("MainWindow", "Total"))
        self.label_2.setText(_translate("MainWindow", "Ram"))
        self.label_12.setText(_translate("MainWindow", "Load"))
        self.label_13.setText(_translate("MainWindow", "Memory"))
        self.label_14.setText(_translate("MainWindow", "Temperature"))
        self.label_11.setText(_translate("MainWindow", "GPU:"))
        self.label_15.setText(_translate("MainWindow", "Read Activity"))
        self.label_16.setText(_translate("MainWindow", "Write Activity"))
        self.label_17.setText(_translate("MainWindow", "Total activity"))
        self.label_18.setText(_translate("MainWindow", "Disk"))
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
