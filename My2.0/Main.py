import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from math import floor, pi
import re
import sys
import xlrd
import xlwt
import matplotlib.pyplot as plt
import pyqtgraph as pg
from fancyimpute import KNN

from matplotlib.figure import Figure
from matplotlib import font_manager
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from modules import *
from widgets import *
from math import sqrt

os.environ["QT_FONT_DPI"] = "96"
font_manager.fontManager.addfont('SourceHanSerifCN-Regular.otf')
plt.rcParams['font.sans-serif'] = 'Source Han Serif CN'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内 

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

        # initial value
        widgets.distanceValue.setText('1.5')
        widgets.spinBox_pole.setValue(48)
        # Action
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

        # extraLeftBox_cal 界面左边弹出界面
        # ---------------------------------
        #-底板岩层电性 关键动态指标elcCal
        widgets.btn_elcCal.clicked.connect(self.btn_click)
        widgets.destroy_btn.clicked.connect(self.btn_click)

        # -底板破坏深度geoCal
        widgets.btn_geoCal.clicked.connect(self.btn_click)

        # -权重计算weight
        widgets.btn_weight.clicked.connect(self.btn_click)
        widgets.btn_data.clicked.connect(self.btn_click)
        widgets.btn_weight_ahp.clicked.connect(self.btn_click)
        widgets.btn_weight_change.clicked.connect(self.btn_click)

        # -油型气涌出危险性分级
        widgets.btn_FinalIndex.clicked.connect(self.btn_click)
        widgets.btn_single.clicked.connect(self.btn_click)
        widgets.btn_final.clicked.connect(self.btn_click)
        # Signal slot
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
            widgets.stackedWidget.setCurrentWidget(widgets.geo) # 切换为地质参数界面
            UIFunctions.selectStyle(self, btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "geo_add":
            # self.row = widgets.tableWidget.currentRow()
            layer = widgets.tableWidget.currentRow()
            λ = widgets.doubleSpinBox_bd.value()
            h = widgets.doubleSpinBox_h.value()
            E = widgets.doubleSpinBox_E.value()
            G = widgets.doubleSpinBox_G.value()
            Cm = widgets.doubleSpinBox_Cm.value()
            phi0 = widgets.doubleSpinBox_phi0.value()
            permeability = widgets.doubleSpinBox_permeability.value()
            item_bd = QTableWidgetItem(str(λ))
            item_h = QTableWidgetItem(str(h))
            item_E = QTableWidgetItem(str(E))
            item_Cm = QTableWidgetItem(str(Cm))
            item_G = QTableWidgetItem(str(G))
            item_phi0 = QTableWidgetItem(str(phi0))
            item_permeability = QTableWidgetItem(str(permeability))
            widgets.tableWidget.setItem(layer, 1, item_bd)
            widgets.tableWidget.setItem(layer, 2, item_h)
            widgets.tableWidget.setItem(layer, 3, item_E)
            widgets.tableWidget.setItem(layer, 4, item_Cm)
            widgets.tableWidget.setItem(layer, 5, item_G)
            widgets.tableWidget.setItem(layer, 6, item_phi0)
            widgets.tableWidget.setItem(layer, 7, item_permeability)
            
        if btnName == "geo_del":
            if widgets.layer1.text() != "当前未选定岩层":
                current_row = widgets.tableWidget.currentRow()
                widgets.tableWidget.removeRow(current_row)
                lithology = QComboBox(widgets.tableWidget)
                lithology.addItems([u"\u6ce5\u5ca9", u"\u9875\u5ca9", u"\u7802\u5ca9"])
                widgets.layer1.setText('当前未选定岩层')
            
        if btnName == "geo_re":

            pass
        if btnName == "geo_clear":
            widgets.tableWidget.clearContents()
            pass
        # ----------------------------------------
        #------------------Calculate--------------------
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
        if btnName == "btn_elcCal":
            widgets.stackedWidget.setCurrentWidget(widgets.elc) 
            self.curve_rho()
            pass

        # 计算破坏深度计算界面
        if btnName == "btn_geoCal":
            widgets.stackedWidget.setCurrentIndex(3)    # !!!按控件名切换 报错  ；使用索引号切换
            widgets.coal_thick__d_value.setText(str(widgets.doubleSpinBox_thick.value()))
            widgets.depth_d_value.setText(str(widgets.doubleSpinBox_depth.value()))
            widgets.stress_d_value.setText(str(widgets.doubleSpinBox_stress.value()))
            widgets.Cm_col_d_value.setText(str(widgets.doubleSpinBox_Cm_col.value()))
            widgets.phi_d_value.setText(str(widgets.doubleSpinBox_phi.value()))
        if btnName == 'destroy_btn':
            try:        
                Ratio_constant = (10/4)**5
                Amplitude_constant = (5/3)**2
                m = widgets.doubleSpinBox_thick.value()    # 采厚
                H = widgets.doubleSpinBox_depth.value()    # 埋深
                phi = widgets.doubleSpinBox_phi.value()    # 内摩擦角  
                Cm = widgets.doubleSpinBox_Cm_col.value()  # 煤层内聚力
                n = widgets.doubleSpinBox_stress.value()   # 应力集中系数
                phi0 = phi*np.pi/180    #煤层内摩擦角
                gama_list = []
                phiR_list = []
                layer_list = []
                E_list = []
                Cm_rock_list = []
                G_list = []
                for row in range(widgets.tableWidget.rowCount()):
                    gama_list.append(float(widgets.tableWidget.item(row, 1).text()))
                    layer_list.append(float(widgets.tableWidget.item(row, 2).text()))
                    E_list.append(float(widgets.tableWidget.item(row, 3).text()))
                    Cm_rock_list.append(float(widgets.tableWidget.item(row, 4).text()))
                    G_list.append(float(widgets.tableWidget.item(row, 5).text()))
                    phiR_list.append(float(widgets.tableWidget.item(row, 6).text()))
                gama_list = np.array(gama_list)
                layer_list = np.array(layer_list)
                E_list = np.array(E_list)
                Cm_rock_list = np.array(Cm_rock_list)
                G_list = np.array(G_list)
                phi1_list = np.array(phiR_list)

                gama = sum(gama_list*layer_list/sum(layer_list))    # 容重
                E = sum(E_list*layer_list/sum(layer_list))  # 弹性模量
                Cm_rock = sum(Cm_rock_list*layer_list/sum(layer_list))  #内聚力 
                G = sum(G_list*layer_list/sum(layer_list))  # 抗拉强度
                phi1 = sum(phi1_list*layer_list/sum(layer_list))    # 岩层内摩擦角

                phi1 = phi1*np.pi/180
                K1 = (1+np.sin(phi1))/(1-np.sin(phi1))
                F = (K1 - 1)/sqrt(K1) + ((K1 - 1)/sqrt(K1))**2 * np.arctan(sqrt(K1))
                x_alpha = m/(2*K1*np.tan(phi1))*np.log((n*gama*H+Cm*np.tan(phi1)**-1)/(K1*Cm*np.tan(phi1)**-1))  # A.H.Wilson 曲屈服区长度计算
                e1 = x_alpha*np.cos(phi0)/(2*np.cos(np.pi/4+phi0/2))
                e2 = np.e**((np.pi/4 + phi0/2)* np.tan(phi0))
                result = e1 * e2
                h = result*(10/E)**0.5*(4/Cm_rock)**0.3*(5/G)**0.2
                h = round(h, 2)
                item_destroy_depth = QTableWidgetItem(str(h))
                widgets.tableWidget_2.setItem(3, 1, item_destroy_depth)
                widgets.textBrowser.append("计算破坏深度：{}m".format(h))
            except Exception as e:
                widgets.textBrowser.append(str(e))
                widgets.textBrowser.append("岩层参数设置不完全")

        # 权重计算界面
        if btnName == "btn_weight":
            widgets.stackedWidget.setCurrentWidget(widgets.AHP) 
        if btnName == "btn_data":
            
            pass
        if btnName == "btn_weight_ahp":
            # 一级指标
            order = widgets.tableWidget_level1.rowCount()
            A1 = [[] for i in range(order)]
            for row in range(order):
                for col in range(order):
                    # 需要添加一个数值判断语句
                    A1[row].append(float(widgets.tableWidget_level1.item(row, col).text()))
            widgets.plain_matrix.appendPlainText("--------一级指标判断矩阵---------")
            w1 = self.check(np.array(A1))


            # 二级指标B1
            order = widgets.tableWidget_21.rowCount()
            B1 = [[] for i in range(order)]
            for row in range(order):
                for col in range(order):
                    # 需要添加一个数值判断语句
                    B1[row].append(float(widgets.tableWidget_21.item(row, col).text()))
            n = np.array(B1).shape[0]
            weight1 = (np.sum(B1/(np.sum(B1, axis=0)), axis=1)) / n   # 算数平均权重
            w21 = weight1
            widgets.plain_matrix.appendPlainText("------二级指标判断矩阵B1---------")
            widgets.plain_matrix.appendPlainText("二阶矩阵具备完全一致性")
            widgets.plain_matrix.appendPlainText("权重向量计算得：\n{}".format(weight1))


            # 二级指标B2
            order = widgets.tableWidget_22.rowCount()
            B2 = [[] for i in range(order)]
            for row in range(order):
                for col in range(order):
                    # 需要添加一个数值判断语句
                    B2[row].append(float(widgets.tableWidget_22.item(row, col).text()))
            n = np.array(B2).shape[0]
            weight1 = (np.sum(B2/(np.sum(B2, axis=0)), axis=1)) / n   # 算数平均权重     
            w22 = weight1       
            widgets.plain_matrix.appendPlainText("------二级指标判断矩阵B2---------")
            widgets.plain_matrix.appendPlainText("二阶矩阵具备完全一致性")
            widgets.plain_matrix.appendPlainText("权重向量计算得：\n{}".format(weight1))


            # 二级指标B3
            order = widgets.tableWidget_24.rowCount()
            B3 = [[] for i in range(order)]
            for row in range(order):
                for col in range(order):
                    # 需要添加一个数值判断语句
                    B3[row].append(float(widgets.tableWidget_24.item(row, col).text()))
            n = np.array(B3).shape[0]
            weight1 = (np.sum(B3/(np.sum(B3, axis=0)), axis=1)) / n   # 算数平均权重
            w23 = weight1
            widgets.plain_matrix.appendPlainText("------二级指标判断矩阵B3---------")
            widgets.plain_matrix.appendPlainText("二阶矩阵具备完全一致性")
            widgets.plain_matrix.appendPlainText("权重向量计算得：\n{}".format(weight1))


            # 二级指标B4
            order = widgets.tableWidget_23.rowCount()
            B4 = [[] for i in range(order)]
            for row in range(order):
                for col in range(order):
                    # 需要添加一个数值判断语句
                    B4[row].append(float(widgets.tableWidget_23.item(row, col).text()))
            n = np.array(B4).shape[0]
            weight1 = (np.sum(B4/(np.sum(B4, axis=0)), axis=1)) / n   # 算数平均权重
            w24 = weight1
            widgets.plain_matrix.appendPlainText("------二级指标判断矩阵B4---------")
            widgets.plain_matrix.appendPlainText("二阶矩阵具备完全一致性")
            widgets.plain_matrix.appendPlainText("权重向量计算得：\n{}".format(weight1))

            wb1 = w1[0]*w21
            wb2 = w1[1]*w22
            wb3 = w1[2]*w23
            wb4 = w1[3]*w24
            global w
            w = np.concatenate((wb1, wb2, wb3, wb4))

        if btnName == "btn_weight_change":
            if not p:
                widgets.mat_Edit.setPlainText('存在判断矩阵一致性未通过')
            if p:
                widgets.mat_Edit.setPlainText('''油型气涌出影响因素\n综合权重\n-----------\n波动程度C1：{:.3f}\n离散程度C2：{:.3f}\n底板岩层渗透率C3：{:.3f}\n底板计算破坏深度C4：{:.3f}\n油型气储集层厚度C5：{:.3f}\n底板含油特征C6：{:.3f}\n断层构造C7：{:.3f}\n褶皱构造C8：{:.3f}'''.format(w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7],))
            else:
                widgets.mat_Edit.appendPlainText('something wrong...')
            pass

        # 危险性分级计算界面
        if btnName == "btn_FinalIndex":
            widgets.stackedWidget.setCurrentIndex(5)    #为什么不用控件名，理由如第三页面相同
        if btnName == "btn_single":
            data_c1 = [0, 0.2, 0.5, 0.8, 1]
            data_c2 = [0, 0.15, 0.3, 0.4, 0.5]
            data_c3 = [0, 50, 100, 1000, 1200]
            data_c4 = [0, 10, 20, 30, 40]
            data_c5 = [0, 3, 7, 10, 13]
            data_c6 = [0, 25, 50, 75, 100]
            data_c7 = [0, 25, 50, 75, 100]
            data_c8 = [0, 25, 50, 75, 100]
            data = [data_c1, data_c2, data_c3, data_c4, data_c5, data_c6, data_c7, data_c8]
            m_value = [[] for _ in range(8)]
            for i in range(8):
                m_value[i] = self.measure(float(widgets.tableWidget_2.item(i, 1).text()), data[i])
            print(m_value)
            widgets.plainTextEdit.appendPlainText('----------------------------------单指标属性测度评价----------------------------------')
            widgets.plainTextEdit.appendPlainText('            c1           c2           c3           c4           c5           c6           c7           c8')
            widgets.plainTextEdit.appendPlainText('Ⅰ       {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}'.format(m_value[0][0], m_value[1][0], m_value[2][0], m_value[3][0], m_value[4][0], m_value[5][0], m_value[6][0], m_value[7][0]))
            widgets.plainTextEdit.appendPlainText('Ⅱ       {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}'.format(m_value[0][1], m_value[1][1], m_value[2][1], m_value[3][1], m_value[4][1], m_value[5][1], m_value[6][1], m_value[7][1]))
            widgets.plainTextEdit.appendPlainText('Ⅲ       {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}'.format(m_value[0][2], m_value[1][2], m_value[2][2], m_value[3][2], m_value[4][2], m_value[5][2], m_value[6][2], m_value[7][2]))
            widgets.plainTextEdit.appendPlainText('Ⅳ       {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}      {:.3f}'.format(m_value[0][3], m_value[1][3], m_value[2][3], m_value[3][3], m_value[4][3], m_value[5][3], m_value[6][3], m_value[7][3]))
            widgets.plainTextEdit.appendPlainText('-----------------------------------------------------------------------------------------')
            m1 = [m_value[0][0], m_value[1][0], m_value[2][0], m_value[3][0], m_value[4][0], m_value[5][0], m_value[6][0], m_value[7][0]]
            m2 = [m_value[0][1], m_value[1][1], m_value[2][1], m_value[3][1], m_value[4][1], m_value[5][1], m_value[6][1], m_value[7][1]]
            m3 = [m_value[0][2], m_value[1][2], m_value[2][2], m_value[3][2], m_value[4][2], m_value[5][2], m_value[6][2], m_value[7][2]]
            m4 = [m_value[0][3], m_value[1][3], m_value[2][3], m_value[3][3], m_value[4][3], m_value[5][3], m_value[6][3], m_value[7][3]]
            widgets.plainTextEdit.appendPlainText('-----------------------------------综合属性测度评价-----------------------------------')
            widgets.plainTextEdit.appendPlainText('                    Ⅰ                    Ⅱ                    Ⅲ                    Ⅳ')
            widgets.plainTextEdit.appendPlainText('                  {:.3f}               {:.3f}               {:.3f}               {:.3f}'.format(sum(w*np.array(m1)), sum(w*np.array(m2)), sum(w*np.array(m3)), sum(w*np.array(m4))))
            d = {'Ⅰ':sum(w*np.array(m1)), 'Ⅱ':sum(w*np.array(m2)), 'Ⅲ':sum(w*np.array(m3)), 'Ⅳ':sum(w*np.array(m4))}
            class_d = {'Ⅰ':'巷道底板稳定，油型气涌出危险性低。', 'Ⅱ':'巷道底板较稳定，油型气涌出危险性较低。', 'Ⅲ':'巷道底板不稳定，可能存在断层等地质构造，油型气涌出危险性高。', 'Ⅳ':'巷道底板极度不稳定，可能存在大尺度断层构造，油型气涌出危险性高。'}
            key_of_max = max(d, key=lambda k: d[k])
            widgets.plainTextEdit.appendPlainText('本次油型气涌出危险性等级评估为 {} 级， {}'.format(key_of_max, class_d[key_of_max]))
        if btnName == "btn_final":
            
            pass
            
        #---------------------------------------------
        #------------------File--------------------
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

        #---------------------------------------------
        print(f'Button "{btnName}" Pressed!')
    # Signal send and recieve
    def send_row_sig(self):
        current_row = widgets.tableWidget.currentRow()
        self.row_signal.emit(current_row)
    def get_row_sig(self, current_row):
        widgets.layer1.setText('当前选定第{}层'.format(current_row+1))


    # Weight
    def check(self, A):
        eigen_value = np.linalg.eig(A)[0] # 特征值与特征向量
        global p
        p = False
        n = A.shape[0]
        CI = (max(eigen_value) - n)/(n - 1)
        RI = [0, 0, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54]
        CR = CI/RI[n-1]
        n = A.shape[0]
        weight1 = (np.sum(A/(np.sum(A, axis=0)), axis=1)) / n   # 算数平均权重
        weight2 = pow(np.prod(A, axis=1), 1/n) / np.sum(pow(np.prod(A, axis=1), 1/n))   #几何平均权重
        # 特征值求权重
        eigen, vector = np.linalg.eig(A)
        for i in range(n):
            if eigen[i] == np.max(eigen):
                index_eigen = i
        e_vector = vector[:, index_eigen]
        weight3 = e_vector/np.sum(e_vector)
        if CR < 0.1: p = True
        if p:
            str_p = '一致性检验通过'
            widgets.plain_matrix.appendPlainText('''权重向量计算得：\n{}\n一致性指标值C.I.为{:.3f}\n一致性比率值C.R.为{:.3f}\n{}！最大特征值λmax为{:.3f}\n--------------------------------'''.format(weight2, CI, CR, str_p, max(eigen_value)))
            return weight2
        else:
            str_p = '一致性检验未通过'
            widgets.plain_matrix.appendPlainText('''权重向量计算得：\n{}\n一致性指标值C.I.为{:.3f}\n一致性比率值C.R.为{:.3f}\n{}！需要重新调整判断矩阵\n--------------------------------'''.format(weight3, CI, CR, str_p))

    # Evaluation
    def measure(self, x, data):
        # numbers = re.findall(r'\d+', text) 正则匹配表格中的测度范围
        m_value = []
        for i in range(len(data)-1):
            def f_0(x, i):
                k = i+1
                a = data[k-1]
                ai = data[k]
                aii = data[k+1]
                bi = (a+ai)/2
                bii = (ai+aii)/2
                di = min(abs(bii-ai), abs(bi-ai))
                if x<ai-di:
                    return 1
                elif ai-di<=x<=ai+di:
                    return (ai+di-x)/(2*di)
                elif x>ai+di:
                    return 0
            def f_k(x, i):
                k = i+1
                ia = data[k-2]
                a = data[k-1]
                ai = data[k]
                aii = data[k+1]

                b = (ia+a)/2
                bi = (a+ai)/2
                bii = (ai+aii)/2

                d = min(abs(bi-a), abs(b-a))
                di = min(abs(bii-ai), abs(bi-ai))
                if x<a-d:
                    return 0
                elif a-d<=x<=a+d:
                    return (x-a+d)/(2*d)
                elif a+d<x<ai-di:
                    return 1
                elif ai-di<=x<=ai+di:
                    return (ai+di-x)/(2*di)
                elif x>ai+di:
                    return 0       
            def f_m(x, i):
                k = i+1
                ia = data[k-2]
                a = data[k-1]
                ai = data[k]


                b = (ia+a)/2
                bi = (a+ai)/2


                d = min(abs(bi-a), abs(b-a))
                if x<a-d:
                    return 0
                elif a-d<=x<=a+d:
                    return (x-a+d)/(2*d)
                elif a+d<x:
                    return 1
                
            if i == 0:
                m_value.append(f_0(x, i))

            elif i == range(len(data))[-2]:
                m_value.append(f_m(x, i))
            else:
                m_value.append(f_k(x, i))
        return m_value

    def curve_rho(self): # 曲线图
        if self.filename == None:
            QMessageBox.warning(window.pushButton, "警告", "未选择数据文件!", QMessageBox.Yes)
            return 
        data = main(self.filename)
        data = data.iloc[:21, :101]
        # data.to_csv('resistivity.csv')
        data1 = data.sum(axis=0)/len(data.index)
        m_line = np.mean(data1)
        # data1.to_csv('1.csv')
        reg = np.polyfit(data1.index, data1.values, 8)
        y = np.polyval(reg, data1.index)
        self.fig = fig_curve(width=widgets.curve_rho.width()/101, height=widgets.curve_rho.height()/81, )
        self.fig.axes.set_xlabel('测点前方距离/m', labelpad=0.1, fontdict={"size":14, 'family':'Source Han Serif CN'})
        self.fig.axes.set_ylabel('底板平均电阻率/(Ω·m)', fontdict={"size":14, 'family':'Source Han Serif CN'})
        self.fig.axes.tick_params(labelsize=16)
        self.fig.axes.axhline(m_line, linestyle='--', c='orange', label='均值线')
        self.fig.axes.plot(data1, label='源数据')
        self.fig.axes.plot(data1.index, y, color='r', label='拟合数据')
        self.fig.axes.set_xticks([x for x in range(0, 100, 10)])
        self.fig.axes.legend(loc=0, prop={"size":14})
        self.fig.tight()
        # self.fig.save()
        self.scene = QGraphicsScene()
        self.scene.addWidget(self.fig)
        widgets.curve_rho.setScene(self.scene)
        widgets.curve_rho.show()
        pass

    # Extra Menu
    def calmenuShow(self):
        
        calMenu = QMenu(widgets.page_container)

        rawData = QWidgetAction(calMenu)
        rawData_btn = QPushButton("岩层电阻率数据导出")
        rawData.setDefaultWidget(rawData_btn)

        calResult = QWidgetAction(calMenu)
        calResult_btn = QPushButton("各参数指标及权重导出")
        calResult.setDefaultWidget(calResult_btn)

        calMenu.addActions([rawData, calResult, ])
        rawData_btn.clicked.connect(self.data_save)
        print(self.mapToParent(widgets.BotContent.pos()))
        
        x_pos = widgets.leftMenu.width()+widgets.extraLeftBox.width()+9
        y_pos = widgets.TopLogo.height()+12
        calMenu.exec(self.mapToParent(QPoint(x_pos, y_pos)))    # mapToParent 相对位置与绝对位置
    def imgmenuShow(self):
        imgMenu = QMenu(widgets.page_container)

        img1= QWidgetAction(imgMenu)
        img1_btn = QPushButton("岩层电阻率数据导出")
        img1.setDefaultWidget(img1_btn)

        img2 = QWidgetAction(imgMenu)
        img2_btn = QPushButton("各参数指标及权重导出")
        img2.setDefaultWidget(img2_btn)

        imgMenu.addActions([img1, img2])
        print(self.mapToParent(widgets.BotContent.pos()))
        x_pos = widgets.leftMenu.width()+widgets.extraLeftBox.width()+9
        y_pos = widgets.TopLogo.height()+widgets.btn_img.height()+12
        imgMenu.exec(self.mapToParent(QPoint(x_pos, y_pos))) 
        pass
    def ChangePol_d(self):
        value = widgets.horizontalSlider.value()
        widgets.distanceValue.setText(str(value*0.5))

    # Action trigger
    def data_save(self):
        
        print('save success')
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

# Figure
class fig_curve(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)
        self.axes = self.fig.add_subplot(111)
    def tight(self):
        self.fig.tight_layout()
    def save(self):
        self.fig.savefig('1.png')

# Algorithm
def mul(df1, df2):
    l1 = df1.values.tolist()
    l2 = df2.values.tolist()
    l3 = np.multiply(l1, l2)
    return DataFrame(l3)

def rho_3(n, filename, a=1.5, reverse=True):
    # 
    dataset = pd.read_csv(filename, encoding='gb2312')
    dataset.dropna(axis=1, inplace=True)
    col = []
    for i in dataset.columns:
        col.append(i[:-3])
    dataset.columns = col
    if not reverse:
        dataset = dataset[0:n]  # Take the first three rows
        ampere = dataset.电流[:n]
        dataset.drop(columns=['电流'], inplace=True)
    elif reverse:
        dataset = dataset[-n:][::-1]  # Take the last three rows
        ampere = dataset.电流
        dataset.drop(columns=['电流'], inplace=True)
        for i in range(len(dataset.index)):
            dataset.iloc[i] = dataset.iloc[i][::-1]

    # rho_s  ------------------------
    data_r = DataFrame(np.zeros((n, 46)))
    for row in range(len(dataset.index)):
        for col in range(row + 1, len(dataset.columns)):
            cat = []
            m = col
            n = col + 1
            while (n - m) <= (m - row) and n <= 47:
                cat.append((row, m, n))
                m -= 1
                n += 1
            if cat != []:
                dog = 0  # Apprent resistivity
                f = 0  # Weight factor: f
                for i in cat:
                    fi = 3 / (4 * pi * (((i[2] - i[0]) * a) ** 3 - (
                                (i[1] - i[0]) * a) ** 3))  # Weight factor f = 3/(4*pi*(AN ** 3 - AM ** 3))
                    ki = 2 * pi * (i[1] - i[0]) * (i[2] - i[0]) * a / (
                                i[2] - i[1])  # Coefficient k = 2*pi*|AM|*|AN|/|MN|
                    dog += fi * ki * (dataset.iloc[i[0]][i[1]] - dataset.iloc[i[0]][i[2]]) / ampere.iloc[
                        i[0]]  # ∑(ai * ki * delta_Ui/I) / ∑ai
                    f += fi
                data_r.iloc [row][col - 1] = dog / f
                # ------------------------------
    # data_r.to_csv('d:/kong/aaa_/3ar.csv', encoding='gb2312')
    return data_r

def Ef(A, M, N, rho, mesh, delta_x=0.25,):
    L_AO = M + (N - M) / 2 - A
    y = lambda x: (L_AO ** 2 - (x + A) ** 2) ** 0.5  # Curve of resident
    y_ = lambda x: (L_AO ** 2 - x ** 2) ** 0.5 - A
    d = L_AO - A  # forward detection distance
    if d > 0:
        t_x = [i for i in np.arange(0, y_(0) + 0.001, delta_x)]  # 0.001 is aimed to get the boundary point
        t_y = [i for i in np.arange(0, y(0) + 0.001, delta_x)]  # Coordinate
        # cross_point(y, y_, t_x, t_y):
        p1 = np.array(list(map(y, t_x))) / delta_x  # cross with axis x
        p2 = np.array(list(map(y_, t_y))) / delta_x  # cross with axis y
        for column, row in enumerate(p1):  # Assignment through point1
            if row != int(row):
                row = floor(row)
                if column == 0:
                    mesh[row][column].append(rho)
                elif column != 0:
                    mesh[row][column].append(rho)
                    mesh[row][column - 1].append(rho)
            elif row == int(row):  # int part
                r_int = int(row)
                if r_int == 0:
                    mesh[r_int][column].append(rho)
                    mesh[r_int][column - 1].append(rho)
                else:
                    if column != 0:
                        mesh[r_int - 1][column - 1].append(rho)
                        mesh[r_int][column - 1].append(rho)
                    mesh[r_int][column].append(rho)
                    mesh[r_int - 1][column].append(rho)
                    
        for row, column in enumerate(p2):  # Assignment through point2
            if column == int(column):  # int part
                column_int = int(column)
                if row == 0:
                    mesh[row][column_int].append(rho)
                    mesh[row][column_int - 1].append(rho)
                else:
                    if column_int != 0:
                        mesh[row][column_int - 1].append(rho)
                        mesh[row - 1][column_int - 1].append(rho)
                    mesh[row][column_int].append(rho)
                    mesh[row - 1][column_int].append(rho)
                    
            elif column != int(column):  # nonint part
                column_f = floor(column)
                mesh[row][column_f].append(rho)
                mesh[row - 1][column_f].append(rho)
    else:
        pass

def main(filename):
    # Grid and assignment
    mesh = DataFrame([[[0]] * 200] * 200)
    for row in range(len(mesh.index)):
        for col in range(len(mesh.columns)):
            mesh[row][col] = [0]
    mesh = mesh.to_numpy()
    n = 6
    reverse = True
    rho_s = rho_3(n=n, filename=filename, reverse=reverse)
    #rho_ss = rho_2(n=n, a=space, reverse=reverse)
    for A in rho_s.index:
        for M in range(A, len(rho_s.columns) - 1):
            Ef(A, M + 1, M + 2, rho_s.iloc[A][M], mesh=mesh)  # rho_3
            #Ef(A, M, M + 2, rho_ss.iloc[A][M])  # rho_2
    mesh = DataFrame(mesh)
    result = mesh.applymap(lambda x: sum(list(set(x))) / (len(list(set(x))) - 1) if x != [0] else np.nan)
    result.dropna(axis=1, how='all', inplace=True)
    result.dropna(axis=0, how='all', inplace=True)
    result = DataFrame(KNN(k=6).fit_transform(result))
    result.to_csv('result.csv')
    # if not reverse:
    #     mesh.to_csv('d:/past_dealer/forward/meshf{}.csv'.format(len(rho_s.index)), encoding='gb2312')  # Unprocessed grid data
    #     result.to_csv('d:/past_dealer/forward/resultf{}.csv'.format(len(rho_s.index)), encoding='gb2312')  # Grid data processed by mean
    # elif reverse:
    #     mesh.to_csv('d:/past_dealer/backward/meshb{}.csv'.format(len(rho_s.index)), encoding='gb2312')  # Unprocessed grid data
    #     result.to_csv('d:/past_dealer/backward/resultb{}.csv'.format(len(rho_s.index)), encoding='gb2312')  # Grid data processed by mean
    return result
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.setFixedSize(window.width(),window.height())   # 限定窗口大小
    window.show()
    sys.exit(app.exec())
