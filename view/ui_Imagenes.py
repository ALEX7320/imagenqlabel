# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ImagenesOLpsng.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Imagenes(object):
    def setupUi(self, Imagenes):
        if not Imagenes.objectName():
            Imagenes.setObjectName(u"Imagenes")
        Imagenes.resize(595, 458)
        Imagenes.setStyleSheet(u"")
        self.centralwidget = QWidget(Imagenes)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(15)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(20, 20, 20, 20)
        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setSpacing(9)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btncar1 = QPushButton(self.groupBox_2)
        self.btncar1.setObjectName(u"btncar1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btncar1.sizePolicy().hasHeightForWidth())
        self.btncar1.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.btncar1, 1, 0, 1, 1)

        self.btndel1 = QPushButton(self.groupBox_2)
        self.btndel1.setObjectName(u"btndel1")
        sizePolicy.setHeightForWidth(self.btndel1.sizePolicy().hasHeightForWidth())
        self.btndel1.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.btndel1, 2, 0, 1, 1)

        self.lblcover1 = QLabel(self.groupBox_2)
        self.lblcover1.setObjectName(u"lblcover1")
        self.lblcover1.setMinimumSize(QSize(250, 250))
        self.lblcover1.setMaximumSize(QSize(250, 250))
        self.lblcover1.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px solid gray;\n"
"}")
        self.lblcover1.setFrameShadow(QFrame.Plain)
        self.lblcover1.setScaledContents(True)

        self.gridLayout_4.addWidget(self.lblcover1, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 2)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setSpacing(9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.btncar2 = QPushButton(self.groupBox)
        self.btncar2.setObjectName(u"btncar2")
        sizePolicy.setHeightForWidth(self.btncar2.sizePolicy().hasHeightForWidth())
        self.btncar2.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.btncar2, 1, 0, 1, 1)

        self.lblcover2 = QLabel(self.groupBox)
        self.lblcover2.setObjectName(u"lblcover2")
        self.lblcover2.setMinimumSize(QSize(250, 250))
        self.lblcover2.setMaximumSize(QSize(250, 250))
        self.lblcover2.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px solid gray;\n"
"}")
        self.lblcover2.setFrameShape(QFrame.NoFrame)
        self.lblcover2.setFrameShadow(QFrame.Plain)
        self.lblcover2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lblcover2, 0, 0, 1, 1)

        self.btndel2 = QPushButton(self.groupBox)
        self.btndel2.setObjectName(u"btndel2")
        sizePolicy.setHeightForWidth(self.btndel2.sizePolicy().hasHeightForWidth())
        self.btndel2.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.btndel2, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        Imagenes.setCentralWidget(self.centralwidget)

        self.retranslateUi(Imagenes)

        QMetaObject.connectSlotsByName(Imagenes)
    # setupUi

    def retranslateUi(self, Imagenes):
        Imagenes.setWindowTitle(QCoreApplication.translate("Imagenes", u"Cargar imagen - ALEX7320", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Imagenes", u"Ignore", None))
        self.btncar1.setText(QCoreApplication.translate("Imagenes", u"Cargar", None))
        self.btndel1.setText(QCoreApplication.translate("Imagenes", u"Eliminar", None))
        self.lblcover1.setText("")
        self.label.setText(QCoreApplication.translate("Imagenes", u"Agregar imagen en QLabel", None))
        self.groupBox.setTitle(QCoreApplication.translate("Imagenes", u"Keep", None))
        self.btncar2.setText(QCoreApplication.translate("Imagenes", u"Cargar", None))
        self.lblcover2.setText("")
        self.btndel2.setText(QCoreApplication.translate("Imagenes", u"Eliminar", None))
    # retranslateUi

