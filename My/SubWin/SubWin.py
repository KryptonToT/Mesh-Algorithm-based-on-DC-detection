# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SubWin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from pyqtgraph import PlotWidget
# 备用子界面

class Sub_Window(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(819, 572)
        self.lxcs = QLabel(Dialog)
        self.lxcs.setObjectName(u"lxcs")
        self.lxcs.setGeometry(QRect(90, 150, 91, 41))
        self.lxcs.setAlignment(Qt.AlignCenter)
        self.st = QLabel(Dialog)
        self.st.setObjectName(u"st")
        self.st.setGeometry(QRect(90, 110, 91, 41))
        self.st.setAlignment(Qt.AlignCenter)
        self.wdx = QLabel(Dialog)
        self.wdx.setObjectName(u"wdx")
        self.wdx.setGeometry(QRect(90, 190, 91, 41))
        self.wdx.setAlignment(Qt.AlignCenter)
        self.jg = QLabel(Dialog)
        self.jg.setObjectName(u"jg")
        self.jg.setGeometry(QRect(90, 230, 91, 41))
        self.jg.setAlignment(Qt.AlignCenter)


        self.doubleSpinBox_st = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_st.setObjectName(u"doubleSpinBox_st")
        self.doubleSpinBox_st.setGeometry(QRect(220, 120, 62, 22))
        #self.doubleSpinBox_st.setEnabled(False)
        self.doubleSpinBox_st.setValue(0.5)
        self.doubleSpinBox_st.setSingleStep(0.1)
        self.doubleSpinBox_st.setRange(0, 1)

        self.doubleSpinBox_lxcs = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_lxcs.setObjectName(u"doubleSpinBox_lxcs")
        self.doubleSpinBox_lxcs.setGeometry(QRect(220, 160, 62, 22))
        #self.doubleSpinBox_lxcs.setEnabled(False)
        self.doubleSpinBox_lxcs.setValue(0.25)
        self.doubleSpinBox_lxcs.setSingleStep(0.1)
        self.doubleSpinBox_lxcs.setRange(0, 1)

        self.doubleSpinBox_wdx = QDoubleSpinBox(Dialog)
        self.doubleSpinBox_wdx.setObjectName(u"doubleSpinBox_wdx")
        self.doubleSpinBox_wdx.setGeometry(QRect(220, 200, 62, 22))
        #self.doubleSpinBox_wdx.setEnabled(False)
        self.doubleSpinBox_wdx.setValue(0.25)
        self.doubleSpinBox_wdx.setSingleStep(0.1)
        self.doubleSpinBox_wdx.setRange(0.0, 1.0)

        self.combobox_jg = QComboBox(Dialog)
        self.combobox_jg.setObjectName(u"doubleSpinBox_jg")
        self.combobox_jg.setGeometry(QRect(220, 240, 62, 22))
        self.combobox_jg.addItems(['0', '1'])
        #self.doubleSpinBox_jg.setEnabled(False)


        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(60, 50, 681, 261))
        self.Label = QLabel(Dialog)
        self.Label.setObjectName(u"\u53c2\u6570\u6743\u91cd\u8bbe\u7f6e")
        self.Label.setGeometry(QRect(500, 100, 230, 50))

        self.pushButton_cal = QPushButton(Dialog)
        self.pushButton_cal.setObjectName(u"pushButton_cal")
        self.pushButton_cal.setGeometry(QRect(500, 160, 80, 40))

        # self.pushButton_st = QPushButton(Dialog)
        # self.pushButton_st.setObjectName(u"pushButton_st")
        # self.pushButton_st.setGeometry(QRect(320, 120, 100, 22))
        # self.pushButton_st.clicked.connect(self.enable_st)

        # self.pushButton_lxcs = QPushButton(Dialog)
        # self.pushButton_lxcs.setObjectName(u"pushButton_lxcs")
        # self.pushButton_lxcs.setGeometry(QRect(320, 160, 100, 22))
        # self.pushButton_lxcs.clicked.connect(self.enable_lxcs)

        # self.pushButton_wdx = QPushButton(Dialog)
        # self.pushButton_wdx.setObjectName(u"pushButton_wdx")
        # self.pushButton_wdx.setGeometry(QRect(320, 200, 100, 22))
        # self.pushButton_wdx.clicked.connect(self.enable_wdx)
        
        # self.pushButton_jg = QPushButton(Dialog)
        # self.pushButton_jg.setObjectName(u"pushButton_jg")
        # self.pushButton_jg.setGeometry(QRect(320, 240, 100, 22))
        # self.pushButton_jg.clicked.connect(self.enable_jg) 

        self.curve = PlotWidget(Dialog)
        self.curve.setObjectName(u"curve")
        self.curve.setGeometry(QRect(60, 320, 681, 241))
        self.groupBox.raise_()
        self.lxcs.raise_()
        self.st.raise_()
        self.wdx.raise_()
        self.jg.raise_()

        self.doubleSpinBox_st.raise_()
        self.doubleSpinBox_lxcs.raise_()
        self.doubleSpinBox_wdx.raise_()
        self.combobox_jg.raise_()
        self.Label.raise_()
        self.pushButton_cal.raise_()
        # self.pushButton_st.raise_()
        # self.pushButton_lxcs.raise_()
        # self.pushButton_wdx.raise_()
        # self.pushButton_jg.raise_()
        self.curve.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    # def enable_st(self):      # 启用按钮槽函数(Abandoned)
    #     if self.pushButton_st.text() == u'\u542f\u7528':
    #         benable = True
    #         command = u'\u5173\u95ed'
    #     else:
    #         benable = False
    #         command = u'\u542f\u7528'
    #     self.doubleSpinBox_st.setEnabled(benable)
    #     self.pushButton_st.setText(command)

    # def enable_lxcs(self):
    #     if self.pushButton_lxcs.text() == u'\u542f\u7528':
    #         benable = True
    #         command = u'\u5173\u95ed'
    #     else:
    #         benable = False
    #         command = u'\u542f\u7528'
    #     self.doubleSpinBox_lxcs.setEnabled(benable)
    #     self.pushButton_lxcs.setText(command)

    # def enable_wdx(self):
    #     if self.pushButton_wdx.text() == u'\u542f\u7528':
    #         benable = True
    #         command = u'\u5173\u95ed'
    #     else:
    #         benable = False
    #         command = u'\u542f\u7528'
    #     self.doubleSpinBox_wdx.setEnabled(benable)
    #     self.pushButton_wdx.setText(command)

    # def enable_jg(self):
    #     if self.pushButton_jg.text() == u'\u542f\u7528':
    #         benable = True
    #         command = u'\u5173\u95ed'
    #     else:
    #         benable = False
    #         command = u'\u542f\u7528'
    #     self.doubleSpinBox_jg.setEnabled(benable)
    #     self.pushButton_jg.setText(command)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lxcs.setText(QCoreApplication.translate("Dialog", u"\u529b\u5b66\u53c2\u6570", None))
        self.st.setText(QCoreApplication.translate("Dialog", u"\u6e17\u900f\u6027", None))
        self.wdx.setText(QCoreApplication.translate("Dialog", u"\u7a33\u5b9a\u6027", None))
        self.jg.setText(QCoreApplication.translate("Dialog", u"\u65ad\u5c42\u6784\u9020\u7ed3\u6784", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u53c2\u6570\u6743\u91cd\u8bbe\u7f6e", None))
        self.pushButton_cal.setText(QCoreApplication.translate("Dialog", u"\u66f2\u7ebf\u7ed8\u5236", None))
        # self.pushButton_st.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None))
        # self.pushButton_lxcs.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None))
        # self.pushButton_wdx.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None))
        # self.pushButton_jg.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None))
    # retranslateUi

