# -*- coding: utf-8 -*-

################################################################################
## Dialog generated from reading UI file 'st.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
# 权重调整子界面

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class SubWindow2(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(827, 761)
        self.label_Permeability = QLabel(Dialog)
        self.label_Permeability.setObjectName(u"label_Permeability")
        self.label_Permeability.setGeometry(QRect(140, 140, 54, 21))
        self.label_Stable = QLabel(Dialog)
        self.label_Stable.setObjectName(u"label_Stable")
        self.label_Stable.setGeometry(QRect(140, 90, 54, 21))
        self.label_Structure = QLabel(Dialog)
        self.label_Structure.setObjectName(u"label_Structure")
        self.label_Structure.setGeometry(QRect(130, 190, 81, 21))
        self.label_Electric = QLabel(Dialog)
        self.label_Electric.setObjectName(u"label_Electric")
        self.label_Electric.setGeometry(QRect(140, 40, 54, 21))
        self.doubleSpinBox_electric = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_electric.setObjectName(u"doubleSpinBox_electric")
        self.doubleSpinBox_electric.setGeometry(QRect(230, 40, 62, 22))
        self.doubleSpinBox_Stable = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_Stable.setObjectName(u"doubleSpinBox_Stable")
        self.doubleSpinBox_Stable.setGeometry(QRect(230, 90, 62, 22))
        self.doubleSpinBox_permeability = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_permeability.setObjectName(u"doubleSpinBox_permeability")
        self.doubleSpinBox_permeability.setGeometry(QRect(230, 140, 62, 22))
        self.doubleSpinBox_structure = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_structure.setObjectName(u"doubleSpinBox_permeability")
        self.doubleSpinBox_structure.setGeometry(QRect(300, 190, 62, 22))
        self.comboBox_structure = QComboBox(Dialog)
        self.comboBox_structure.addItem("")
        self.comboBox_structure.addItem("")
        self.comboBox_structure.setObjectName(u"comboBox_structure")
        self.comboBox_structure.setGeometry(QRect(225, 190, 69, 22))

        # self.label_Electric.raise_()
        # self.label_Permeability.raise_()
        # self.label_Stable.raise_()
        # self.label_Structure.raise_()
        # self.doubleSpinBox_permeability.raise_()
        # self.doubleSpinBox_electric.raise_()
        # self.doubleSpinBox_Stable.raise_()
        # self.doubleSpinBox_Stable.raise_()
        # self.comboBox_structure.raise_()
    

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"st", None))

        self.label_Permeability.setText(QCoreApplication.translate("Dialog", u"\u6e17\u900f\u6027", None))
        self.label_Stable.setText(QCoreApplication.translate("Dialog", u"\u7a33\u5b9a\u6027", None))
        self.label_Structure.setText(QCoreApplication.translate("Dialog", u"\u65ad\u5c42\u6784\u9020\u7ed3\u6784", None))
        self.label_Electric.setText(QCoreApplication.translate("Dialog", u"\u7535\u6cd5\u6743\u91cd", None))
        self.comboBox_structure.setItemText(0, QCoreApplication.translate("Dialog", u"0", None))
        self.comboBox_structure.setItemText(1, QCoreApplication.translate("Dialog", u"1", None))
    # retranslateUi

