import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" 

class MainWindow(QMainWindow):
    File_signal = Signal(str)   # 发送信号
    general_para = Signal(int, int)
    row_signal = Signal(int) 
    table_signal = Signal(str)
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        title = 'GUI'
        self.setWindowTitle(title) 
        UIFunctions.uiDefinitions(self)


        widgets.btn_res.clicked.connect(self.calmenuShow)
        widgets.btn_img.clicked.connect(self.imgmenuShow)
        # Extra leftBox
        def openCLoseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        # widgets.bottomButton.clicked.connect(openCLoseLeftBox)
        widgets.extraCloseBtn.clicked.connect(openCLoseLeftBox)
        widgets.extraCloseBtn2.clicked.connect(openCLoseLeftBox)
        widgets.extraCloseBtn3.clicked.connect(openCLoseLeftBox)
            
        # leftMenu
        widgets.toggleButton.clicked.connect(lambda:UIFunctions.toggleMenu(self, True))
        widgets.home_btn.clicked.connect(self.btn_click)
        widgets.Elc_btn.clicked.connect(self.btn_click)
        widgets.Geo_btn.clicked.connect(self.btn_click)
        widgets.Cal_btn.clicked.connect(self.btn_click)
        widgets.Save_btn.clicked.connect(self.btn_click)


        # Set home page
        widgets.stackedWidget.setCurrentWidget(widgets.home)

        # Elc page
        widgets.file_open.clicked.connect(self.btn_click)   
        widgets.horizontalSlider.valueChanged.connect(self.ChangePol_d) # QSlider 响应事件
        # Geo page
        widgets.geo_add.clicked.connect(self.btn_click)
        widgets.geo_del.clicked.connect(self.btn_click)
        # widgets.geo_re.clicked.connect(self.btn_click)
        widgets.geo_clear.clicked.connect(self.btn_click)
            # --Signal slot
        self.row_signal.connect(self.get_row_sig)   # 获取表格的行序号
        widgets.tableWidget.clicked.connect(self.send_row_sig) 

        



    # Buttons Click
    def btn_click(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "home_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.selectStyle(self, btnName)
            pass
        # ---------------------Elc---------------
        if btnName == "Elc_btn":
            print("page{}".format(widgets.extraLeftBox.currentIndex()))
            if widgets.extraLeftBox.width() == Settings.LEFT_BOX_WIDTH and widgets.extraLeftBox.currentIndex()!=0:
                widgets.extraLeftBox.setCurrentIndex(0)
            elif widgets.extraLeftBox.width() == 0 and widgets.extraLeftBox.currentIndex()!=0:
                widgets.extraLeftBox.setCurrentIndex(0)
                UIFunctions.LeftBox(self, True)
            else:
                UIFunctions.LeftBox(self, True)
            UIFunctions.selectStyle(self, btnName)
        if btnName == "file_open":
            #if
            dialog  = QFileDialog()
            # 选择多个文件
            dialog.setFileMode(QFileDialog.ExistingFile)
            path, _ = dialog.getOpenFileName(self, "打开图片", QDir.currentPath(),"数据文件(*.dat);;所有文件(*)", options=QFileDialog.DontUseNativeDialog)
            self.filename = path
            widgets.textBrowser.append('数据导入成功')
        # ----------------------------------------

        #------------------Geo--------------------
        if btnName == "Geo_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.geo)
            UIFunctions.selectStyle(self, btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            pass
        if btnName == "geo_add":
            # self.row = self.ui.tableWidget.currentRow()
            layer = self.ui.tableWidget.currentRow()
            λ = self.ui.doubleSpinBox_bd.value()
            h = self.ui.doubleSpinBox_h.value()
            E = self.ui.doubleSpinBox_E.value()
            G = self.ui.doubleSpinBox_G.value()
            Cm = self.ui.doubleSpinBox_Cm.value()
            phi0 = self.ui.doubleSpinBox_phi0.value()
            permeability = self.ui.doubleSpinBox_permeability.value()
            item_bd = QTableWidgetItem(str(λ))
            item_h = QTableWidgetItem(str(h))
            item_E = QTableWidgetItem(str(E))
            item_Cm = QTableWidgetItem(str(Cm))
            item_G = QTableWidgetItem(str(G))
            item_phi0 = QTableWidgetItem(str(phi0))
            item_permeability = QTableWidgetItem(str(permeability))
            self.ui.tableWidget.setItem(layer, 1, item_bd)
            self.ui.tableWidget.setItem(layer, 2, item_h)
            self.ui.tableWidget.setItem(layer, 3, item_E)
            self.ui.tableWidget.setItem(layer, 4, item_Cm)
            self.ui.tableWidget.setItem(layer, 5, item_G)
            self.ui.tableWidget.setItem(layer, 6, item_phi0)
            self.ui.tableWidget.setItem(layer, 7, item_permeability)
            
        if btnName == "geo_del":
            if self.ui.layer1.text() != "当前未选定岩层":
                current_row = self.ui.tableWidget.currentRow()
                self.ui.tableWidget.removeRow(current_row)
                lithology = QComboBox(self.ui.tableWidget)
                lithology.addItems([u"\u6ce5\u5ca9", u"\u9875\u5ca9", u"\u7802\u5ca9"])
                self.ui.layer1.setText('当前未选定岩层')
            
        if btnName == "geo_re":

            pass
        if btnName == "geo_clear":
            self.ui.tableWidget.clearContents()
            pass
        # ----------------------------------------
        if btnName == "Cal_btn":
            print("page{}".format(widgets.extraLeftBox.currentIndex()))
            if widgets.extraLeftBox.width() == Settings.LEFT_BOX_WIDTH and widgets.extraLeftBox.currentIndex()!=1:
                widgets.extraLeftBox.setCurrentIndex(1)
            elif widgets.extraLeftBox.width() == 0 and widgets.extraLeftBox.currentIndex()!=1:
                widgets.extraLeftBox.setCurrentIndex(1)
                UIFunctions.LeftBox(self, True)
            else:
                UIFunctions.LeftBox(self, True)
            UIFunctions.selectStyle(self, btnName)
        if btnName == "Save_btn":
            print("page{}".format(widgets.extraLeftBox.currentIndex()))
            if widgets.extraLeftBox.width() == Settings.LEFT_BOX_WIDTH and widgets.extraLeftBox.currentIndex()!=2:
                widgets.extraLeftBox.setCurrentIndex(2)
            elif widgets.extraLeftBox.width() == 0 and widgets.extraLeftBox.currentIndex()!=2:
                widgets.extraLeftBox.setCurrentIndex(2)
                UIFunctions.LeftBox(self, True)
            else:
                UIFunctions.LeftBox(self, True)
            UIFunctions.selectStyle(self, btnName)


        print(f'Button "{btnName}" Pressed!')
    # Signal send and recieve
    def send_row_sig(self):
        current_row = self.ui.tableWidget.currentRow()
        self.row_signal.emit(current_row)
    def get_row_sig(self, current_row):
        self.ui.layer1.setText('当前选定第{}层'.format(current_row+1))
    # Extra Menu
    def calmenuShow(self):
        
        calMenu = QMenu(widgets.page_container)
        rawData = QAction("岩层电阻率数据导出", calMenu)

        calResult = QAction("各参数指标及权重导出", calMenu)

        calMenu.addActions([rawData, calResult])
        print(self.mapToParent(widgets.BotContent.pos()))
        x_pos = widgets.leftMenu.width()+widgets.extraLeftBox.width()+9
        y_pos = widgets.TopLogo.height()+12
        calMenu.exec(self.mapToParent(QPoint(x_pos, y_pos)))    # mapToParent 相对位置与绝对位置
    def imgmenuShow(self):
        imgMenu = QMenu(widgets.page_container)
        rawData = QAction("岩层电阻率数据导出", calMenu)

        calResult = QAction("各参数指标及权重导出", calMenu)

        imgMenu.addActions([rawData, calResult])
        print(self.mapToParent(widgets.BotContent.pos()))
        x_pos = widgets.leftMenu.width()+widgets.extraLeftBox.width()+9
        y_pos = widgets.TopLogo.height()+widgets.btn_img.height()+12
        imgMenu.exec(self.mapToParent(QPoint(x_pos, y_pos))) 
        pass
    def ChangePol_d(self):
        value = widgets.horizontalSlider.value()
        widgets.distanceValue.setText(str(value*0.5))
    
    # 跟随尺寸改变
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)
    # 跟随鼠标拖动
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.setFixedSize(window.width(),window.height())   # 限定窗口大小
    window.show()
    sys.exit(app.exec())
