# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDoubleSpinBox, QFrame, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1013, 746)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setStyleSheet(u"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"#BackGround {	\n"
"	background-color: rgb(255, 255, 250);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-radius:10px;\n"
"}\n"
"QWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	font: 14pt ;\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QSpinBox{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 250, 255);\n"
"	border-radius:5px;\n"
"	border: 2px solid rgb(245, 245, 250);\n"
"	padding-left:20px;\n"
"}\n"
"QSpinBox::up-button{\n"
"	image: url(:/icons/images/icons/arrow_up.png);\n"
"	border-radius:3px;\n"
"	width:40px\n"
"}\n"
"QSpinBox::up-button:hover{\n"
""
                        "	background-color: #dfc9ff;\n"
"}\n"
"QSpinBox::up-button:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QSpinBox::down-button{\n"
"	image: url(:/icons/images/icons/arrow_down.png);\n"
"	border-radius:3px;\n"
"	width:40px\n"
"}\n"
"QSpinBox::down-button:hover{\n"
"	background-color: #dfc9ff;\n"
"}\n"
"QSpinBox::down-button:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #a2bded;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::handle:horizontal:hover{\n"
"	background-color: rgb(195, 155, 255);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"	background-color: rgb(223, 200, 255);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"	background-color: rgb(255, 250, 250);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-"
                        "radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"	background-color: rgb(255, 250, 250);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:#a2bded ;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(195, 155, 255);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: "
                        "rgb(223, 200, 255);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"	background-color: rgb(255, 250, 250);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(255, 250, 250);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////// \n"
"extraLeftBox*/\n"
"\n"
"/*elc*/\n"
"#extraLeftBox_elc{\n"
"	background-color: rgb(245, 245, 255);\n"
"}\n"
"#extraLeftBox_elc"
                        " QScrollBar:vertical {\n"
"	border: none;\n"
"	background: rgb(234, 234, 239);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"#extraLeftBox_elc QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 5px\n"
" }\n"
" #extraLeftBox_elc QScrollBar::handle:vertical:pressed{\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"#extraLeftBox_elc QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(195, 155, 255);\n"
"}\n"
"#extraLeftBox_elc QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(245, 245, 255);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"#extraLeftBox_elc QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(245, 245, 255);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radi"
                        "us: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"#extraLeftBox_elc QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"#extraLeftBox_elc QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"#extraTop{\n"
"	background-color: rgb(255, 252, 245);\n"
"}\n"
"#extraTopLabel{\n"
"	color: rgb(104, 152, 236);\n"
"	font: 20pt \"\u9ed1\u4f53\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(162, 189, 237);\n"
"	background-color: rgb(255, 250, 255);\n"
"	border-radius:5px;\n"
"	border:2px solid rgb(255, 250, 255);\n"
"	padding-left:30px;\n"
"	selection-color: rgb(180, 208, 255);\n"
"	selection-background-color: rgb(160, 195, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(180, 208, 255);\n"
"}\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(160, 195, 255);\n"
"}\n"
"#file_open{\n"
"	background-color: rgb(255, 252, 245);\n"
"	border-radius:5px;\n"
"	border: 2px sollid  "
                        "rgb(255, 252, 245);\n"
"}\n"
"#file_open:hover{\n"
"	border:2px solid rgb(160, 195, 255);\n"
"}\n"
"#file_open:pressed{\n"
"	background-color: rgb(217, 224, 255);\n"
"}\n"
"#extraCloseBtn{background-color: rgb(255, 255, 250);border:none;border-radius:5px;}\n"
"#extraCloseBtn:hover {background-color: rgb(255, 252, 245);border-style:solid;border-radius:4px;	border:2px solid rgb(160, 195, 255);}\n"
"#extraCloseBtn:pressed{background-color:rgb(245, 245, 255);border-style:solid;border-radius:4px;}\n"
"#extraCloseBtn2{background-color: rgb(255, 255, 250);border:none;border-radius:5px;}\n"
"#extraCloseBtn2:hover {background-color: rgb(255, 252, 245);border-style:solid;border-radius:4px;	border:2px solid rgb(160, 195, 255);}\n"
"#extraCloseBtn2:pressed{background-color:rgb(245, 245, 255);border-style:solid;border-radius:4px;}\n"
"#extraCloseBtn3{background-color: rgb(255, 255, 250);border:none;border-radius:5px;}\n"
"#extraCloseBtn3:hover {background-color: rgb(255, 252, 245);border-style:solid;border-radius:4px;	bord"
                        "er:2px solid rgb(160, 195, 255);}\n"
"#extraCloseBtn3:pressed{background-color:rgb(245, 245, 255);border-style:solid;border-radius:4px;}\n"
"\n"
"QDoubleSpinBox{\n"
"	color: rgb(100, 157, 255);\n"
"	background-color: rgb(255, 250, 255);\n"
"	border-radius:5px;\n"
"	border: 2px solid rgb(245, 245, 250);\n"
"	padding-left:20px;\n"
"}\n"
"QDoubleSpinBox::up-button{\n"
"	image: url(:/icons/images/icons/arrow_up.png);\n"
"	border-radius:3px;\n"
"	width:40px\n"
"}\n"
"QDoubleSpinBox::up-button:hover{\n"
"	background-color: #dfc9ff;\n"
"}\n"
"QDoubleSpinBox::up-button:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QDoubleSpinBox::down-button{\n"
"	image: url(:/icons/images/icons/arrow_down.png);\n"
"	border-radius:3px;\n"
"	width:40px\n"
"}\n"
"QDoubleSpinBox::down-button:hover{\n"
"	background-color: #dfc9ff;\n"
"}\n"
"QDoubleSpinBox::down-button:pressed{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 10px;\n"
"    height: 20px;\n"
"	margin: 0px;"
                        "\n"
" 	background-color:rgb(234, 234, 239);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(217, 224, 255);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 20px;\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"	border-radius: 10px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"\n"
"#pipText{\n"
"	border-radius:5px;\n"
"	selection-color:rgb(255,255,255);\n"
"	selection-background-color:rgb(255,121,198);\n"
"}\n"
"\n"
"#pipText QScrollBar:vertical{\n"
"	width:10px;\n"
"}\n"
"/*cal*/\n"
"#extraTopMenu2 QPushButton{\n"
"	color: rgb(85, 85, 127);\n"
"	background-color: rgb(225, 225, 255);\n"
"	border-radius:10px;\n"
"}\n"
"#extraTopMenu2 QPushButton:hover{\n"
"	border: 2px solid rgb(100, 149, 237);\n"
"}\n"
"#extraTopMenu2 QPushButton:pressed{\n"
"	background-color: rgb"
                        "(255, 252, 245);\n"
"}\n"
"#extraLeftBox_cal{\n"
"	background-color: rgb(245, 245, 255);\n"
"}\n"
"#extraTop2{\n"
"	background-color: rgb(255, 252, 245);\n"
"}\n"
"#extraTopLabel2{\n"
"	color: rgb(104, 152, 236);\n"
"	font: 20pt \"\u9ed1\u4f53\";\n"
"}\n"
"\n"
"\n"
"/*file*/\n"
"#extraTopMenu3 QPushButton{\n"
"	color: rgb(85, 85, 127);\n"
"	background-color: rgb(225, 225, 255);\n"
"	border-radius:10px;\n"
"}\n"
"#extraTopMenu3 QPushButton:hover{\n"
"	border: 2px solid rgb(100, 149, 237);\n"
"}\n"
"#extraTopMenu3 QPushButton:pressed{\n"
"	background-color: rgb(255, 252, 245);\n"
"}\n"
"#extraLeftBox_file{\n"
"	background-color: rgb(245, 245, 255);\n"
"}\n"
"#extraTop3{\n"
"	background-color: rgb(255, 252, 245);\n"
"}\n"
"#extraToplogo3{\n"
"	background-repeat:no-repeat;\n"
"	background-position:right center;\n"
"}\n"
"#extraTopLabel3{\n"
"	color: rgb(104, 152, 236);\n"
"	font: 20pt \"\u9ed1\u4f53\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////// \n"
"Conten"
                        "tBox*/\n"
"contentBox{\n"
"	border-top-right:10px;\n"
"	border-bottom-right:10px;\n"
"}\n"
"/*TopContent*/\n"
"#TopContent QPushButton{background-color: rgb(255, 255, 250);border:none;border-radius:5px;}\n"
"#TopContent QPushButton:hover {background-color: rgb(255, 252, 245);border-style:solid;border-radius:4px;	border:2px solid rgb(160, 195, 255);}\n"
"#TopContent QPushButton:pressed{background-color:rgb(245, 245, 255);border-style:solid;border-radius:4px;}\n"
"/*Content*/\n"
"\n"
"#page_container{\n"
"	background-color:transparent;\n"
"}\n"
"#home{\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"}\n"
"\n"
"#page_container QMenu{\n"
"	background-color:rgb(245, 245, 255);\n"
"    font:12pt'\u5b8b\u4f53';\n"
"    color:rgb(72,61, 139);\n"
"}\n"
"#page_container QPushButton{\n"
"    color: rgb(85, 85, 127);\n"
"	background-color:rgb(245, 245, 255);\n"
"    font:18pt'\u5b8b\u4f53';\n"
"    border-style: flat;\n"
"}\n"
"#page_container QPushButton:hover{\n"
"	background-color: rgb(223, 220, "
                        "255);\n"
"}\n"
"#page_container QPushButton:pressed{\n"
"	background-color: rgb(255, 252, 245);\n"
"}\n"
"/*stackedWidget*/\n"
"\n"
"/*destroy_depth*/\n"
"#destroy_depth QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"#destroy_depth QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"#destroy_depth QTableWidget::item:selected{\n"
"	background-color: rgb(223, 200, 255);\n"
"}\n"
"\n"
"#destroy_depth QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(162, 189, 237);\n"
"}\n"
"#destroy_depth QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color:#CEDFEF;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"#destroy_depth QHeaderView::section:vertical{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color:r"
                        "gb(255, 223, 112);\n"
"}\n"
"\n"
"/*AHP*/\n"
"#AHP QPlainTextEdit {\n"
"	background-color: rgb(255,255,255);\n"
"   font:12pt'\u5b8b\u4f53';\n"
"}\n"
"\n"
"#frame_layer1 QTableWidget {	\n"
"	padding: 5px;\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"#frame_layer1 QTableWidget::item{\n"
"	border-color: #EE4431;\n"
"	gridline-color: #EE4431;\n"
"}\n"
"#frame_layer1 QTableWidget::item:selected{\n"
"	background-color: #EE4431;\n"
"}\n"
"\n"
"#frame_layer1 QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: #B9DBAB;\n"
"	padding: 3px;\n"
"}\n"
"#frame_layer1 QHeaderView::section:vertical{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color:#B9DBAB;\n"
"	padding: 10px\n"
"}\n"
"\n"
"/*level2*/\n"
"#level2 QTableWidget {	\n"
"	padding: 5px;\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"#level2 QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"#level2 QTableWidget::item:selected{\n"
"	background-color: #B9DBAB"
                        ";\n"
"}\n"
"\n"
"#level2 QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: #CFE7EB;\n"
"}\n"
"#level2 QHeaderView::section:vertical{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color:#CFE7EB;\n"
"	padding: 10px\n"
"}\n"
"\n"
"/*risk*/\n"
"#Final QPushButton{\n"
"	background-color:rgb(255, 226, 123);\n"
"	border-radius:10px;\n"
"}\n"
"#Fianl QPushButton:hover{\n"
"	background-color: rgb(255, 229, 35);\n"
"}\n"
"#Final QPushButton:pressed{\n"
"	background-color: rgb(247, 99, 12);\n"
"}\n"
"#Single QPushButton{\n"
"	border-radius:10px;\n"
"}\n"
"#risk QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"#risk QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"#risk QTableWidget::item:selected{\n"
"	background-color: rgb(223, 200, 255);\n"
"}\n"
"\n"
"#risk "
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(162, 189, 237);\n"
"}\n"
"#risk QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(162, 189, 237);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"#risk QHeaderView::section:vertical{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color:rgb(255, 223, 112);\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"\n"
"#textBrowser {\n"
"	background-color:rgb(255, 250, 250);\n"
"   font:18pt'\u5b8b\u4f53';\n"
"}\n"
"#bottom_bar QLabel { font-size: 11px; color: rgb(113, 126, 149); background-color:rgb(255,255,250);padding-left: 5px; padding-right: 10px; padding-bottom: 2px; }\n"
"/*Geo*/\n"
"QSpinBox{\n"
"	background-color:transparent;\n"
"}\n"
"QComboBox {\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    background: transparent; \n"
"    border: 1px solid gray; \n"
"	color: #333333;\n"
"	border-color: rgb(149, "
                        "188, 255);\n"
"	background-color: #FFFFFF;\n"
"}\n"
"QComboBox:on {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(245,245,255);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    outline: 1px solid #000000;\n"
"    border: 1px solid rgb(149, 188, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: #FFFFFF; \n"
"    selection-color: rgb(245, 245, 255);\n"
"    selection-background-color:#FFFFFF;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; \n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px; \n"
"    background: rgb(236, 236, 236);\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"    background: #dfc9ff;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 15px;\n"
"    background: transparent;\n"
"    padding: 0px 0px 0px 0px;\n"
"    image: url(:/icons/images/icons/arrow_down.png);\n"
""
                        "}\n"
"\n"
"\n"
"QComboBox::down-arrow:on {\n"
"	image: url(:/icons/images/icons/arrow_up.png);\n"
"}\n"
"#list_frame QComboBox:on {\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(223, 200, 255);\n"
"}\n"
"\n"
"#geoFuncMenu QPushButton{\n"
"	background-color:transparent;\n"
"	border-radius:5px;\n"
"}\n"
"#geoFuncMenu QPushButton:hover{\n"
"	background-color: rgb(236, 236, 236);\n"
"	border:2px solid rgb(160, 195, 255);\n"
"}\n"
"#geoFuncMenu QPushButton:pressed{\n"
"	background-color: rgb(230, 230, 250);\n"
"    border: 2px sollid  rgb(255, 252, 245);\n"
"}\n"
"#geo QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"#geo QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"#geo QTableWidget::item:selected{\n"
"	background-color: rgb(223, 200, 255);\n"
"}\n"
"\n"
"#geo QTableWidget::horizontalHeader {	\n"
"	b"
                        "ackground-color: rgb(162, 189, 237);\n"
"}\n"
"#geo QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(162, 189, 237);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"#geo QHeaderView::section:vertical{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color:rgb(255, 223, 112);\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////\n"
"leftMenu */\n"
"\n"
"#Logo {\n"
"	background-position: centered;\n"
"	background-repeat:no-repeat;\n"
"}\n"
"\n"
"#titleDescription{font:14pt\"\u534e\u6587\u6977\u4f53\";color:rgb(72,61, 139);}\n"
"\n"
"#leftMenu {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"

"/* toggleButton*/\n"
"#toggleButton {\n"
"	background-position: left cen"
                        "ter;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 16px solid transparent;\n"
"	background-color: rgb(255, 255, 255);\n"
"	text-align: left;\n"
"	padding-left: 60px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"/*bottom Button*/\n"
"#bottomButton{\n"
"	background-color: rgb(248, 248, 255);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 16px solid transparent;\n"
"	background-color: rgb(255, 255, 255);\n"
"	text-align: left;\n"
"	padding-left: 60px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"\n"
"/*Buttons*/\n"
"#topMenu QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 12px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 84px;\n"
"}\n"
"#topMenu QPushButton:hover{\n"
"	background-color: rgb(236, 236, 236);\n"
"}\n"
"#topMenu QPushButton:pressed{\n"
"	background-color: rgb(230, 230, 250);\n"
"	co"
                        "lor: rgb(74,74, 255);\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.BackGround = QFrame(self.styleSheet)
        self.BackGround.setObjectName(u"BackGround")
        self.BackGround.setFrameShape(QFrame.StyledPanel)
        self.BackGround.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.BackGround)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.BackGround)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(75, 0))
        self.leftMenu.setMaximumSize(QSize(75, 16777215))
        self.leftMenu.setFrameShape(QFrame.NoFrame)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TopLogo = QFrame(self.leftMenu)
        self.TopLogo.setObjectName(u"TopLogo")
        self.TopLogo.setMinimumSize(QSize(0, 65))
        self.TopLogo.setMaximumSize(QSize(16777215, 65))
        self.TopLogo.setFrameShape(QFrame.NoFrame)
        self.TopLogo.setFrameShadow(QFrame.Raised)
        self.Logo = QFrame(self.TopLogo)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(7, 5, 61, 60))
        self.Logo.setStyleSheet(u"border-image: url(:/images/images/images/logo.png);")
        self.Logo.setFrameShape(QFrame.NoFrame)
        self.Logo.setFrameShadow(QFrame.Raised)
        self.titleDescription = QLabel(self.TopLogo)
        self.titleDescription.setObjectName(u"titleDescription")
        self.titleDescription.setGeometry(QRect(80, 10, 161, 51))

        self.verticalLayout_2.addWidget(self.TopLogo)

        self.funcMenu = QFrame(self.leftMenu)
        self.funcMenu.setObjectName(u"funcMenu")
        self.funcMenu.setFrameShape(QFrame.NoFrame)
        self.funcMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.funcMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.funcMenu)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 65))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setMinimumSize(QSize(0, 65))
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/menu.png);")

        self.verticalLayout_5.addWidget(self.toggleButton)


        self.verticalLayout_3.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.funcMenu)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMaximumSize(QSize(16777215, 325))
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.topMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.topMenu)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(0, 65))
        self.home_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/home.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 16px solid transparent;\n"
"text-align: left;\n"
"padding-left: 80px;\n"
"")

        self.verticalLayout_4.addWidget(self.home_btn)

        self.Elc_btn = QPushButton(self.topMenu)
        self.Elc_btn.setObjectName(u"Elc_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Elc_btn.sizePolicy().hasHeightForWidth())
        self.Elc_btn.setSizePolicy(sizePolicy)
        self.Elc_btn.setMinimumSize(QSize(3, 65))
        self.Elc_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Elc_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/light1.png);")

        self.verticalLayout_4.addWidget(self.Elc_btn)

        self.Geo_btn = QPushButton(self.topMenu)
        self.Geo_btn.setObjectName(u"Geo_btn")
        sizePolicy.setHeightForWidth(self.Geo_btn.sizePolicy().hasHeightForWidth())
        self.Geo_btn.setSizePolicy(sizePolicy)
        self.Geo_btn.setMinimumSize(QSize(0, 65))
        self.Geo_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Geo_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/funnel.png);")

        self.verticalLayout_4.addWidget(self.Geo_btn)

        self.Cal_btn = QPushButton(self.topMenu)
        self.Cal_btn.setObjectName(u"Cal_btn")
        sizePolicy.setHeightForWidth(self.Cal_btn.sizePolicy().hasHeightForWidth())
        self.Cal_btn.setSizePolicy(sizePolicy)
        self.Cal_btn.setMinimumSize(QSize(0, 65))
        self.Cal_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Cal_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cal.png);")

        self.verticalLayout_4.addWidget(self.Cal_btn)

        self.Save_btn = QPushButton(self.topMenu)
        self.Save_btn.setObjectName(u"Save_btn")
        sizePolicy.setHeightForWidth(self.Save_btn.sizePolicy().hasHeightForWidth())
        self.Save_btn.setSizePolicy(sizePolicy)
        self.Save_btn.setMinimumSize(QSize(0, 65))
        self.Save_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Save_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/save.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 16px solid transparent;\n"
"text-align: left;\n"
"padding-left: 80px;\n"
"")

        self.verticalLayout_4.addWidget(self.Save_btn)


        self.verticalLayout_3.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.funcMenu)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setMinimumSize(QSize(0, 0))
        self.bottomMenu.setMaximumSize(QSize(16777215, 16777215))
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.blank = QFrame(self.bottomMenu)
        self.blank.setObjectName(u"blank")
        self.blank.setFrameShape(QFrame.NoFrame)
        self.blank.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.blank)

        self.bottomBtn = QFrame(self.bottomMenu)
        self.bottomBtn.setObjectName(u"bottomBtn")
        self.bottomBtn.setMinimumSize(QSize(0, 50))
        self.bottomBtn.setMaximumSize(QSize(16777215, 50))
        self.bottomBtn.setFrameShape(QFrame.NoFrame)
        self.bottomBtn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.bottomBtn)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.bottomButton = QPushButton(self.bottomBtn)
        self.bottomButton.setObjectName(u"bottomButton")
        self.bottomButton.setMinimumSize(QSize(0, 50))
        self.bottomButton.setMaximumSize(QSize(16777215, 50))
        self.bottomButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.bottomButton.setStyleSheet(u"background-image: url(:/icons/images/icons/settings.png);\n"
"border-bottom-left-radius:10px;\n"
"")

        self.verticalLayout_10.addWidget(self.bottomButton)


        self.verticalLayout_9.addWidget(self.bottomBtn)


        self.verticalLayout_3.addWidget(self.bottomMenu)


        self.verticalLayout_2.addWidget(self.funcMenu)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.extraLeftBox = QStackedWidget(self.BackGround)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraLeftBox_elc = QWidget()
        self.extraLeftBox_elc.setObjectName(u"extraLeftBox_elc")
        self.verticalLayout_14 = QVBoxLayout(self.extraLeftBox_elc)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.extraTop = QFrame(self.extraLeftBox_elc)
        self.extraTop.setObjectName(u"extraTop")
        self.extraTop.setMinimumSize(QSize(0, 65))
        self.extraTop.setMaximumSize(QSize(16777215, 65))
        self.extraTop.setFrameShape(QFrame.StyledPanel)
        self.extraTop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.extraTop)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.extraToplogo = QFrame(self.extraTop)
        self.extraToplogo.setObjectName(u"extraToplogo")
        self.extraToplogo.setMinimumSize(QSize(40, 0))
        self.extraToplogo.setMaximumSize(QSize(40, 40))
        self.extraToplogo.setStyleSheet(u"background-image: url(:/icons/images/icons/light_mini.png);")
        self.extraToplogo.setFrameShape(QFrame.NoFrame)
        self.extraToplogo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.extraToplogo)

        self.extraTopLabel = QLabel(self.extraTop)
        self.extraTopLabel.setObjectName(u"extraTopLabel")
        self.extraTopLabel.setMinimumSize(QSize(120, 0))
        self.extraTopLabel.setMaximumSize(QSize(120, 16777215))
        self.extraTopLabel.setStyleSheet(u"font: 20pt \"\u9ed1\u4f53\";")
        self.extraTopLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.extraTopLabel)

        self.extraCloseBtn = QPushButton(self.extraTop)
        self.extraCloseBtn.setObjectName(u"extraCloseBtn")
        self.extraCloseBtn.setMinimumSize(QSize(40, 40))
        self.extraCloseBtn.setMaximumSize(QSize(40, 40))
        self.extraCloseBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.extraCloseBtn.setStyleSheet(u"image: url(:/icons/images/icons/return.png);")
        self.extraCloseBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.extraCloseBtn)


        self.verticalLayout_14.addWidget(self.extraTop)

        self.extraTopMenu = QFrame(self.extraLeftBox_elc)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setMinimumSize(QSize(0, 265))
        self.extraTopMenu.setMaximumSize(QSize(16777215, 265))
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.file_pole = QFrame(self.extraTopMenu)
        self.file_pole.setObjectName(u"file_pole")
        self.file_pole.setFrameShape(QFrame.StyledPanel)
        self.file_pole.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.file_pole)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.file_label = QFrame(self.file_pole)
        self.file_label.setObjectName(u"file_label")
        self.file_label.setMaximumSize(QSize(16777215, 20))
        self.file_label.setFrameShape(QFrame.StyledPanel)
        self.file_label.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.file_label)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_file = QLabel(self.file_label)
        self.label_file.setObjectName(u"label_file")
        self.label_file.setStyleSheet(u"color: rgb(132, 132, 197);")

        self.verticalLayout_24.addWidget(self.label_file)


        self.verticalLayout_23.addWidget(self.file_label)

        self.file_input = QFrame(self.file_pole)
        self.file_input.setObjectName(u"file_input")
        self.file_input.setFrameShape(QFrame.StyledPanel)
        self.file_input.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.file_input)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.file_input)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.file_open = QPushButton(self.file_input)
        self.file_open.setObjectName(u"file_open")
        self.file_open.setMinimumSize(QSize(60, 30))
        self.file_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.file_open.setStyleSheet(u"color: rgb(100, 149, 237);\n"
"font: 16pt \"\u9ed1\u4f53\";")

        self.horizontalLayout_2.addWidget(self.file_open)


        self.verticalLayout_23.addWidget(self.file_input)

        self.frame_pole = QFrame(self.file_pole)
        self.frame_pole.setObjectName(u"frame_pole")
        self.frame_pole.setMinimumSize(QSize(0, 65))
        self.frame_pole.setMaximumSize(QSize(16777215, 65))
        self.frame_pole.setFrameShape(QFrame.StyledPanel)
        self.frame_pole.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_pole)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 5, 0)
        self.pole_logo = QFrame(self.frame_pole)
        self.pole_logo.setObjectName(u"pole_logo")
        self.pole_logo.setMaximumSize(QSize(40, 40))
        self.pole_logo.setStyleSheet(u"background-image: url(:/icons/images/icons/pole.png);")
        self.pole_logo.setFrameShape(QFrame.NoFrame)
        self.pole_logo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.pole_logo)

        self.pole_number_label = QLabel(self.frame_pole)
        self.pole_number_label.setObjectName(u"pole_number_label")
        self.pole_number_label.setMaximumSize(QSize(16777215, 16777215))
        self.pole_number_label.setStyleSheet(u"color: rgb(120, 120, 120);")

        self.horizontalLayout_4.addWidget(self.pole_number_label)

        self.spinBox_pole = QSpinBox(self.frame_pole)
        self.spinBox_pole.setObjectName(u"spinBox_pole")
        self.spinBox_pole.setMinimumSize(QSize(0, 20))
        self.spinBox_pole.setMaximumSize(QSize(16777215, 16777215))
        self.spinBox_pole.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.spinBox_pole)


        self.verticalLayout_23.addWidget(self.frame_pole)


        self.verticalLayout.addWidget(self.file_pole)

        self.pole_distance = QFrame(self.extraTopMenu)
        self.pole_distance.setObjectName(u"pole_distance")
        self.pole_distance.setFrameShape(QFrame.StyledPanel)
        self.pole_distance.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pole_distance)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.distanceText = QFrame(self.pole_distance)
        self.distanceText.setObjectName(u"distanceText")
        self.distanceText.setFrameShape(QFrame.StyledPanel)
        self.distanceText.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.distanceText)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.distanceLogo = QFrame(self.distanceText)
        self.distanceLogo.setObjectName(u"distanceLogo")
        self.distanceLogo.setMaximumSize(QSize(40, 40))
        self.distanceLogo.setStyleSheet(u"border-image: url(:/icons/images/icons/distance.png);")
        self.distanceLogo.setFrameShape(QFrame.NoFrame)
        self.distanceLogo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.distanceLogo)

        self.pol_distance_label = QLabel(self.distanceText)
        self.pol_distance_label.setObjectName(u"pol_distance_label")
        self.pol_distance_label.setMinimumSize(QSize(0, 0))
        self.pol_distance_label.setMaximumSize(QSize(16777215, 16777215))
        self.pol_distance_label.setStyleSheet(u"color: rgb(120, 120, 120);")

        self.horizontalLayout_5.addWidget(self.pol_distance_label)

        self.distanceValue = QLabel(self.distanceText)
        self.distanceValue.setObjectName(u"distanceValue")
        self.distanceValue.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.distanceValue)

        self.meter = QLabel(self.distanceText)
        self.meter.setObjectName(u"meter")
        self.meter.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.meter)


        self.verticalLayout_15.addWidget(self.distanceText)

        self.distanceWidget = QFrame(self.pole_distance)
        self.distanceWidget.setObjectName(u"distanceWidget")
        self.distanceWidget.setFrameShape(QFrame.StyledPanel)
        self.distanceWidget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.distanceWidget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalSlider = QSlider(self.distanceWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(10)

        self.verticalLayout_16.addWidget(self.horizontalSlider)


        self.verticalLayout_15.addWidget(self.distanceWidget)


        self.verticalLayout.addWidget(self.pole_distance)


        self.verticalLayout_14.addWidget(self.extraTopMenu)

        self.extraBottom = QFrame(self.extraLeftBox_elc)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setStyleSheet(u"")
        self.extraBottom.setFrameShape(QFrame.StyledPanel)
        self.extraBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.extraBottom)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pipPic = QFrame(self.extraBottom)
        self.pipPic.setObjectName(u"pipPic")
        self.pipPic.setMinimumSize(QSize(0, 140))
        self.pipPic.setMaximumSize(QSize(16777215, 140))
        self.pipPic.setStyleSheet(u"border-image: url(:/icons/images/icons/pip.png);\n"
"background-repeat:no-repeat;")
        self.pipPic.setFrameShape(QFrame.StyledPanel)
        self.pipPic.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.pipPic)

        self.pipText = QFrame(self.extraBottom)
        self.pipText.setObjectName(u"pipText")
        self.pipText.setFrameShape(QFrame.StyledPanel)
        self.pipText.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.pipText)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.textEdit = QTextEdit(self.pipText)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color:transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_18.addWidget(self.textEdit)


        self.verticalLayout_17.addWidget(self.pipText)


        self.verticalLayout_14.addWidget(self.extraBottom)

        self.extraLeftBox.addWidget(self.extraLeftBox_elc)
        self.extraLeftBox_cal = QWidget()
        self.extraLeftBox_cal.setObjectName(u"extraLeftBox_cal")
        self.verticalLayout_21 = QVBoxLayout(self.extraLeftBox_cal)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.extraTop2 = QFrame(self.extraLeftBox_cal)
        self.extraTop2.setObjectName(u"extraTop2")
        self.extraTop2.setMinimumSize(QSize(0, 65))
        self.extraTop2.setMaximumSize(QSize(16777215, 65))
        self.extraTop2.setFrameShape(QFrame.StyledPanel)
        self.extraTop2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.extraTop2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.extraToplogo2 = QFrame(self.extraTop2)
        self.extraToplogo2.setObjectName(u"extraToplogo2")
        self.extraToplogo2.setMinimumSize(QSize(40, 0))
        self.extraToplogo2.setMaximumSize(QSize(40, 40))
        self.extraToplogo2.setStyleSheet(u"background-image: url(:/icons/images/icons/cal_mini.png);")
        self.extraToplogo2.setFrameShape(QFrame.NoFrame)
        self.extraToplogo2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.extraToplogo2)

        self.extraTopLabel2 = QLabel(self.extraTop2)
        self.extraTopLabel2.setObjectName(u"extraTopLabel2")
        self.extraTopLabel2.setMinimumSize(QSize(120, 0))
        self.extraTopLabel2.setMaximumSize(QSize(120, 16777215))
        self.extraTopLabel2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.extraTopLabel2)

        self.extraCloseBtn2 = QPushButton(self.extraTop2)
        self.extraCloseBtn2.setObjectName(u"extraCloseBtn2")
        self.extraCloseBtn2.setMinimumSize(QSize(40, 40))
        self.extraCloseBtn2.setMaximumSize(QSize(40, 40))
        self.extraCloseBtn2.setCursor(QCursor(Qt.PointingHandCursor))
        self.extraCloseBtn2.setStyleSheet(u"image: url(:/icons/images/icons/return.png);")
        self.extraCloseBtn2.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.extraCloseBtn2)


        self.verticalLayout_21.addWidget(self.extraTop2)

        self.extraTopMenu2 = QFrame(self.extraLeftBox_cal)
        self.extraTopMenu2.setObjectName(u"extraTopMenu2")
        self.extraTopMenu2.setMinimumSize(QSize(0, 260))
        self.extraTopMenu2.setMaximumSize(QSize(16777215, 260))
        self.extraTopMenu2.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.extraTopMenu2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.btn_elcCal = QPushButton(self.extraTopMenu2)
        self.btn_elcCal.setObjectName(u"btn_elcCal")
        self.btn_elcCal.setMinimumSize(QSize(0, 65))

        self.verticalLayout_19.addWidget(self.btn_elcCal)

        self.btn_geoCal = QPushButton(self.extraTopMenu2)
        self.btn_geoCal.setObjectName(u"btn_geoCal")
        self.btn_geoCal.setMinimumSize(QSize(0, 65))

        self.verticalLayout_19.addWidget(self.btn_geoCal)

        self.btn_weight = QPushButton(self.extraTopMenu2)
        self.btn_weight.setObjectName(u"btn_weight")
        self.btn_weight.setMinimumSize(QSize(0, 65))

        self.verticalLayout_19.addWidget(self.btn_weight)

        self.btn_FinalIndex = QPushButton(self.extraTopMenu2)
        self.btn_FinalIndex.setObjectName(u"btn_FinalIndex")
        self.btn_FinalIndex.setMinimumSize(QSize(0, 65))

        self.verticalLayout_19.addWidget(self.btn_FinalIndex)


        self.verticalLayout_21.addWidget(self.extraTopMenu2)

        self.extraBottom2 = QFrame(self.extraLeftBox_cal)
        self.extraBottom2.setObjectName(u"extraBottom2")
        self.extraBottom2.setFrameShape(QFrame.StyledPanel)
        self.extraBottom2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_21.addWidget(self.extraBottom2)

        self.extraLeftBox.addWidget(self.extraLeftBox_cal)
        self.extraLeftBox_file = QWidget()
        self.extraLeftBox_file.setObjectName(u"extraLeftBox_file")
        self.verticalLayout_31 = QVBoxLayout(self.extraLeftBox_file)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.extraTop3 = QFrame(self.extraLeftBox_file)
        self.extraTop3.setObjectName(u"extraTop3")
        self.extraTop3.setMinimumSize(QSize(0, 65))
        self.extraTop3.setMaximumSize(QSize(16777215, 65))
        self.extraTop3.setFrameShape(QFrame.StyledPanel)
        self.extraTop3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.extraTop3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.extraToplogo3 = QFrame(self.extraTop3)
        self.extraToplogo3.setObjectName(u"extraToplogo3")
        self.extraToplogo3.setMinimumSize(QSize(40, 0))
        self.extraToplogo3.setMaximumSize(QSize(40, 40))
        self.extraToplogo3.setLayoutDirection(Qt.LeftToRight)
        self.extraToplogo3.setStyleSheet(u"background-image: url(:/icons/images/icons/save_mini.png);\n"
"\n"
"")
        self.extraToplogo3.setFrameShape(QFrame.NoFrame)
        self.extraToplogo3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.extraToplogo3)

        self.extraTopLabel3 = QLabel(self.extraTop3)
        self.extraTopLabel3.setObjectName(u"extraTopLabel3")
        self.extraTopLabel3.setMinimumSize(QSize(120, 0))
        self.extraTopLabel3.setMaximumSize(QSize(120, 16777215))
        self.extraTopLabel3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.extraTopLabel3)

        self.extraCloseBtn3 = QPushButton(self.extraTop3)
        self.extraCloseBtn3.setObjectName(u"extraCloseBtn3")
        self.extraCloseBtn3.setMinimumSize(QSize(40, 40))
        self.extraCloseBtn3.setMaximumSize(QSize(40, 40))
        self.extraCloseBtn3.setCursor(QCursor(Qt.PointingHandCursor))
        self.extraCloseBtn3.setStyleSheet(u"image: url(:/icons/images/icons/return.png);")
        self.extraCloseBtn3.setIconSize(QSize(40, 40))

        self.horizontalLayout_10.addWidget(self.extraCloseBtn3)


        self.verticalLayout_31.addWidget(self.extraTop3)

        self.extraTopMenu3 = QFrame(self.extraLeftBox_file)
        self.extraTopMenu3.setObjectName(u"extraTopMenu3")
        self.extraTopMenu3.setMinimumSize(QSize(0, 160))
        self.extraTopMenu3.setMaximumSize(QSize(16777215, 160))
        self.extraTopMenu3.setFrameShape(QFrame.StyledPanel)
        self.extraTopMenu3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.extraTopMenu3)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.btn_res = QPushButton(self.extraTopMenu3)
        self.btn_res.setObjectName(u"btn_res")
        self.btn_res.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_22.addWidget(self.btn_res)

        self.btn_img = QPushButton(self.extraTopMenu3)
        self.btn_img.setObjectName(u"btn_img")
        self.btn_img.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_22.addWidget(self.btn_img)


        self.verticalLayout_31.addWidget(self.extraTopMenu3)

        self.extraBottom3 = QFrame(self.extraLeftBox_file)
        self.extraBottom3.setObjectName(u"extraBottom3")
        self.extraBottom3.setFrameShape(QFrame.StyledPanel)
        self.extraBottom3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_31.addWidget(self.extraBottom3)

        self.extraLeftBox.addWidget(self.extraLeftBox_file)

        self.horizontalLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.BackGround)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.TopContent = QFrame(self.contentBox)
        self.TopContent.setObjectName(u"TopContent")
        self.TopContent.setMinimumSize(QSize(0, 65))
        self.TopContent.setMaximumSize(QSize(16777215, 65))
        self.TopContent.setFrameShape(QFrame.NoFrame)
        self.TopContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.TopContent)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.TopContent)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 65))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame)

        self.frame_2 = QFrame(self.TopContent)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(160, 65))
        self.frame_2.setMaximumSize(QSize(160, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setSpacing(8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(8, 0, 8, 0)
        self.minBtn = QPushButton(self.frame_2)
        self.minBtn.setObjectName(u"minBtn")
        self.minBtn.setMinimumSize(QSize(40, 40))
        self.minBtn.setStyleSheet(u"image: url(:/icons/images/icons/minimize.png);")

        self.horizontalLayout_9.addWidget(self.minBtn)

        self.maxBtn = QPushButton(self.frame_2)
        self.maxBtn.setObjectName(u"maxBtn")
        self.maxBtn.setMinimumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxBtn.setIcon(icon)
        self.maxBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_9.addWidget(self.maxBtn)

        self.exitBtn = QPushButton(self.frame_2)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMinimumSize(QSize(40, 40))
        self.exitBtn.setStyleSheet(u"image: url(:/icons/images/icons/x.png);")

        self.horizontalLayout_9.addWidget(self.exitBtn)


        self.horizontalLayout_7.addWidget(self.frame_2)


        self.verticalLayout_6.addWidget(self.TopContent)

        self.BotContent = QFrame(self.contentBox)
        self.BotContent.setObjectName(u"BotContent")
        self.BotContent.setMinimumSize(QSize(0, 450))
        self.BotContent.setMaximumSize(QSize(16777215, 16777215))
        self.BotContent.setStyleSheet(u"")
        self.BotContent.setFrameShape(QFrame.NoFrame)
        self.BotContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.BotContent)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.page_container = QFrame(self.BotContent)
        self.page_container.setObjectName(u"page_container")
        self.page_container.setStyleSheet(u"")
        self.page_container.setFrameShape(QFrame.StyledPanel)
        self.page_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.page_container)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.page_container)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/school.png);")
        self.stackedWidget.addWidget(self.home)
        self.geo = QWidget()
        self.geo.setObjectName(u"geo")
        self.verticalLayout_13 = QVBoxLayout(self.geo)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.parameter_frame = QFrame(self.geo)
        self.parameter_frame.setObjectName(u"parameter_frame")
        self.parameter_frame.setMinimumSize(QSize(0, 0))
        self.parameter_frame.setMaximumSize(QSize(16777215, 360))
        self.parameter_frame.setFrameShape(QFrame.StyledPanel)
        self.parameter_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.parameter_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.generalPara = QFrame(self.parameter_frame)
        self.generalPara.setObjectName(u"generalPara")
        self.generalPara.setFrameShape(QFrame.StyledPanel)
        self.generalPara.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.generalPara)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_layer = QFrame(self.generalPara)
        self.frame_layer.setObjectName(u"frame_layer")
        self.frame_layer.setMinimumSize(QSize(0, 20))
        self.frame_layer.setMaximumSize(QSize(16777215, 30))
        self.frame_layer.setFrameShape(QFrame.StyledPanel)
        self.frame_layer.setFrameShadow(QFrame.Raised)
        self.comboBox = QComboBox(self.frame_layer)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 0, 101, 28))
        self.layer = QLabel(self.frame_layer)
        self.layer.setObjectName(u"layer")
        self.layer.setGeometry(QRect(1, 1, 111, 25))
        self.layer.setMinimumSize(QSize(0, 0))
        self.layer.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.frame_layer)

        self.groupBox_1 = QGroupBox(self.generalPara)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.gridLayout_2 = QGridLayout(self.groupBox_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setContentsMargins(0, 0, 50, 0)
        self.doubleSpinBox_depth = QDoubleSpinBox(self.groupBox_1)
        self.doubleSpinBox_depth.setObjectName(u"doubleSpinBox_depth")
        self.doubleSpinBox_depth.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_depth.setCursor(QCursor(Qt.PointingHandCursor))
        self.doubleSpinBox_depth.setMaximum(99999.99)

        self.gridLayout_2.addWidget(self.doubleSpinBox_depth, 1, 1, 1, 1)

        self.doubleSpinBox_stress = QDoubleSpinBox(self.groupBox_1)
        self.doubleSpinBox_stress.setObjectName(u"doubleSpinBox_stress")
        self.doubleSpinBox_stress.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_stress.setCursor(QCursor(Qt.PointingHandCursor))
        self.doubleSpinBox_stress.setMaximum(99999.99)

        self.gridLayout_2.addWidget(self.doubleSpinBox_stress, 2, 1, 1, 1)

        self.depth = QLabel(self.groupBox_1)
        self.depth.setObjectName(u"depth")
        self.depth.setMaximumSize(QSize(16777215, 30))
        self.depth.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.depth, 1, 0, 1, 1)

        self.doubleSpinBox_phi = QDoubleSpinBox(self.groupBox_1)
        self.doubleSpinBox_phi.setObjectName(u"doubleSpinBox_phi")
        self.doubleSpinBox_phi.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_phi.setCursor(QCursor(Qt.PointingHandCursor))
        self.doubleSpinBox_phi.setMaximum(99999.99)

        self.gridLayout_2.addWidget(self.doubleSpinBox_phi, 4, 1, 1, 1)

        self.phi = QLabel(self.groupBox_1)
        self.phi.setObjectName(u"phi")
        self.phi.setMaximumSize(QSize(16777215, 30))
        self.phi.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.phi, 4, 0, 1, 1)

        self.doubleSpinBox_Cm_col = QDoubleSpinBox(self.groupBox_1)
        self.doubleSpinBox_Cm_col.setObjectName(u"doubleSpinBox_Cm_col")
        self.doubleSpinBox_Cm_col.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_Cm_col.setCursor(QCursor(Qt.PointingHandCursor))
        self.doubleSpinBox_Cm_col.setMaximum(99999.99)

        self.gridLayout_2.addWidget(self.doubleSpinBox_Cm_col, 3, 1, 1, 1)

        self.doubleSpinBox_thick = QDoubleSpinBox(self.groupBox_1)
        self.doubleSpinBox_thick.setObjectName(u"doubleSpinBox_thick")
        self.doubleSpinBox_thick.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_thick.setCursor(QCursor(Qt.PointingHandCursor))
        self.doubleSpinBox_thick.setMaximum(99999.99)

        self.gridLayout_2.addWidget(self.doubleSpinBox_thick, 0, 1, 1, 1)

        self.Cm_col = QLabel(self.groupBox_1)
        self.Cm_col.setObjectName(u"Cm_col")
        self.Cm_col.setMaximumSize(QSize(16777215, 30))
        self.Cm_col.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Cm_col, 3, 0, 1, 1)

        self.stress = QLabel(self.groupBox_1)
        self.stress.setObjectName(u"stress")
        self.stress.setMaximumSize(QSize(16777215, 30))
        self.stress.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.stress, 2, 0, 1, 1)

        self.coal_thick = QLabel(self.groupBox_1)
        self.coal_thick.setObjectName(u"coal_thick")
        self.coal_thick.setMinimumSize(QSize(0, 30))
        self.coal_thick.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.coal_thick, 0, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 3)

        self.verticalLayout_25.addWidget(self.groupBox_1)


        self.horizontalLayout_8.addWidget(self.generalPara)

        self.groupBox = QGroupBox(self.parameter_frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(0, 0, 50, 10)
        self.extension = QLabel(self.groupBox)
        self.extension.setObjectName(u"extension")
        self.extension.setMaximumSize(QSize(16777215, 30))
        self.extension.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.extension, 4, 0, 1, 1)

        self.permeability = QLabel(self.groupBox)
        self.permeability.setObjectName(u"permeability")
        self.permeability.setMinimumSize(QSize(0, 30))
        self.permeability.setMaximumSize(QSize(16777215, 30))
        self.permeability.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.permeability, 6, 0, 2, 1)

        self.h = QLabel(self.groupBox)
        self.h.setObjectName(u"h")
        self.h.setMaximumSize(QSize(16777215, 30))
        self.h.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.h, 1, 0, 1, 1)

        self.doubleSpinBox_G = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_G.setObjectName(u"doubleSpinBox_G")
        self.doubleSpinBox_G.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_G.setCursor(QCursor(Qt.PointingHandCursor))
        self.doubleSpinBox_G.setMaximum(99999.99)

        self.gridLayout.addWidget(self.doubleSpinBox_G, 4, 1, 1, 1)

        self.G = QLabel(self.groupBox)
        self.G.setObjectName(u"G")
        self.G.setMaximumSize(QSize(16777215, 30))
        self.G.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.G, 2, 0, 1, 1)

        self.doubleSpinBox_phi0 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_phi0.setObjectName(u"doubleSpinBox_phi0")
        self.doubleSpinBox_phi0.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_phi0.setCursor(QCursor(Qt.PointingHandCursor))
        self.doubleSpinBox_phi0.setMaximum(99999.99)
        self.gridLayout.addWidget(self.doubleSpinBox_phi0, 5, 1, 2, 1)

        self.doubleSpinBox_h = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_h.setObjectName(u"doubleSpinBox_h")
        self.doubleSpinBox_h.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_h.setCursor(QCursor(Qt.PointingHandCursor))
        self.doubleSpinBox_h.setMaximum(99999.99)

        self.gridLayout.addWidget(self.doubleSpinBox_h, 1, 1, 1, 1)

        self.bd = QLabel(self.groupBox)
        self.bd.setObjectName(u"bd")
        self.bd.setMinimumSize(QSize(0, 30))
        self.bd.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.bd, 0, 0, 1, 1)

        self.cohesion = QLabel(self.groupBox)
        self.cohesion.setObjectName(u"cohesion")
        self.cohesion.setMaximumSize(QSize(16777215, 30))
        self.cohesion.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.cohesion, 3, 0, 1, 1)

        self.angle = QLabel(self.groupBox)
        self.angle.setObjectName(u"angle")
        self.angle.setMinimumSize(QSize(0, 30))
        self.angle.setMaximumSize(QSize(16777215, 30))
        self.angle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.angle, 5, 0, 1, 1)

        self.doubleSpinBox_Cm = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_Cm.setObjectName(u"doubleSpinBox_Cm")
        self.doubleSpinBox_Cm.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_Cm.setCursor(QCursor(Qt.PointingHandCursor))
        self.doubleSpinBox_Cm.setMaximum(99999.99)

        self.gridLayout.addWidget(self.doubleSpinBox_Cm, 3, 1, 1, 1)

        self.doubleSpinBox_permeability = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_permeability.setObjectName(u"doubleSpinBox_permeability")
        self.doubleSpinBox_permeability.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_permeability.setCursor(QCursor(Qt.PointingHandCursor))
        self.doubleSpinBox_permeability.setMaximum(99999.99)
        self.gridLayout.addWidget(self.doubleSpinBox_permeability, 7, 1, 1, 1)

        self.doubleSpinBox_bd = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_bd.setObjectName(u"doubleSpinBox_bd")
        self.doubleSpinBox_bd.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_bd.setCursor(QCursor(Qt.PointingHandCursor))
        self.doubleSpinBox_bd.setMaximum(99999.99)
        self.gridLayout.addWidget(self.doubleSpinBox_bd, 0, 1, 1, 1)

        self.doubleSpinBox_E = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_E.setObjectName(u"doubleSpinBox_E")
        self.doubleSpinBox_E.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_E.setCursor(QCursor(Qt.PointingHandCursor))
        self.doubleSpinBox_E.setMaximum(99999.99)
        self.gridLayout.addWidget(self.doubleSpinBox_E, 2, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)

        self.horizontalLayout_8.addWidget(self.groupBox)

        self.geoFuncMenu = QFrame(self.parameter_frame)
        self.geoFuncMenu.setObjectName(u"geoFuncMenu")
        self.geoFuncMenu.setFrameShape(QFrame.StyledPanel)
        self.geoFuncMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.geoFuncMenu)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.geo_input = QPushButton(self.geoFuncMenu)
        self.geo_input.setObjectName(u"geo_input")
        self.geo_input.setMinimumSize(QSize(0, 71))
        self.geo_input.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_27.addWidget(self.geo_input)

        self.geo_add = QPushButton(self.geoFuncMenu)
        self.geo_add.setObjectName(u"geo_add")
        self.geo_add.setMinimumSize(QSize(70, 71))
        self.geo_add.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_27.addWidget(self.geo_add)

        self.geo_del = QPushButton(self.geoFuncMenu)
        self.geo_del.setObjectName(u"geo_del")
        self.geo_del.setMinimumSize(QSize(0, 71))
        self.geo_del.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_27.addWidget(self.geo_del)

        self.geo_clear = QPushButton(self.geoFuncMenu)
        self.geo_clear.setObjectName(u"geo_clear")
        self.geo_clear.setMinimumSize(QSize(0, 71))
        self.geo_clear.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_27.addWidget(self.geo_clear)

        self.geo_output = QPushButton(self.geoFuncMenu)
        self.geo_output.setObjectName(u"geo_output")
        self.geo_output.setMinimumSize(QSize(0, 71))
        self.geo_output.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_27.addWidget(self.geo_output)


        self.horizontalLayout_8.addWidget(self.geoFuncMenu)


        self.verticalLayout_13.addWidget(self.parameter_frame)

        self.list_frame = QFrame(self.geo)
        self.list_frame.setObjectName(u"list_frame")
        self.list_frame.setMinimumSize(QSize(0, 100))
        self.list_frame.setMaximumSize(QSize(16777215, 16777215))
        self.list_frame.setFrameShape(QFrame.NoFrame)
        self.list_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.list_frame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.layer1 = QLabel(self.list_frame)
        self.layer1.setObjectName(u"layer1")

        self.verticalLayout_12.addWidget(self.layer1)

        self.tableWidget = QTableWidget(self.list_frame)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tableWidget.rowCount() < 12):
            self.tableWidget.setRowCount(12)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem19)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(Qt.DashLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_13.addWidget(self.list_frame)

        self.stackedWidget.addWidget(self.geo)
        self.elc = QWidget()
        self.elc.setObjectName(u"elc")
        self.verticalLayout_20 = QVBoxLayout(self.elc)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.contour_rho = QGraphicsView(self.elc)
        self.contour_rho.setObjectName(u"contour_rho")

        self.verticalLayout_20.addWidget(self.contour_rho)

        self.contour_label = QLabel(self.elc)
        self.contour_label.setObjectName(u"contour_label")
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.contour_label.setFont(font)
        self.contour_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.contour_label)

        self.curve_rho = QGraphicsView(self.elc)
        self.curve_rho.setObjectName(u"curve_rho")

        self.verticalLayout_20.addWidget(self.curve_rho)

        self.curve_label = QLabel(self.elc)
        self.curve_label.setObjectName(u"curve_label")
        self.curve_label.setFont(font)
        self.curve_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.curve_label)

        self.stackedWidget.addWidget(self.elc)
        self.destroy_depth = QWidget()
        self.destroy_depth.setObjectName(u"destroy_depth")
        self.horizontalLayout_18 = QHBoxLayout(self.destroy_depth)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.groupBox_d = QGroupBox(self.destroy_depth)
        self.groupBox_d.setObjectName(u"groupBox_d")
        self.groupBox_d.setMinimumSize(QSize(200, 0))
        self.groupBox_d.setAlignment(Qt.AlignCenter)
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_d)
        self.verticalLayout_26.setSpacing(2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.destroy_btn = QPushButton(self.groupBox_d)
        self.destroy_btn.setObjectName(u"destroy_btn")
        self.destroy_btn.setMinimumSize(QSize(0, 60))

        self.verticalLayout_26.addWidget(self.destroy_btn)

        self.coal_title = QLabel(self.groupBox_d)
        self.coal_title.setObjectName(u"coal_title")
        self.coal_title.setFont(font)
        self.coal_title.setFrameShape(QFrame.WinPanel)
        self.coal_title.setLineWidth(5)
        self.coal_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.coal_title)

        self.frame_coal_thick = QFrame(self.groupBox_d)
        self.frame_coal_thick.setObjectName(u"frame_coal_thick")
        self.frame_coal_thick.setFrameShape(QFrame.StyledPanel)
        self.frame_coal_thick.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_coal_thick)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.coal_thick_d = QLabel(self.frame_coal_thick)
        self.coal_thick_d.setObjectName(u"coal_thick_d")
        self.coal_thick_d.setMinimumSize(QSize(0, 30))
        self.coal_thick_d.setFont(font)
        self.coal_thick_d.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.coal_thick_d)

        self.coal_thick__d_value = QLabel(self.frame_coal_thick)
        self.coal_thick__d_value.setObjectName(u"coal_thick__d_value")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.coal_thick__d_value.setFont(font1)
        self.coal_thick__d_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.coal_thick__d_value)


        self.verticalLayout_26.addWidget(self.frame_coal_thick)

        self.frame_depth = QFrame(self.groupBox_d)
        self.frame_depth.setObjectName(u"frame_depth")
        self.frame_depth.setFrameShape(QFrame.StyledPanel)
        self.frame_depth.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_depth)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.depth_d = QLabel(self.frame_depth)
        self.depth_d.setObjectName(u"depth_d")
        self.depth_d.setMaximumSize(QSize(16777215, 30))
        self.depth_d.setFont(font)
        self.depth_d.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.depth_d)

        self.depth_d_value = QLabel(self.frame_depth)
        self.depth_d_value.setObjectName(u"depth_d_value")
        self.depth_d_value.setFont(font1)
        self.depth_d_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.depth_d_value)


        self.verticalLayout_26.addWidget(self.frame_depth)

        self.frame_stress = QFrame(self.groupBox_d)
        self.frame_stress.setObjectName(u"frame_stress")
        self.frame_stress.setFont(font)
        self.frame_stress.setFrameShape(QFrame.StyledPanel)
        self.frame_stress.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_stress)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stress_d = QLabel(self.frame_stress)
        self.stress_d.setObjectName(u"stress_d")
        self.stress_d.setMaximumSize(QSize(16777215, 30))
        self.stress_d.setFont(font)
        self.stress_d.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.stress_d)

        self.stress_d_value = QLabel(self.frame_stress)
        self.stress_d_value.setObjectName(u"stress_d_value")
        self.stress_d_value.setFont(font1)
        self.stress_d_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.stress_d_value)


        self.verticalLayout_26.addWidget(self.frame_stress)

        self.frame_Cm = QFrame(self.groupBox_d)
        self.frame_Cm.setObjectName(u"frame_Cm")
        self.frame_Cm.setFont(font)
        self.frame_Cm.setFrameShape(QFrame.StyledPanel)
        self.frame_Cm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_Cm)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.Cm_col_d = QLabel(self.frame_Cm)
        self.Cm_col_d.setObjectName(u"Cm_col_d")
        self.Cm_col_d.setMaximumSize(QSize(16777215, 30))
        self.Cm_col_d.setFont(font)
        self.Cm_col_d.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.Cm_col_d)

        self.Cm_col_d_value = QLabel(self.frame_Cm)
        self.Cm_col_d_value.setObjectName(u"Cm_col_d_value")
        self.Cm_col_d_value.setFont(font1)
        self.Cm_col_d_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.Cm_col_d_value)


        self.verticalLayout_26.addWidget(self.frame_Cm)

        self.frame_phi = QFrame(self.groupBox_d)
        self.frame_phi.setObjectName(u"frame_phi")
        self.frame_phi.setFrameShape(QFrame.StyledPanel)
        self.frame_phi.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_phi)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.phi_d = QLabel(self.frame_phi)
        self.phi_d.setObjectName(u"phi_d")
        self.phi_d.setMaximumSize(QSize(16777215, 30))
        self.phi_d.setFont(font)
        self.phi_d.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.phi_d)

        self.phi_d_value = QLabel(self.frame_phi)
        self.phi_d_value.setObjectName(u"phi_d_value")
        self.phi_d_value.setFont(font1)
        self.phi_d_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.phi_d_value)


        self.verticalLayout_26.addWidget(self.frame_phi)


        self.horizontalLayout_18.addWidget(self.groupBox_d)

        self.groupBox_d_show = QGroupBox(self.destroy_depth)
        self.groupBox_d_show.setObjectName(u"groupBox_d_show")
        self.groupBox_d_show.setAlignment(Qt.AlignCenter)
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_d_show)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.graph_depth = QGraphicsView(self.groupBox_d_show)
        self.graph_depth.setObjectName(u"graph_depth")
        self.graph_depth.setMaximumSize(QSize(16777215, 150))
        self.graph_depth.setFrameShadow(QFrame.Plain)

        self.verticalLayout_28.addWidget(self.graph_depth)

        self.tableWidget_2 = QTableWidget(self.groupBox_d_show)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        if (self.tableWidget_2.rowCount() < 8):
            self.tableWidget_2.setRowCount(8)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem29)
        brush = QBrush(QColor(255, 85, 0, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem30.setBackground(brush1);
        __qtablewidgetitem30.setForeground(brush);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem31)
        brush2 = QBrush(QColor(255, 85, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem31.setBackground(brush3);
        __qtablewidgetitem31.setForeground(brush2);
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem31)
        __qtablewidgetitem311 = QTableWidgetItem()
        __qtablewidgetitem311.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem311)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem32)
        __qtablewidgetitem321 = QTableWidgetItem()
        __qtablewidgetitem321.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem321)
        __qtablewidgetitem32.setBackground(brush3);
        __qtablewidgetitem32.setForeground(brush2);
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(3, 0, __qtablewidgetitem33)
        __qtablewidgetitem331 = QTableWidgetItem()
        __qtablewidgetitem331.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(3, 1, __qtablewidgetitem331)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(4, 0, __qtablewidgetitem34)
        __qtablewidgetitem341 = QTableWidgetItem()
        __qtablewidgetitem341.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(4, 1, __qtablewidgetitem341)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(5, 0, __qtablewidgetitem35)
        __qtablewidgetitem351 = QTableWidgetItem()
        __qtablewidgetitem351.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(5, 1, __qtablewidgetitem351)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(6, 0, __qtablewidgetitem36)
        __qtablewidgetitem361 = QTableWidgetItem()
        __qtablewidgetitem361.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(6, 1, __qtablewidgetitem361)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(7, 0, __qtablewidgetitem37)
        __qtablewidgetitem371 = QTableWidgetItem()
        __qtablewidgetitem371.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(7, 1, __qtablewidgetitem371)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(300)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_2.verticalHeader().setHighlightSections(True)

        self.verticalLayout_28.addWidget(self.tableWidget_2)


        self.horizontalLayout_18.addWidget(self.groupBox_d_show)

        self.stackedWidget.addWidget(self.destroy_depth)
        self.AHP = QWidget()
        self.AHP.setObjectName(u"AHP")
        self.horizontalLayout_19 = QHBoxLayout(self.AHP)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_input = QFrame(self.AHP)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setMinimumSize(QSize(0, 0))
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_input)
        self.verticalLayout_32.setSpacing(5)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_btn = QFrame(self.frame_input)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMinimumSize(QSize(0, 100))
        self.frame_btn.setMaximumSize(QSize(16777215, 100))
        self.frame_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_btn)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.btn_data = QPushButton(self.frame_btn)
        self.btn_data.setObjectName(u"btn_data")
        self.btn_data.setMinimumSize(QSize(0, 33))

        self.verticalLayout_35.addWidget(self.btn_data)

        self.btn_weight_ahp = QPushButton(self.frame_btn)
        self.btn_weight_ahp.setObjectName(u"btn_weight_ahp")
        self.btn_weight_ahp.setMinimumSize(QSize(0, 33))

        self.verticalLayout_35.addWidget(self.btn_weight_ahp)

        self.btn_weight_change = QPushButton(self.frame_btn)
        self.btn_weight_change.setObjectName(u"btn_weight_change")
        self.btn_weight_change.setMinimumSize(QSize(0, 33))

        self.verticalLayout_35.addWidget(self.btn_weight_change)


        self.verticalLayout_32.addWidget(self.frame_btn)

        self.mat_Edit = QPlainTextEdit(self.frame_input)
        self.mat_Edit.setObjectName(u"mat_Edit")
        self.mat_Edit.setEnabled(True)

        self.verticalLayout_32.addWidget(self.mat_Edit)


        self.horizontalLayout_19.addWidget(self.frame_input)

        self.frame_table = QFrame(self.AHP)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setMinimumSize(QSize(720, 0))
        self.frame_table.setMaximumSize(QSize(695, 16777215))
        self.frame_table.setFrameShape(QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_table)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_layer1 = QFrame(self.frame_table)
        self.frame_layer1.setObjectName(u"frame_layer1")
        self.frame_layer1.setMinimumSize(QSize(0, 220))
        font2 = QFont()
        font2.setFamilies([u"\u5b8b\u4f53"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.frame_layer1.setFont(font2)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_layer1)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.level1 = QGroupBox(self.frame_layer1)
        self.level1.setObjectName(u"level1")
        self.level1.setFont(font2)
        self.verticalLayout_33 = QVBoxLayout(self.level1)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_level1 = QTableWidget(self.level1)
        if (self.tableWidget_level1.columnCount() < 4):
            self.tableWidget_level1.setColumnCount(4)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_level1.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_level1.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_level1.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_level1.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        if (self.tableWidget_level1.rowCount() < 4):
            self.tableWidget_level1.setRowCount(4)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_level1.setVerticalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_level1.setVerticalHeaderItem(1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_level1.setVerticalHeaderItem(2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_level1.setVerticalHeaderItem(3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(0, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(0, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(0, 2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(0, 3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(1, 0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(1, 1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(1, 2, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(1, 3, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(2, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(2, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(2, 2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(2, 3, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(3, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(3, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(3, 2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_level1.setItem(3, 3, __qtablewidgetitem61)
        self.tableWidget_level1.setObjectName(u"tableWidget_level1")
        self.tableWidget_level1.horizontalHeader().setMinimumSectionSize(67)
        self.tableWidget_level1.horizontalHeader().setDefaultSectionSize(67)
        self.tableWidget_level1.verticalHeader().setMinimumSectionSize(43)
        self.tableWidget_level1.verticalHeader().setDefaultSectionSize(43)
        self.tableWidget_level1.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_33.addWidget(self.tableWidget_level1)


        self.horizontalLayout_20.addWidget(self.level1)

        self.plain_matrix = QPlainTextEdit(self.frame_layer1)
        self.plain_matrix.setObjectName(u"plain_matrix")
        self.plain_matrix.setEnabled(True)
        self.plain_matrix.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_20.addWidget(self.plain_matrix)


        self.verticalLayout_30.addWidget(self.frame_layer1)

        self.level2 = QGroupBox(self.frame_table)
        self.level2.setObjectName(u"level2")
        self.level2.setMinimumSize(QSize(0, 285))
        self.level2.setMaximumSize(QSize(16777215, 285))
        self.level2.setFont(font2)
        self.level2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_29 = QVBoxLayout(self.level2)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.level2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_21 = QTableWidget(self.frame_21)
        if (self.tableWidget_21.columnCount() < 2):
            self.tableWidget_21.setColumnCount(2)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(1, __qtablewidgetitem63)
        if (self.tableWidget_21.rowCount() < 2):
            self.tableWidget_21.setRowCount(2)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_21.setVerticalHeaderItem(0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_21.setVerticalHeaderItem(1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_21.setItem(0, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_21.setItem(0, 1, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_21.setItem(1, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_21.setItem(1, 1, __qtablewidgetitem69)
        self.tableWidget_21.setObjectName(u"tableWidget_21")
        self.tableWidget_21.horizontalHeader().setDefaultSectionSize(139)
        self.tableWidget_21.verticalHeader().setMinimumSectionSize(38)
        self.tableWidget_21.verticalHeader().setDefaultSectionSize(38)

        self.horizontalLayout_21.addWidget(self.tableWidget_21)

        self.tableWidget_22 = QTableWidget(self.frame_21)
        if (self.tableWidget_22.columnCount() < 2):
            self.tableWidget_22.setColumnCount(2)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(1, __qtablewidgetitem71)
        if (self.tableWidget_22.rowCount() < 2):
            self.tableWidget_22.setRowCount(2)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_22.setVerticalHeaderItem(0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_22.setVerticalHeaderItem(1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_22.setItem(0, 0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_22.setItem(0, 1, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_22.setItem(1, 0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_22.setItem(1, 1, __qtablewidgetitem77)
        self.tableWidget_22.setObjectName(u"tableWidget_22")
        self.tableWidget_22.horizontalHeader().setDefaultSectionSize(137)
        self.tableWidget_22.verticalHeader().setMinimumSectionSize(39)
        self.tableWidget_22.verticalHeader().setDefaultSectionSize(39)

        self.horizontalLayout_21.addWidget(self.tableWidget_22)


        self.verticalLayout_29.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.level2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 16777215))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_24 = QTableWidget(self.frame_22)
        if (self.tableWidget_24.columnCount() < 2):
            self.tableWidget_24.setColumnCount(2)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(1, __qtablewidgetitem79)
        if (self.tableWidget_24.rowCount() < 2):
            self.tableWidget_24.setRowCount(2)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_24.setVerticalHeaderItem(0, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_24.setVerticalHeaderItem(1, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_24.setItem(0, 0, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_24.setItem(0, 1, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_24.setItem(1, 0, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_24.setItem(1, 1, __qtablewidgetitem85)
        self.tableWidget_24.setObjectName(u"tableWidget_24")
        self.tableWidget_24.horizontalHeader().setDefaultSectionSize(138)
        self.tableWidget_24.verticalHeader().setMinimumSectionSize(39)
        self.tableWidget_24.verticalHeader().setDefaultSectionSize(39)

        self.horizontalLayout_22.addWidget(self.tableWidget_24)

        self.tableWidget_23 = QTableWidget(self.frame_22)
        if (self.tableWidget_23.columnCount() < 2):
            self.tableWidget_23.setColumnCount(2)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(1, __qtablewidgetitem87)
        if (self.tableWidget_23.rowCount() < 2):
            self.tableWidget_23.setRowCount(2)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_23.setVerticalHeaderItem(0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_23.setVerticalHeaderItem(1, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_23.setItem(0, 0, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_23.setItem(0, 1, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_23.setItem(1, 0, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_23.setItem(1, 1, __qtablewidgetitem93)
        self.tableWidget_23.setObjectName(u"tableWidget_23")
        self.tableWidget_23.horizontalHeader().setDefaultSectionSize(138)
        self.tableWidget_23.verticalHeader().setMinimumSectionSize(39)
        self.tableWidget_23.verticalHeader().setDefaultSectionSize(39)

        self.horizontalLayout_22.addWidget(self.tableWidget_23)


        self.verticalLayout_29.addWidget(self.frame_22)


        self.verticalLayout_30.addWidget(self.level2)


        self.horizontalLayout_19.addWidget(self.frame_table)

        self.stackedWidget.addWidget(self.AHP)
        self.risk = QWidget()
        self.risk.setObjectName(u"risk")
        self.verticalLayout_37 = QVBoxLayout(self.risk)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.risk_up = QFrame(self.risk)
        self.risk_up.setObjectName(u"risk_up")
        self.risk_up.setMinimumSize(QSize(0, 300))
        self.risk_up.setMaximumSize(QSize(16777215, 300))
        self.risk_up.setFrameShape(QFrame.StyledPanel)
        self.risk_up.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.risk_up)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.risk_btn = QFrame(self.risk_up)
        self.risk_btn.setObjectName(u"risk_btn")
        self.risk_btn.setFrameShape(QFrame.StyledPanel)
        self.risk_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.risk_btn)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.Single = QFrame(self.risk_btn)
        self.Single.setObjectName(u"Single")
        self.Single.setFrameShape(QFrame.StyledPanel)
        self.Single.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.Single)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.btn_single = QPushButton(self.Single)
        self.btn_single.setObjectName(u"btn_single")
        self.btn_single.setEnabled(True)
        self.btn_single.setMinimumSize(QSize(0, 150))

        self.verticalLayout_39.addWidget(self.btn_single)


        self.verticalLayout_36.addWidget(self.Single)

        self.Final = QFrame(self.risk_btn)
        self.Final.setObjectName(u"Final")
        self.Final.setMaximumSize(QSize(16777215, 16777215))
        self.Final.setFrameShape(QFrame.StyledPanel)
        self.Final.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.Final)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.btn_final = QPushButton(self.Final)
        self.btn_final.setObjectName(u"btn_final")
        self.btn_final.setMinimumSize(QSize(0, 150))

        self.verticalLayout_38.addWidget(self.btn_final)


        self.verticalLayout_36.addWidget(self.Final)


        self.horizontalLayout_23.addWidget(self.risk_btn)

        self.level_risk = QGroupBox(self.risk_up)
        self.level_risk.setObjectName(u"level_risk")
        self.level_risk.setMinimumSize(QSize(0, 285))
        self.level_risk.setMaximumSize(QSize(16777215, 16777215))
        self.level_risk.setFont(font2)
        self.level_risk.setAlignment(Qt.AlignCenter)
        self.verticalLayout_34 = QVBoxLayout(self.level_risk)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_4 = QTableWidget(self.level_risk)
        if (self.tableWidget_4.columnCount() < 4):
            self.tableWidget_4.setColumnCount(4)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem97)
        if (self.tableWidget_4.rowCount() < 8):
            self.tableWidget_4.setRowCount(8)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(0, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(1, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(2, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(3, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(4, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(5, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(6, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setVerticalHeaderItem(7, __qtablewidgetitem105)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem106.setFont(font3);
        self.tableWidget_4.setItem(0, 0, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem107.setFont(font3);
        self.tableWidget_4.setItem(0, 1, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem108.setFont(font3);
        self.tableWidget_4.setItem(0, 2, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem109.setFont(font3);
        self.tableWidget_4.setItem(0, 3, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(1, 0, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        __qtablewidgetitem111.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(1, 1, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        __qtablewidgetitem112.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(1, 2, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        __qtablewidgetitem113.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(1, 3, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        __qtablewidgetitem114.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(2, 0, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        __qtablewidgetitem115.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(2, 1, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        __qtablewidgetitem116.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(2, 2, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        __qtablewidgetitem117.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(2, 3, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        __qtablewidgetitem118.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(3, 0, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        __qtablewidgetitem119.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(3, 1, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        __qtablewidgetitem120.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(3, 2, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        __qtablewidgetitem121.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(3, 3, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        __qtablewidgetitem122.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(4, 0, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        __qtablewidgetitem123.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(4, 1, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        __qtablewidgetitem124.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(4, 2, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        __qtablewidgetitem125.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(4, 3, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(5, 0, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        __qtablewidgetitem127.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(5, 1, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        __qtablewidgetitem128.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(5, 2, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        __qtablewidgetitem129.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(5, 3, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        __qtablewidgetitem130.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(6, 0, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        __qtablewidgetitem131.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(6, 1, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        __qtablewidgetitem132.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(6, 2, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        __qtablewidgetitem133.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(6, 3, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        __qtablewidgetitem134.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(7, 0, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        __qtablewidgetitem135.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(7, 1, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        __qtablewidgetitem136.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(7, 2, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        __qtablewidgetitem137.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(7, 3, __qtablewidgetitem137)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setMinimumSize(QSize(0, 0))
        self.tableWidget_4.setSizeIncrement(QSize(0, 0))
        self.tableWidget_4.setBaseSize(QSize(0, 0))
        self.tableWidget_4.setFont(font1)
        self.tableWidget_4.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tableWidget_4.setFrameShape(QFrame.NoFrame)
        self.tableWidget_4.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_4.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_4.setGridStyle(Qt.DashLine)
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.horizontalHeader().setVisible(True)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_4.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_4.horizontalHeader().setHighlightSections(True)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_4.verticalHeader().setVisible(True)
        self.tableWidget_4.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget_4.verticalHeader().setHighlightSections(False)
        self.tableWidget_4.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_4.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_34.addWidget(self.tableWidget_4)


        self.horizontalLayout_23.addWidget(self.level_risk)


        self.verticalLayout_37.addWidget(self.risk_up)

        self.plainTextEdit = QPlainTextEdit(self.risk)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 0))

        self.verticalLayout_37.addWidget(self.plainTextEdit)

        self.stackedWidget.addWidget(self.risk)

        self.verticalLayout_11.addWidget(self.stackedWidget)


        self.verticalLayout_8.addWidget(self.page_container)

        self.info_text = QFrame(self.BotContent)
        self.info_text.setObjectName(u"info_text")
        self.info_text.setMinimumSize(QSize(0, 70))
        self.info_text.setMaximumSize(QSize(16777215, 100))
        self.info_text.setFrameShape(QFrame.NoFrame)
        self.info_text.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.info_text)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.info_text)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 0))
        self.textBrowser.setMaximumSize(QSize(16777215, 16777215))
        self.textBrowser.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_7.addWidget(self.textBrowser)

        self.bottom_bar = QFrame(self.info_text)
        self.bottom_bar.setObjectName(u"bottom_bar")
        self.bottom_bar.setMinimumSize(QSize(0, 16))
        self.bottom_bar.setFrameShape(QFrame.StyledPanel)
        self.bottom_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.bottom_bar)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.credit_label = QLabel(self.bottom_bar)
        self.credit_label.setObjectName(u"credit_label")

        self.horizontalLayout_11.addWidget(self.credit_label)

        self.frame_size_grip = QFrame(self.bottom_bar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_size_grip)


        self.verticalLayout_7.addWidget(self.bottom_bar)


        self.verticalLayout_8.addWidget(self.info_text)


        self.verticalLayout_6.addWidget(self.BotContent)


        self.horizontalLayout.addWidget(self.contentBox)

        self.leftMenu.raise_()
        self.contentBox.raise_()
        self.extraLeftBox.raise_()

        self.horizontalLayout_12.addWidget(self.BackGround)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.extraLeftBox.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
        self.comboBox.currentIndexChanged.connect(self.Table_resize)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def Table_resize(self):
        layer = self.comboBox.currentIndex()
        self.tableWidget.setEnabled(True)
        self.tableWidget.setRowCount(layer)
        for i in range(0, layer+1):
            self.lithology = QComboBox(self.tableWidget)
            self.lithology.addItems([u"\u6ce5\u5ca9", u"\u9875\u5ca9", u"\u7802\u5ca9"])
            self.tableWidget.setCellWidget(i, 0, self.lithology)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleDescription.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u6cb9\u578b\u6c14\u6d8c\u51fa\u5371\u9669\u6027<br/>\u8bc4\u4ef7\u8f6f\u4ef6V2.0</span></p></body></html>", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.Elc_btn.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6cd5\u63a2\u6d4b", None))
        self.Geo_btn.setText(QCoreApplication.translate("MainWindow", u"\u5730\u8d28\u53c2\u6570", None))
        self.Cal_btn.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.Save_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.bottomButton.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.extraTopLabel.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6cd5\u63a2\u6d4b", None))
        self.extraCloseBtn.setText("")
        self.label_file.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u96c6\u6570\u636e\u5bfc\u5165", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84", None))
        self.file_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.pole_number_label.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6781\u4e2a\u6570", None))
        self.pol_distance_label.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6781\u8ddd", None))
        self.distanceValue.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.meter.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'\u5b8b\u4f53'; font-size:16pt; font-weight:700; color:#5500ff;\">\u7535\u6781\u5e03\u7f6e\u65b9\u5f0f</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'\u5b8b\u4f53'; font-size:"
                        "10pt;\">\u4f9b\u7535\u7535\u6781</span><span style=\" font-family:'Times New Roman','serif'; font-size:10pt;\">B</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:10pt;\">\u7f6e\u4e8e\u65e0\u7a77\u8fdc\u5904\uff0c\u6d4b\u91cf\u7535\u6781\u4ee5\u56fa\u5b9a\u7535\u6781\u8ddd\u65b9\u5f0f\u76f4\u7ebf\u5e03\u7f6e,\u5176\u4e2dA\u4e3a\u4f9b\u7535\u7535\u6781\u3001M\u3001N\u4e3a\u63a5\u6536\u7535\u6781</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'\u5b8b\u4f53'; font-size:16pt; font-weight:700; color:#ff5500;\">\u6570\u636e\u91c7\u96c6\u65b9\u5f0f</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'\u5b8b\u4f53'; font-size:10pt;\">\u9996\u5148\uff0c</span><span style=\" font-family:'Times New Roman','serif'; fo"
                        "nt-size:10pt;\">A=#1\uff0cM=#2\u2026\u2026#n-1</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:10pt;\">\uff0c</span><span style=\" font-family:'Times New Roman','serif'; font-size:10pt;\">N=#3\u2026\u2026#n</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:10pt;\">\uff0c\u79fb\u52a8\u6d4b\u5f97\u7b2c\u4e00\u7ec4</span><a name=\"_x0000_t75\"></a><span style=\" font-family:'Times New Roman','serif'; font-size:10pt;\"> </span><a name=\"\u56fe\u7247_x0020_253\"></a><span style=\" font-family:'\u5b8b\u4f53'; font-size:10pt;\">\u6570</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:10pt;\">\u636e\uff1b </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'\u5b8b\u4f53'; font-size:10pt;\">\u63a5\u7740\u4f9b\u7535\u7535\u6781</span><span style=\" font-family:'Times New Roman','serif'; font-size:10pt;\">A</span><span style=\" font-family:'\u5b8b"
                        "\u4f53'; font-size:10pt;\">\u5411\u524d\u79fb\u52a8\u4e00\u4e2a\u7535\u6781\uff0c</span><span style=\" font-family:'Times New Roman','serif'; font-size:10pt;\">A=#2\uff0c\u83b7\u53d6\u7b2c\u4e8c\u7ec4\u6570\u636e\uff1b</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:'Times New Roman','serif'; font-size:10pt;\">\u4ee5\u6b64\u7c7b\u63a8</span></p></body></html>", None))
        self.extraTopLabel2.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.extraCloseBtn2.setText("")
        self.btn_elcCal.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u6001\u5173\u952e\u6307\u6807\u8ba1\u7b97", None))
        self.btn_geoCal.setText(QCoreApplication.translate("MainWindow", u"\u9759\u6001\u8bc4\u4ef7\u6307\u6807\u8ba1\u7b97", None))
        self.btn_weight.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u4ef7\u6307\u6807\u6743\u91cd\u8ba1\u7b97", None))
        self.btn_FinalIndex.setText(QCoreApplication.translate("MainWindow", u"\u6cb9\u578b\u6c14\u6d8c\u51fa\u5371\u9669\u6027\n\u7efc\u5408\u7b49\u7ea7\u5224\u8bc6", None))
        self.extraTopLabel3.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.extraCloseBtn3.setText("")
        self.btn_res.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u7ed3\u679c\u4fdd\u5b58", None))
        self.btn_img.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u89c6\u5316\u56fe\u50cf\u4fdd\u5b58", None))
        self.minBtn.setText("")
        self.maxBtn.setText("")
        self.exitBtn.setText("")
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))

        self.layer.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u5ca9\u5c42\u6570", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"\u7164\u5c42\u53c2\u6570\u8bbe\u7f6e", None))
        self.depth.setText(QCoreApplication.translate("MainWindow", u"\u57cb\u6df1/m", None))
        self.phi.setText(QCoreApplication.translate("MainWindow", u"\u7164\u5c42\u5185\u6469\u64e6\u89d2/\u00b0", None))
        self.Cm_col.setText(QCoreApplication.translate("MainWindow", u"\u7164\u5c42\u5185\u805a\u529b/MPa", None))
        self.stress.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u529b\u96c6\u4e2d\u7cfb\u6570(1\uff5e5)", None))
        self.coal_thick.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u539a/m", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5ca9\u5c42\u53c2\u6570\u8bbe\u7f6e", None))
        self.extension.setText(QCoreApplication.translate("MainWindow", u"\u6297\u62c9\u5f3a\u5ea6/MPa", None))
        self.permeability.setText(QCoreApplication.translate("MainWindow", u"\u6e17\u900f\u7387/mD", None))
        self.h.setText(QCoreApplication.translate("MainWindow", u"\u5c42\u539a/m", None))
        self.G.setText(QCoreApplication.translate("MainWindow", u"\u5f39\u6027\u6a21\u91cf/GPa", None))
        self.bd.setText(QCoreApplication.translate("MainWindow", u"\u5bb9\u91cd/KN/m\u00b3", None))
        self.cohesion.setText(QCoreApplication.translate("MainWindow", u"\u5185\u805a\u529b/MPa", None))
        self.angle.setText(QCoreApplication.translate("MainWindow", u"\u5185\u6469\u64e6\u89d2/\u00b0", None))
        self.geo_input.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.geo_add.setText(QCoreApplication.translate("MainWindow", u"\u5355\u5c42\u6dfb\u52a0", None))
        self.geo_del.setText(QCoreApplication.translate("MainWindow", u"\u5355\u5c42\u5220\u9664", None))
        self.geo_clear.setText(QCoreApplication.translate("MainWindow", u"\u5168\u4f53\u6e05\u9664", None))
        self.geo_output.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.layer1.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u672a\u9009\u5b9a\u5ca9\u5c42", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5ca9\u6027", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5bb9\u91cd/KN/m\u00b3", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5c42\u539a/m", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u5f39\u6027\u6a21\u91cf/Gpa", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5185\u805a\u529b/Mpa", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u6297\u62c9\u5f3a\u5ea6/Mpa", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u5185\u6469\u64e6\u89d2/\u00b0", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u6e17\u900f\u7387/mD", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"12", None));
        self.contour_label.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u677f\u7535\u963b\u7387\u63a2\u6d4b\u5206\u5e03\u56fe", None))
        self.curve_label.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u677f\u7535\u963b\u7387\u5206\u5e03\u66f2\u7ebf\u53d8\u5316\u56fe", None))
        self.groupBox_d.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u9762\u677f", None))
        self.destroy_btn.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u7834\u574f\u6df1\u5ea6", None))
        self.coal_title.setText(QCoreApplication.translate("MainWindow", u"\u2b07\u2b07\u91c7\u9762\u7164\u5c42\u76f8\u5173\u7cfb\u6570\u2b07\u2b07", None))
        self.coal_thick_d.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u539a/m", None))
        self.coal_thick__d_value.setText("")
        self.depth_d.setText(QCoreApplication.translate("MainWindow", u"\u57cb\u6df1/m", None))
        self.depth_d_value.setText("")
        self.stress_d.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u529b\u96c6\u4e2d\u7cfb\u6570(1\uff5e5)", None))
        self.stress_d_value.setText("")
        self.Cm_col_d.setText(QCoreApplication.translate("MainWindow", u"\u7164\u5c42\u5185\u805a\u529b/MPa", None))
        self.Cm_col_d_value.setText("")
        self.phi_d.setText(QCoreApplication.translate("MainWindow", u"\u7164\u5c42\u5185\u6469\u64e6\u89d2/\u00b0", None))
        self.phi_d_value.setText("")
        self.groupBox_d_show.setTitle(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u9762\u677f", None))
        ___qtablewidgetitem20 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u6cb9\u578b\u6c14\u6d8c\u51fa\u5371\u9669\u6027\u8bc4\u4ef7\u6307\u6807", None));
        ___qtablewidgetitem21 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u4ef7\u6307\u6807\u503c", None));
        ___qtablewidgetitem22 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u52a8\u7a0b\u5ea6C1", None));
        ___qtablewidgetitem23 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u79bb\u6563\u7a0b\u5ea6C2", None));
        ___qtablewidgetitem24 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u677f\u5ca9\u5c42\u6e17\u900f\u7387C3", None));
        ___qtablewidgetitem25 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u677f\u542b\u6cb9\u5f3a\u5ea6C4", None));
        ___qtablewidgetitem26 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u76d6\u5c42\u539a\u5ea6C5", None));
        ___qtablewidgetitem27 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u677f\u542b\u6cb9\u5f3a\u5ea6C6", None));
        ___qtablewidgetitem28 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u65ad\u5c42\u6784\u9020C7", None));
        ___qtablewidgetitem29 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u8936\u76b1\u6784\u9020C8", None));
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem30 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u52a8\u7a0b\u5ea6C1", None));
        ___qtablewidgetitem31 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u79bb\u6563\u7a0b\u5ea6C2", None));
        ___qtablewidgetitem32 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u677f\u5ca9\u5c42\u6e17\u900f\u7387C3", None));
        ___qtablewidgetitem33 = self.tableWidget_2.item(3, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u677f\u542b\u6cb9\u5f3a\u5ea6C4", None));
        ___qtablewidgetitem34 = self.tableWidget_2.item(4, 0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u76d6\u5c42\u539a\u5ea6C5", None));
        ___qtablewidgetitem35 = self.tableWidget_2.item(5, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u677f\u8ba1\u7b97\u7834\u574f\u6df1\u5ea6C6", None));
        ___qtablewidgetitem36 = self.tableWidget_2.item(6, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u65ad\u5c42\u6784\u9020C7", None));
        ___qtablewidgetitem37 = self.tableWidget_2.item(7, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u8936\u76b1\u6784\u9020C8", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.btn_data.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u5224\u65ad\u77e9\u9635\u6570\u636e", None))
        self.btn_weight_ahp.setText(QCoreApplication.translate("MainWindow", u"\u6743\u91cd\u8ba1\u7b97", None))
        self.btn_weight_change.setText(QCoreApplication.translate("MainWindow", u"\u6743\u91cd\u4f18\u5316", None))
        self.level1.setTitle(QCoreApplication.translate("MainWindow", u"\u4e00\u7ea7\u6307\u6807\u77e9\u9635", None))
        ___qtablewidgetitem38 = self.tableWidget_level1.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"B1", None));
        ___qtablewidgetitem39 = self.tableWidget_level1.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"B2", None));
        ___qtablewidgetitem40 = self.tableWidget_level1.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"B3", None));
        ___qtablewidgetitem41 = self.tableWidget_level1.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"B4", None));
        ___qtablewidgetitem42 = self.tableWidget_level1.verticalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"B1", None));
        ___qtablewidgetitem43 = self.tableWidget_level1.verticalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"B2", None));
        ___qtablewidgetitem44 = self.tableWidget_level1.verticalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"B3", None));
        ___qtablewidgetitem45 = self.tableWidget_level1.verticalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"B4", None));

        __sortingEnabled1 = self.tableWidget_level1.isSortingEnabled()
        self.tableWidget_level1.setSortingEnabled(False)
        self.tableWidget_level1.setSortingEnabled(__sortingEnabled1)

        self.plain_matrix.setPlainText(QCoreApplication.translate("MainWindow", u"\u5224\u65ad\u77e9\u9635\u8ba1\u7b97\u62a5\u544a\n"
"", None))
        self.level2.setTitle(QCoreApplication.translate("MainWindow", u"\u4e8c\u7ea7\u6307\u6807\u77e9\u9635", None))
        ___qtablewidgetitem46 = self.tableWidget_21.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"C1", None));
        ___qtablewidgetitem47 = self.tableWidget_21.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"C2", None));
        ___qtablewidgetitem48 = self.tableWidget_21.verticalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"C1", None));
        ___qtablewidgetitem49 = self.tableWidget_21.verticalHeaderItem(1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"C2", None));

        __sortingEnabled2 = self.tableWidget_21.isSortingEnabled()
        self.tableWidget_21.setSortingEnabled(False)
        self.tableWidget_21.setSortingEnabled(__sortingEnabled2)

        ___qtablewidgetitem50 = self.tableWidget_22.horizontalHeaderItem(0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"C3", None));
        ___qtablewidgetitem51 = self.tableWidget_22.horizontalHeaderItem(1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"C4", None));
        ___qtablewidgetitem52 = self.tableWidget_22.verticalHeaderItem(0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"C3", None));
        ___qtablewidgetitem53 = self.tableWidget_22.verticalHeaderItem(1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"C4", None));

        __sortingEnabled3 = self.tableWidget_22.isSortingEnabled()
        self.tableWidget_22.setSortingEnabled(False)
        self.tableWidget_22.setSortingEnabled(__sortingEnabled3)

        ___qtablewidgetitem54 = self.tableWidget_24.horizontalHeaderItem(0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"C7", None));
        ___qtablewidgetitem55 = self.tableWidget_24.horizontalHeaderItem(1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"C8", None));
        ___qtablewidgetitem56 = self.tableWidget_24.verticalHeaderItem(0)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"C7", None));
        ___qtablewidgetitem57 = self.tableWidget_24.verticalHeaderItem(1)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"C8", None));

        __sortingEnabled4 = self.tableWidget_24.isSortingEnabled()
        self.tableWidget_24.setSortingEnabled(False)
        self.tableWidget_24.setSortingEnabled(__sortingEnabled4)

        ___qtablewidgetitem58 = self.tableWidget_23.horizontalHeaderItem(0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"C5", None));
        ___qtablewidgetitem59 = self.tableWidget_23.horizontalHeaderItem(1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"C6", None));
        ___qtablewidgetitem60 = self.tableWidget_23.verticalHeaderItem(0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"C5", None));
        ___qtablewidgetitem61 = self.tableWidget_23.verticalHeaderItem(1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"C6", None));

        __sortingEnabled5 = self.tableWidget_23.isSortingEnabled()
        self.tableWidget_23.setSortingEnabled(False)
        self.tableWidget_23.setSortingEnabled(__sortingEnabled5)

        self.btn_single.setText(QCoreApplication.translate("MainWindow", u"\u5355\u6307\u6807\u5c5e\u6027\u6d4b\u5ea6\n"
"\u8ba1\u7b97", None))
        self.btn_final.setText(QCoreApplication.translate("MainWindow", u"\u6cb9\u578b\u6c14\u6d8c\u51fa\n"
"\u5371\u9669\u6027\u5206\u7ea7", None))

        self.level_risk.setTitle(QCoreApplication.translate("MainWindow", u"\u98ce\u9669\u6307\u6807\u5b9a\u91cf\u5206\u7ea7", None))
        ___qtablewidgetitem62 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"\u2160", None));
        ___qtablewidgetitem63 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"\u2161", None));
        ___qtablewidgetitem64 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"\u2162", None));
        ___qtablewidgetitem65 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"\u2163", None));
        ___qtablewidgetitem66 = self.tableWidget_4.verticalHeaderItem(0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u52a8\u7a0b\u5ea6", None));
        ___qtablewidgetitem67 = self.tableWidget_4.verticalHeaderItem(1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"\u79bb\u6563\u7a0b\u5ea6", None));
        ___qtablewidgetitem68 = self.tableWidget_4.verticalHeaderItem(2)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u677f\u5ca9\u5c42\u6e17\u900f\u7387/mD", None));
        ___qtablewidgetitem69 = self.tableWidget_4.verticalHeaderItem(3)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u677f\u542b\u6cb9\u5f3a\u5ea6", None));
        ___qtablewidgetitem70 = self.tableWidget_4.verticalHeaderItem(4)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"\u76d6\u5c42\u539a\u5ea6/m", None));
        ___qtablewidgetitem71 = self.tableWidget_4.verticalHeaderItem(5)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u677f\u8ba1\u7b97\u7834\u574f\u6df1\u5ea6/m", None));
        ___qtablewidgetitem72 = self.tableWidget_4.verticalHeaderItem(6)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"\u65ad\u5c42\u6784\u9020", None));
        ___qtablewidgetitem73 = self.tableWidget_4.verticalHeaderItem(7)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"\u8936\u76b1\u6784\u9020", None));

        __sortingEnabled6 = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        ___qtablewidgetitem74 = self.tableWidget_4.item(0, 0)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"\uff080\uff0c0.1]", None));
        ___qtablewidgetitem75 = self.tableWidget_4.item(0, 1)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"\uff080.1\uff0c0.4]", None));
        ___qtablewidgetitem76 = self.tableWidget_4.item(0, 2)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"\uff080.5\uff0c0.8]", None));
        ___qtablewidgetitem77 = self.tableWidget_4.item(0, 3)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"\uff080.8\uff0c1]", None));
        ___qtablewidgetitem78 = self.tableWidget_4.item(1, 0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"\uff080\uff0c0.15]", None));
        ___qtablewidgetitem79 = self.tableWidget_4.item(1, 1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"\uff080.15\uff0c0.30]", None));
        ___qtablewidgetitem80 = self.tableWidget_4.item(1, 2)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"\uff080.30\uff0c0.40]", None));
        ___qtablewidgetitem81 = self.tableWidget_4.item(1, 3)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"\uff080.40\uff0c0.50]", None));
        ___qtablewidgetitem82 = self.tableWidget_4.item(2, 0)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"\uff080\uff0c50]", None));
        ___qtablewidgetitem83 = self.tableWidget_4.item(2, 1)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"\uff0850\uff0c100]", None));
        ___qtablewidgetitem84 = self.tableWidget_4.item(2, 2)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"\uff08100\uff0c1000]", None));
        ___qtablewidgetitem85 = self.tableWidget_4.item(2, 3)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"\uff081000\uff0c+\u221e)", None));
        ___qtablewidgetitem86 = self.tableWidget_4.item(5, 0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"\uff080\uff0c5]", None));
        ___qtablewidgetitem87 = self.tableWidget_4.item(5, 1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"\uff085\uff0c8]", None));
        ___qtablewidgetitem88 = self.tableWidget_4.item(5, 2)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"\uff088\uff0c13]", None));
        ___qtablewidgetitem89 = self.tableWidget_4.item(5, 3)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"\uff0813\uff0c+\u221e\uff09", None));
        ___qtablewidgetitem90 = self.tableWidget_4.item(4, 0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"\uff08+\u221e\uff0c20\uff09", None));
        ___qtablewidgetitem91 = self.tableWidget_4.item(4, 1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"[20\uff0c13\uff09", None));
        ___qtablewidgetitem92 = self.tableWidget_4.item(4, 2)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"[13\uff0c9\uff09", None));
        ___qtablewidgetitem93 = self.tableWidget_4.item(4, 3)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"[9\uff0c0)", None));
        ___qtablewidgetitem94 = self.tableWidget_4.item(3, 0)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"\uff080\uff0c25]", None));
        ___qtablewidgetitem95 = self.tableWidget_4.item(3, 1)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"\uff0825\uff0c50]", None));
        ___qtablewidgetitem96 = self.tableWidget_4.item(3, 2)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"\uff0850\uff0c75]", None));
        ___qtablewidgetitem97 = self.tableWidget_4.item(3, 3)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"\uff0875\uff0c100]", None));
        ___qtablewidgetitem98 = self.tableWidget_4.item(6, 0)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"\uff080\uff0c25]", None));
        ___qtablewidgetitem99 = self.tableWidget_4.item(6, 1)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"\uff0825\uff0c50]", None));
        ___qtablewidgetitem100 = self.tableWidget_4.item(6, 2)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"\uff0850\uff0c75]", None));
        ___qtablewidgetitem101 = self.tableWidget_4.item(6, 3)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"\uff0875\uff0c100]", None));
        ___qtablewidgetitem102 = self.tableWidget_4.item(7, 0)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"\uff080\uff0c25]", None));
        ___qtablewidgetitem103 = self.tableWidget_4.item(7, 1)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"\uff0825\uff0c50]", None));
        ___qtablewidgetitem104 = self.tableWidget_4.item(7, 2)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"\uff0850\uff0c75]", None));
        ___qtablewidgetitem105 = self.tableWidget_4.item(7, 3)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"\uff0875\uff0c100]", None));
        self.tableWidget_4.setSortingEnabled(__sortingEnabled6)

        ___qtablewidgetitem106 = self.tableWidget_level1.item(1, 1)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem107 = self.tableWidget_level1.item(2, 2)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem108 = self.tableWidget_level1.item(3, 3)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem109 = self.tableWidget_level1.item(0, 0)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem110 = self.tableWidget_21.item(1, 1)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem111 = self.tableWidget_21.item(0, 0)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem112 = self.tableWidget_22.item(1, 1)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem113 = self.tableWidget_22.item(0, 0)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem114 = self.tableWidget_23.item(1, 1)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem115 = self.tableWidget_23.item(0, 0)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem116 = self.tableWidget_24.item(1, 1)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem117 = self.tableWidget_24.item(0, 0)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"1", None));
        # self.credit_label.setText(QCoreApplication.translate("MainWindow", u"by Kong", None))
    # retranslateUi

