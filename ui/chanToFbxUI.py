# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/chanToFbxUI.ui'
#
# Created: Thu Aug 25 14:56:15 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(744, 409)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(744, 496))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgb(41, 41, 41);\n"
"    color: rgb(200, 200,200);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color: rgb(255, 165, 0);\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:disabled {\n"
"    color: rgb(128, 128, 128);\n"
"    border-color: rgb(128, 128, 128);\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: rgb(55, 55, 55);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid white;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: rgb(55, 55, 55);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: rgb(55, 55, 55);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QStackedWidget {\n"
"    border: 2px solid rgb(120, 120, 120);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QGroupBox#subGroupBox {\n"
"    border: 0px;\n"
"}\n"
"\n"
"#buttonBar {\n"
"    background-image: url(:/images/toolbarBg.png);\n"
"}\n"
"\n"
"QPushButton[flat=\'false\'] {\n"
"    border: 2px solid rgb(200, 200, 200);\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton[flat=\'false\']:pressed {\n"
"    border: 3px inset rgb(200, 200, 200);\n"
"}\n"
"QPushButton[flat=\'false\']:disabled {\n"
"    border: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"#convertButton {\n"
"    min-width: 60px;\n"
"    color: rgb(73, 255, 73);\n"
"}\n"
"#quitButton {\n"
"    min-width: 60px;\n"
"    color: rgb(255, 77, 73);\n"
"}\n"
"\n"
"#sourceFileButton,#outFileButton {\n"
"    min-width: 25px;\n"
"}\n"
"\n"
"QMessageBox { background-color: rgb(55, 55, 55); }\n"
"\n"
"#adFrame {\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(8, 6, 8, 6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.buttonBar = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBar.sizePolicy().hasHeightForWidth())
        self.buttonBar.setSizePolicy(sizePolicy)
        self.buttonBar.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonBar.setObjectName(_fromUtf8("buttonBar"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.buttonBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.settingsBtn = QtGui.QPushButton(self.buttonBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsBtn.sizePolicy().hasHeightForWidth())
        self.settingsBtn.setSizePolicy(sizePolicy)
        self.settingsBtn.setMinimumSize(QtCore.QSize(0, 54))
        self.settingsBtn.setMaximumSize(QtCore.QSize(130, 54))
        self.settingsBtn.setStyleSheet(_fromUtf8(""))
        self.settingsBtn.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/settingsOff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/settingsOn.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.settingsBtn.setIcon(icon1)
        self.settingsBtn.setIconSize(QtCore.QSize(135, 60))
        self.settingsBtn.setCheckable(True)
        self.settingsBtn.setChecked(True)
        self.settingsBtn.setFlat(True)
        self.settingsBtn.setObjectName(_fromUtf8("settingsBtn"))
        self.horizontalLayout_3.addWidget(self.settingsBtn)
        self.aboutBtn = QtGui.QPushButton(self.buttonBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutBtn.sizePolicy().hasHeightForWidth())
        self.aboutBtn.setSizePolicy(sizePolicy)
        self.aboutBtn.setMinimumSize(QtCore.QSize(0, 54))
        self.aboutBtn.setMaximumSize(QtCore.QSize(132, 54))
        self.aboutBtn.setStyleSheet(_fromUtf8(""))
        self.aboutBtn.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/aboutOff.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/aboutOn.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.aboutBtn.setIcon(icon2)
        self.aboutBtn.setIconSize(QtCore.QSize(135, 60))
        self.aboutBtn.setCheckable(True)
        self.aboutBtn.setFlat(True)
        self.aboutBtn.setObjectName(_fromUtf8("aboutBtn"))
        self.horizontalLayout_3.addWidget(self.aboutBtn)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.cmiSmallButton = QtGui.QPushButton(self.buttonBar)
        self.cmiSmallButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/cmi_small.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmiSmallButton.setIcon(icon3)
        self.cmiSmallButton.setIconSize(QtCore.QSize(69, 19))
        self.cmiSmallButton.setFlat(True)
        self.cmiSmallButton.setObjectName(_fromUtf8("cmiSmallButton"))
        self.horizontalLayout_3.addWidget(self.cmiSmallButton)
        self.verticalLayout.addWidget(self.buttonBar)
        self.stack = QtGui.QStackedWidget(self.centralwidget)
        self.stack.setFrameShape(QtGui.QFrame.NoFrame)
        self.stack.setFrameShadow(QtGui.QFrame.Raised)
        self.stack.setObjectName(_fromUtf8("stack"))
        self.settingsPage = QtGui.QWidget()
        self.settingsPage.setObjectName(_fromUtf8("settingsPage"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.settingsPage)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.settingsPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox.setMouseTracking(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setContentsMargins(25, 10, 0, 6)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(107, 0))
        self.label_4.setMaximumSize(QtCore.QSize(107, 16777215))
        self.label_4.setMouseTracking(True)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.sourceFileField = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceFileField.sizePolicy().hasHeightForWidth())
        self.sourceFileField.setSizePolicy(sizePolicy)
        self.sourceFileField.setMinimumSize(QtCore.QSize(485, 24))
        self.sourceFileField.setMaximumSize(QtCore.QSize(485, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sourceFileField.setFont(font)
        self.sourceFileField.setText(_fromUtf8(""))
        self.sourceFileField.setObjectName(_fromUtf8("sourceFileField"))
        self.horizontalLayout_5.addWidget(self.sourceFileField)
        self.sourceFileButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceFileButton.sizePolicy().hasHeightForWidth())
        self.sourceFileButton.setSizePolicy(sizePolicy)
        self.sourceFileButton.setMinimumSize(QtCore.QSize(29, 24))
        self.sourceFileButton.setMaximumSize(QtCore.QSize(25, 24))
        self.sourceFileButton.setMouseTracking(True)
        self.sourceFileButton.setFlat(False)
        self.sourceFileButton.setObjectName(_fromUtf8("sourceFileButton"))
        self.horizontalLayout_5.addWidget(self.sourceFileButton)
        spacerItem3 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(107, 0))
        self.label_10.setMaximumSize(QtCore.QSize(107, 16777215))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setMouseTracking(True)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_7.addWidget(self.label_10)
        self.objFileField = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.objFileField.sizePolicy().hasHeightForWidth())
        self.objFileField.setSizePolicy(sizePolicy)
        self.objFileField.setMinimumSize(QtCore.QSize(485, 24))
        self.objFileField.setMaximumSize(QtCore.QSize(485, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.objFileField.setFont(font)
        self.objFileField.setObjectName(_fromUtf8("objFileField"))
        self.horizontalLayout_7.addWidget(self.objFileField)
        self.objFileButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.objFileButton.sizePolicy().hasHeightForWidth())
        self.objFileButton.setSizePolicy(sizePolicy)
        self.objFileButton.setMinimumSize(QtCore.QSize(29, 24))
        self.objFileButton.setMaximumSize(QtCore.QSize(25, 24))
        self.objFileButton.setMouseTracking(True)
        self.objFileButton.setFlat(False)
        self.objFileButton.setObjectName(_fromUtf8("objFileButton"))
        self.horizontalLayout_7.addWidget(self.objFileButton)
        spacerItem4 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(107, 0))
        self.label_11.setMaximumSize(QtCore.QSize(107, 16777215))
        self.label_11.setMouseTracking(True)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_6.addWidget(self.label_11)
        self.outFileField = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outFileField.sizePolicy().hasHeightForWidth())
        self.outFileField.setSizePolicy(sizePolicy)
        self.outFileField.setMinimumSize(QtCore.QSize(485, 24))
        self.outFileField.setMaximumSize(QtCore.QSize(485, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.outFileField.setFont(font)
        self.outFileField.setText(_fromUtf8(""))
        self.outFileField.setObjectName(_fromUtf8("outFileField"))
        self.horizontalLayout_6.addWidget(self.outFileField)
        self.outFileButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outFileButton.sizePolicy().hasHeightForWidth())
        self.outFileButton.setSizePolicy(sizePolicy)
        self.outFileButton.setMinimumSize(QtCore.QSize(29, 24))
        self.outFileButton.setMaximumSize(QtCore.QSize(25, 24))
        self.outFileButton.setMouseTracking(True)
        self.outFileButton.setFlat(False)
        self.outFileButton.setObjectName(_fromUtf8("outFileButton"))
        self.horizontalLayout_6.addWidget(self.outFileButton)
        spacerItem5 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(40)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(107, 0))
        self.label_9.setMaximumSize(QtCore.QSize(107, 16777215))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_4.addWidget(self.label_9)
        self.radioFbx = QtGui.QRadioButton(self.groupBox)
        self.radioFbx.setChecked(True)
        self.radioFbx.setObjectName(_fromUtf8("radioFbx"))
        self.horizontalLayout_4.addWidget(self.radioFbx)
        self.radioAction = QtGui.QRadioButton(self.groupBox)
        self.radioAction.setObjectName(_fromUtf8("radioAction"))
        self.horizontalLayout_4.addWidget(self.radioAction)
        self.radioTerragen = QtGui.QRadioButton(self.groupBox)
        self.radioTerragen.setObjectName(_fromUtf8("radioTerragen"))
        self.horizontalLayout_4.addWidget(self.radioTerragen)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.subGroupBox = QtGui.QGroupBox(self.settingsPage)
        self.subGroupBox.setMaximumSize(QtCore.QSize(16777215, 116))
        self.subGroupBox.setTitle(_fromUtf8(""))
        self.subGroupBox.setObjectName(_fromUtf8("subGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.subGroupBox)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_4 = QtGui.QGroupBox(self.subGroupBox)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.widthField = QtGui.QLineEdit(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widthField.sizePolicy().hasHeightForWidth())
        self.widthField.setSizePolicy(sizePolicy)
        self.widthField.setMaximumSize(QtCore.QSize(50, 16777215))
        self.widthField.setObjectName(_fromUtf8("widthField"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.widthField)
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.heightField = QtGui.QLineEdit(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heightField.sizePolicy().hasHeightForWidth())
        self.heightField.setSizePolicy(sizePolicy)
        self.heightField.setMaximumSize(QtCore.QSize(50, 16777215))
        self.heightField.setObjectName(_fromUtf8("heightField"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.heightField)
        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.subGroupBox)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.hfaField = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hfaField.sizePolicy().hasHeightForWidth())
        self.hfaField.setSizePolicy(sizePolicy)
        self.hfaField.setMaximumSize(QtCore.QSize(60, 1600))
        self.hfaField.setObjectName(_fromUtf8("hfaField"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.hfaField)
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.vfaField = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vfaField.sizePolicy().hasHeightForWidth())
        self.vfaField.setSizePolicy(sizePolicy)
        self.vfaField.setMaximumSize(QtCore.QSize(60, 16777215))
        self.vfaField.setObjectName(_fromUtf8("vfaField"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.vfaField)
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.subGroupBox)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_5)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.fpsField = QtGui.QLineEdit(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fpsField.sizePolicy().hasHeightForWidth())
        self.fpsField.setSizePolicy(sizePolicy)
        self.fpsField.setMaximumSize(QtCore.QSize(45, 16777215))
        self.fpsField.setAlignment(QtCore.Qt.AlignCenter)
        self.fpsField.setObjectName(_fromUtf8("fpsField"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.fpsField)
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.scaleField = QtGui.QLineEdit(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleField.sizePolicy().hasHeightForWidth())
        self.scaleField.setSizePolicy(sizePolicy)
        self.scaleField.setMaximumSize(QtCore.QSize(45, 16777215))
        self.scaleField.setAlignment(QtCore.Qt.AlignCenter)
        self.scaleField.setObjectName(_fromUtf8("scaleField"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.scaleField)
        self.gridLayout.addWidget(self.groupBox_5, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.subGroupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.infoLine = QtGui.QLabel(self.settingsPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoLine.sizePolicy().hasHeightForWidth())
        self.infoLine.setSizePolicy(sizePolicy)
        self.infoLine.setMinimumSize(QtCore.QSize(0, 50))
        self.infoLine.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setPointSize(11)
        self.infoLine.setFont(font)
        self.infoLine.setText(_fromUtf8(""))
        self.infoLine.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.infoLine.setWordWrap(True)
        self.infoLine.setObjectName(_fromUtf8("infoLine"))
        self.horizontalLayout.addWidget(self.infoLine)
        self.convertButton = QtGui.QPushButton(self.settingsPage)
        self.convertButton.setMinimumSize(QtCore.QSize(64, 30))
        self.convertButton.setObjectName(_fromUtf8("convertButton"))
        self.horizontalLayout.addWidget(self.convertButton)
        self.quitButton = QtGui.QPushButton(self.settingsPage)
        self.quitButton.setMinimumSize(QtCore.QSize(64, 30))
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.horizontalLayout.addWidget(self.quitButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.stack.addWidget(self.settingsPage)
        self.aboutPage = QtGui.QWidget()
        self.aboutPage.setObjectName(_fromUtf8("aboutPage"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.aboutPage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 12, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.cmiLogoButton = QtGui.QPushButton(self.aboutPage)
        self.cmiLogoButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/cmi_logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmiLogoButton.setIcon(icon4)
        self.cmiLogoButton.setIconSize(QtCore.QSize(180, 105))
        self.cmiLogoButton.setFlat(True)
        self.cmiLogoButton.setObjectName(_fromUtf8("cmiLogoButton"))
        self.horizontalLayout_2.addWidget(self.cmiLogoButton)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_6 = QtGui.QLabel(self.aboutPage)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.stack.addWidget(self.aboutPage)
        self.chatPage = QtGui.QWidget()
        self.chatPage.setObjectName(_fromUtf8("chatPage"))
        self.gridLayout_2 = QtGui.QGridLayout(self.chatPage)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.stack.addWidget(self.chatPage)
        self.verticalLayout.addWidget(self.stack)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "AtomSplitter", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsPage.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-color: rgb(55, 55, 55);", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Camera .chan:", None, QtGui.QApplication.UnicodeUTF8))
        self.sourceFileButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Point Cloud .obj:", None, QtGui.QApplication.UnicodeUTF8))
        self.objFileField.setText(QtGui.QApplication.translate("MainWindow", "[Optional]", None, QtGui.QApplication.UnicodeUTF8))
        self.objFileButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Out file:", None, QtGui.QApplication.UnicodeUTF8))
        self.outFileButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Out Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioFbx.setText(QtGui.QApplication.translate("MainWindow", "FBX", None, QtGui.QApplication.UnicodeUTF8))
        self.radioAction.setText(QtGui.QApplication.translate("MainWindow", ".action (Flame)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioTerragen.setText(QtGui.QApplication.translate("MainWindow", "Terragen", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.widthField.setText(QtGui.QApplication.translate("MainWindow", "2048", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Height:", None, QtGui.QApplication.UnicodeUTF8))
        self.heightField.setText(QtGui.QApplication.translate("MainWindow", "1556", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Film Aperature (mm)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Horizontal:", None, QtGui.QApplication.UnicodeUTF8))
        self.hfaField.setText(QtGui.QApplication.translate("MainWindow", "24.576", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Vertical:", None, QtGui.QApplication.UnicodeUTF8))
        self.vfaField.setText(QtGui.QApplication.translate("MainWindow", "18.672", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Misc", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "FPS:", None, QtGui.QApplication.UnicodeUTF8))
        self.fpsField.setText(QtGui.QApplication.translate("MainWindow", "24", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Scene Scale:", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleField.setText(QtGui.QApplication.translate("MainWindow", "1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.convertButton.setText(QtGui.QApplication.translate("MainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutPage.setStyleSheet(QtGui.QApplication.translate("MainWindow", "    background-color: rgb(120, 120, 120);\n"
"    color: rgb(255, 255, 255);", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" align=\"center\" cellspacing=\"8\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Project based on the beta testing between <br />The Foundry\'s NUKE Tracker and Flame Action by Chris Maynard.</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Project Tracking: <a href=\"http://redmine.justinfx.com/projects/atomsplitter\"><span style=\" text-decoration: underline; color:#ffa500;\">http://redmine.justinfx.com/projects/atomsplitter</span></a></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">GUI Design / .chan parsing / FBX, TGD conversion:</span><br />Justin Israel <a href=\"mailto:justinisrael@gmail.com\"><span style=\" text-decoration: underline; color:#ffa500;\">(justinisrael@gmail.com)</span></a><br /><a href=\"http://www.justinfx.com\"><span style=\" text-decoration: underline; color:#ffa500;\">www.justinfx.com</span></a></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">.action conversion code provided by: </span><br />Georges Nakhle <a href=\"mailto:nakhle_georges@hotmail.com\"><span style=\" text-decoration: underline; color:#ffa500;\">(nakhle_georges@hotmail.com)</span></a><br /><a href=\"http://www.geonak.com/\"><span style=\" text-decoration: underline; color:#ffa500;\">www.geonak.com</span></a></p></td></tr></table></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
