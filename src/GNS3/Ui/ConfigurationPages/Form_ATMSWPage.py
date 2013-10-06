# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_ATMSWPage.ui'
#
# Created: Mon Sep  9 21:29:22 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ATMSWPage(object):
    def setupUi(self, ATMSWPage):
        ATMSWPage.setObjectName(_fromUtf8("ATMSWPage"))
        ATMSWPage.resize(482, 376)
        ATMSWPage.setWindowTitle(QtGui.QApplication.translate("ATMSWPage", "ATM Switch", None, QtGui.QApplication.UnicodeUTF8))
        self.gridlayout = QtGui.QGridLayout(ATMSWPage)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.checkBoxVPI = QtGui.QCheckBox(ATMSWPage)
        self.checkBoxVPI.setText(QtGui.QApplication.translate("ATMSWPage", "Use VPI only (VP tunnel)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxVPI.setObjectName(_fromUtf8("checkBoxVPI"))
        self.gridlayout.addWidget(self.checkBoxVPI, 0, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(ATMSWPage)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ATMSWPage", "Mapping", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.treeWidgetVCmap = QtGui.QTreeWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidgetVCmap.sizePolicy().hasHeightForWidth())
        self.treeWidgetVCmap.setSizePolicy(sizePolicy)
        self.treeWidgetVCmap.setRootIsDecorated(False)
        self.treeWidgetVCmap.setObjectName(_fromUtf8("treeWidgetVCmap"))
        self.treeWidgetVCmap.headerItem().setText(0, QtGui.QApplication.translate("ATMSWPage", "Port:VPI:VCI", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetVCmap.headerItem().setText(1, QtGui.QApplication.translate("ATMSWPage", "Port:VPI:VCI", None, QtGui.QApplication.UnicodeUTF8))
        self.vboxlayout.addWidget(self.treeWidgetVCmap)
        self.gridlayout.addWidget(self.groupBox_2, 0, 2, 4, 1)
        self.groupBox = QtGui.QGroupBox(ATMSWPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(QtGui.QApplication.translate("ATMSWPage", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("ATMSWPage", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout1.addWidget(self.label, 0, 0, 1, 1)
        self.spinBoxSrcPort = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxSrcPort.sizePolicy().hasHeightForWidth())
        self.spinBoxSrcPort.setSizePolicy(sizePolicy)
        self.spinBoxSrcPort.setMinimum(0)
        self.spinBoxSrcPort.setMaximum(65535)
        self.spinBoxSrcPort.setProperty("value", 1)
        self.spinBoxSrcPort.setObjectName(_fromUtf8("spinBoxSrcPort"))
        self.gridlayout1.addWidget(self.spinBoxSrcPort, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setText(QtGui.QApplication.translate("ATMSWPage", "VPI:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridlayout1.addWidget(self.label_5, 1, 0, 1, 1)
        self.spinBoxSrcVPI = QtGui.QSpinBox(self.groupBox)
        self.spinBoxSrcVPI.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxSrcVPI.sizePolicy().hasHeightForWidth())
        self.spinBoxSrcVPI.setSizePolicy(sizePolicy)
        self.spinBoxSrcVPI.setMaximum(65535)
        self.spinBoxSrcVPI.setProperty("value", 0)
        self.spinBoxSrcVPI.setObjectName(_fromUtf8("spinBoxSrcVPI"))
        self.gridlayout1.addWidget(self.spinBoxSrcVPI, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("ATMSWPage", "VCI:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout1.addWidget(self.label_2, 2, 0, 1, 1)
        self.spinBoxSrcVCI = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxSrcVCI.sizePolicy().hasHeightForWidth())
        self.spinBoxSrcVCI.setSizePolicy(sizePolicy)
        self.spinBoxSrcVCI.setMaximum(65535)
        self.spinBoxSrcVCI.setProperty("value", 100)
        self.spinBoxSrcVCI.setObjectName(_fromUtf8("spinBoxSrcVCI"))
        self.gridlayout1.addWidget(self.spinBoxSrcVCI, 2, 1, 1, 1)
        self.gridlayout.addWidget(self.groupBox, 1, 0, 1, 2)
        self.groupBox_3 = QtGui.QGroupBox(ATMSWPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ATMSWPage", "Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridlayout2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setText(QtGui.QApplication.translate("ATMSWPage", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout2.addWidget(self.label_3, 0, 0, 1, 1)
        self.spinBoxDestPort = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxDestPort.sizePolicy().hasHeightForWidth())
        self.spinBoxDestPort.setSizePolicy(sizePolicy)
        self.spinBoxDestPort.setMinimum(0)
        self.spinBoxDestPort.setMaximum(65535)
        self.spinBoxDestPort.setProperty("value", 10)
        self.spinBoxDestPort.setObjectName(_fromUtf8("spinBoxDestPort"))
        self.gridlayout2.addWidget(self.spinBoxDestPort, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setText(QtGui.QApplication.translate("ATMSWPage", "VPI:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridlayout2.addWidget(self.label_6, 1, 0, 1, 1)
        self.spinBoxDestVPI = QtGui.QSpinBox(self.groupBox_3)
        self.spinBoxDestVPI.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxDestVPI.sizePolicy().hasHeightForWidth())
        self.spinBoxDestVPI.setSizePolicy(sizePolicy)
        self.spinBoxDestVPI.setMaximum(65535)
        self.spinBoxDestVPI.setProperty("value", 0)
        self.spinBoxDestVPI.setObjectName(_fromUtf8("spinBoxDestVPI"))
        self.gridlayout2.addWidget(self.spinBoxDestVPI, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setText(QtGui.QApplication.translate("ATMSWPage", "VCI:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridlayout2.addWidget(self.label_4, 2, 0, 1, 1)
        self.spinBoxDestVCI = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxDestVCI.sizePolicy().hasHeightForWidth())
        self.spinBoxDestVCI.setSizePolicy(sizePolicy)
        self.spinBoxDestVCI.setMaximum(65535)
        self.spinBoxDestVCI.setProperty("value", 200)
        self.spinBoxDestVCI.setObjectName(_fromUtf8("spinBoxDestVCI"))
        self.gridlayout2.addWidget(self.spinBoxDestVCI, 2, 1, 1, 1)
        self.gridlayout.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.pushButtonAdd = QtGui.QPushButton(ATMSWPage)
        self.pushButtonAdd.setText(QtGui.QApplication.translate("ATMSWPage", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.gridlayout.addWidget(self.pushButtonAdd, 3, 0, 1, 1)
        self.pushButtonDelete = QtGui.QPushButton(ATMSWPage)
        self.pushButtonDelete.setEnabled(False)
        self.pushButtonDelete.setText(QtGui.QApplication.translate("ATMSWPage", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDelete.setObjectName(_fromUtf8("pushButtonDelete"))
        self.gridlayout.addWidget(self.pushButtonDelete, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(213, 31, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 4, 2, 1, 1)

        self.retranslateUi(ATMSWPage)
        QtCore.QMetaObject.connectSlotsByName(ATMSWPage)
        ATMSWPage.setTabOrder(self.checkBoxVPI, self.spinBoxSrcPort)
        ATMSWPage.setTabOrder(self.spinBoxSrcPort, self.spinBoxSrcVPI)
        ATMSWPage.setTabOrder(self.spinBoxSrcVPI, self.spinBoxSrcVCI)
        ATMSWPage.setTabOrder(self.spinBoxSrcVCI, self.spinBoxDestPort)
        ATMSWPage.setTabOrder(self.spinBoxDestPort, self.spinBoxDestVPI)
        ATMSWPage.setTabOrder(self.spinBoxDestVPI, self.spinBoxDestVCI)
        ATMSWPage.setTabOrder(self.spinBoxDestVCI, self.pushButtonAdd)
        ATMSWPage.setTabOrder(self.pushButtonAdd, self.pushButtonDelete)
        ATMSWPage.setTabOrder(self.pushButtonDelete, self.treeWidgetVCmap)

    def retranslateUi(self, ATMSWPage):
        pass
