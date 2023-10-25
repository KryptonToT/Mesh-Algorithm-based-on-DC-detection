0# _*_ coding : UTF-8 _*_
# 开发人员： MY
# 开发时间： 2022/2/28  16:58
# 文件名称： 1.py
# 开发工具： PyCharm

import PySide6.QtGui
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from math import floor, pi
import fancyimpute
import re
import sys
import xlrd
import xlwt
import matplotlib.pyplot as plt
import pyqtgraph as pg

from math import sqrt
from pandas import DataFrame, Series
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtUiTools import QUiLoader
from MainWin.MainWin import Ui_MainWindow
from SubWin.SubWin import Sub_Window
from SubWin.SubUi import Ui_Dialog
from SubWin.reset_UI import SubWindow2

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内



class MainWindow(QMainWindow, Ui_MainWindow):
    File_signal = Signal(str)   # 发送信号
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.decoration()
        appIcon = QIcon('./Material/stack.png')
        self.setWindowIcon(appIcon)
        self.setWindowTitle('油型气涌出危险性评价软件v1.0')
        self.filename = None
        self.Rock_set_pushButton.clicked.connect(self.rock_set)
        self.pushButton_weight.clicked.connect(self.weight_set)
        self.Electric_cal_pushButton.clicked.connect(self.une)
        self.destroy_depth_cal__pushButton.clicked.connect(self.destroy)
        self.Sun_cal_pushButton.clicked.connect(self.sum_cal)
        # self.Stable_cal_pushButton_.clicked.connect(self.handle)
        self.File_pushButton.clicked.connect(self.open)
        self.Sub = ChildWindow()
        self.Sub1 = ChildWindow1()
        self.Sub2 = ChildWindow2()
        self.Sub1.table_signal.connect(self.save)
        self.Sub1.general_para.connect((self.destroy))
        self.File_signal.connect(self.Sub.storge)
        # self.menu_2.triggered.connect(self.handle)
        judge = QRegularExpression("^[0-9]+(\.[0-9]+$)?")
        self.lineEdit.setValidator(QRegularExpressionValidator(judge))
        # self.lineEdit_Permeability.setValidator(QRegularExpressionValidator(judge))

    def closeEvent(self, event: QCloseEvent) -> None:
        sys.exit(0)

    def decoration(self):
        self.Sun_cal_pushButton.setStyleSheet(
            '''
                background-color: #2ABf9E;
                padding: 20px;
                font-size: 15px;
            '''
        )
    def open(self):
        dialog  = QFileDialog()
        # 选择多个文件
        dialog.setFileMode(QFileDialog.ExistingFile)
        path, _ = dialog.getOpenFileName(self, "打开图片", QDir.currentPath(),"数据文件(*.dat);;所有文件(*)")
        self.filename = path
        self.textBrowser_info.append('数据导入成功')
    def save(self, SubSig):
        self.textBrowser_info.append(SubSig)
    def exit(self):
        window.close()
    def handle(self):
        self.File_signal.emit(self.filename)
        self.Sub.show()       
        pass
    def rock_set(self):
        self.Sub1.show()
    def weight_set(self):
        self.Sub2.show()
    def handle4(self):
        self.jg = jg()
        self.jg.ui.show()
    def draw(self):     # Merge to une    
        judge = re.compile(r'^[0-9]+(\.[0-9]+$)?')
        space = self.lineEdit.text()
        if not space:
            QMessageBox.information(window.pushButton, "错误", "缺少关键参数！", QMessageBox.Yes)
            return
        if not judge.match(space):
            QMessageBox.critical(window.pushButton, "错误", "参数输入错误！", QMessageBox.Yes)
            return
        if self.filename == None:
            QMessageBox.warning(window.pushButton, "警告", "未选择数据文件!", QMessageBox.Yes)
            return 
        combo = self.comboBox.currentIndex()
        result = mainFunc(self.filename, space=float(space))
        result = result.iloc[:20, :100]      
        self.fig = drawFigure(width=self.Graph_show.width()/101, height=self.Graph_show.height()/101, )
        
        im = self.fig.axes.contourf(result, cmap='rainbow')
        self.fig.axes
        self.fig.axes.invert_yaxis()
        cb = fig.fig.colorbar(im, ax=fig.axes)
        cb.set_label
        self.scene = QGraphicsScene()
        self.scene.addWidget(self.fig)
        self.Graph_show.setScene(self.scene)
        self.Graph_show.show()
        


        self.textBrowser_info.append(str('作图完成'))
    def une(self):  # 计算电法指标
        space = self.lineEdit.text()
        if not space:
            QMessageBox.information(window.Electric_cal_pushButton, "提示", "缺少电极个数参数！", QMessageBox.Yes)
            return
        if self.filename == None:
            QMessageBox.warning(window.Electric_cal_pushButton, "警告", "未选择数据文件!", QMessageBox.Yes)
            return 

        data = mainFunc(self.filename, space=float(space))
        result = data.iloc[:20, :100]
        result = np.array(result)
        self.fig = drawFigure(width=self.Graph_show.width()/101, height=self.Graph_show.height()/101, )
        im = self.fig.axes.contourf(result,cmap='rainbow')
        self.fig.axes.set_xlabel('测点前方距离/m')
        self.fig.axes.set_ylabel('底板探测深度/m')
        self.fig.axes.xaxis.tick_top()
        self.fig.axes.invert_yaxis()
        cb = self.fig.fig.colorbar(im, ax=self.fig.axes)
        cb.set_label('电阻率/Ω',loc='bottom')
        self.scene = QGraphicsScene()
        self.scene.addWidget(self.fig)
        self.Graph_show.setScene(self.scene)
        self.Graph_show.show()
        data = data.iloc[:10]
        d = []
        for row in data.index:
            d.append(uneven(data.iloc[row], 6))
        weight = Series(reversed([i for i in range(len(data))]))
        dog = Series(d)
        sum_ = sum(weight.values * dog.values/sum(weight))*10
        sum_ = round(sum_, 2)
        self.textBrowser_info.append("电法评价指标：%.2f" % sum_)
        self.label_value1.setText(str(sum_))
        return sum_
    def destroy(self):
        try:        
            Ratio_constant = (10/4)**5
            Amplitude_constant = (5/3)**2
            m = self.Sub1.ui.doubleSpinBox_thick.value()    # 采厚
            H = self.Sub1.ui.doubleSpinBox_depth.value()    # 埋深
            phi = self.Sub1.ui.doubleSpinBox_phi.value()    # 内摩擦角  
            Cm = self.Sub1.ui.doubleSpinBox_Cm_col.value()  # 煤层内聚力
            n = self.Sub1.ui.doubleSpinBox_stress.value()   # 应力集中系数
            phi0 = phi*np.pi/180    #煤层内摩擦角
            gama_list = []
            phiR_list = []
            layer_list = []
            E_list = []
            Cm_rock_list = []
            G_list = []
            for row in range(self.Sub1.ui.TableWidget.rowCount()):
                gama_list.append(float(self.Sub1.ui.TableWidget.item(row, 1).text()))
                layer_list.append(float(self.Sub1.ui.TableWidget.item(row, 2).text()))
                E_list.append(float(self.Sub1.ui.TableWidget.item(row, 3).text()))
                Cm_rock_list.append(float(self.Sub1.ui.TableWidget.item(row, 4).text()))
                G_list.append(float(self.Sub1.ui.TableWidget.item(row, 5).text()))
                phiR_list.append(float(self.Sub1.ui.TableWidget.item(row, 6).text()))
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
            self.textBrowser_info.append("计算破坏深度：{}m".format(h))
            self.label_value2.setText(str(h)+'m')
            return e1 * e2
        except Exception as e:
            self.textBrowser_info.append(str(e))
            self.textBrowser_info.append("岩层参数设置不完全")
    def sum_cal(self):
        m = self.Sub2.ui.doubleSpinBox_electric.value()
        g = self.Sub2.ui.doubleSpinBox_Stable.value()
        c = self.Sub2.ui.doubleSpinBox_permeability.value()
        s = self.Sub2.ui.doubleSpinBox_structure.value()
        s1 = self.Sub2.ui.comboBox_structure.currentIndex()
        if m+g+c+s != 1:
            self.textBrowser_info.append("错误：无效权重值")
            return
        u = self.une()
        d = self.destroy()
        permeability_list = []
        for row in range(self.Sub1.ui.TableWidget.rowCount()):
            permeability_list.append(float(self.Sub1.ui.TableWidget.item(row, 7).text()))
        p = min(permeability_list)
        if p < 50:      #低渗
            k = 0.1
        elif 100>p>=50:     #中渗
            k = 0.4
        elif  1000>p>=100:      #高渗
            k = 0.8
        elif p>=1000:       #特高渗
            k = 1
        self.textBrowser_info.append("渗透性参数取值为：{}".format(p))
        self.textBrowser_info.append("地址构造参数取值为：{}".format(s1))
        sum_value = u*m + d/100*g + k*c + s*s1
        sum_value = round(sum_value, 2)
        self.textBrowser_info.append("总评价指标：%.2f"%sum_value)
        self.label_value3.setText(str(sum_value))

class drawFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)
        self.axes = self.fig.add_subplot(111)

# 实例化一个新界面

class ChildWindow(QDialog):     # 备用界面
    def __init__(self) -> None:
        QDialog.__init__(self)
        self.ui = Sub_Window()
        self.ui.setupUi(self)
        appIcon = QIcon('./Material/curve.png')
        self.setWindowIcon(appIcon)   
        self.setWindowTitle('计算与曲线绘制')
        self.ui.pushButton_cal.clicked.connect(self.calculate)
    # slot
    def storge(self, MainSig):
        self.ui.Label.setText(MainSig)

    def calculate(self):
        FileName = self.ui.Label.text()
        if FileName == '':
             QMessageBox.information(self.ui.pushButton_cal, "提示", "未导入可用数据文件", QMessageBox.Yes)
             return 
        loader = QUiLoader()
        loader.registerCustomWidget(pg.PlotWidget)
        data = mainFunc(FileName, 0.25, 0)
        data = data.iloc[:10]
        d = []
        for row in data.index:
            d.append(uneven(data.iloc[row], 6))
        weight = Series(reversed([i for i in range(len(data))]))
        dog = Series(d)
        self.ui.curve.setTitle("岩层不均匀度", color = '009090', size='12pt')
        self.ui.curve.setBackground('w')
        self.ui.curve.showGrid(x=True, y=True)
        self.ui.curve.setLabel("left", "不均匀度")
        self.ui.curve.setLabel("bottom", "距离")
        x = dog.index
        y = dog.values
        self.ui.curve.plot(x, y, pen=pg.mkPen('b'))

class ChildWindow1(QDialog):    # 岩层参数设置 子界面
    general_para = Signal(int, int)
    row_signal = Signal(int) 
    table_signal = Signal(str)
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        appIcon = QIcon('./Material/funnel.png')
        self.setWindowIcon(appIcon)
        self.setWindowTitle('岩层参数设置')
        self.data = {}
        # lithology = QComboBox(self.ui.TableWidget)
        # lithology.addItems([u"\u6ce5\u5ca9", u"\u9875\u5ca9", u"\u7802\u5ca9"])
        # self.ui.TableWidget.setCellWidget(0, 0, lithology)
        self.ui.layer.setGeometry(QRect(30, 5, 91, 41))
        self.ui.comboBox.setGeometry(QRect(130, 15, 61, 22))
        self.ui.btn_add.clicked.connect(self.add)
        self.ui.btn_del.clicked.connect(self.delete)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_clear.clicked.connect(self.clear)    
        self.row_signal.connect(self.get_row_sig)
        self.ui.TableWidget.clicked.connect(self.send_row_sig)  

# Signal send and receive

    def send_row_sig(self):
        current_row = self.ui.TableWidget.currentRow()
        self.row_signal.emit(current_row)
    def get_row_sig(self, current_row):
        self.ui.layer1.setText('当前选定第{}层'.format(current_row+1))

# Function
    def add(self):
        self.row = self.ui.TableWidget.currentRow()
        layer_str = str(self.ui.TableWidget.currentRow())
        layer = self.ui.TableWidget.currentRow()
        # lithology = QComboBox(self.ui.TableWidget)
        # lithology.addItems([u"\u6ce5\u5ca9", u"\u9875\u5ca9", u"\u7802\u5ca9"])
        # self.ui.TableWidget.setCellWidget(layer, 0, lithology)       

        #检测该层号是否存在（已舍弃）
        # for i in range(self.layer):
        #     if self.ui.TableWidget.item(i, 0) != None:
        #         if self.ui.TableWidget.item(i, 0).text() == layer_str:
        #             QMessageBox.information(self.ui.btn_add, '提示', layer_str+'层已存在,若要修改请使用修改功能', QMessageBox.Yes)
        #             return 
        λ = self.ui.doubleSpinBox_bd.value()
        h = self.ui.doubleSpinBox_h.value()
        E = self.ui.doubleSpinBox_E.value()
        G = self.ui.doubleSpinBox_G.value()
        Rm = self.ui.doubleSpinBox_Rm.value()
        phi0 = self.ui.doubleSpinBox_phi0.value()
        permeability = self.ui.doubleSpinBox_permeability.value()
        item_bd = QTableWidgetItem(str(λ))
        item_h = QTableWidgetItem(str(h))
        item_E = QTableWidgetItem(str(E))
        item_G = QTableWidgetItem(str(Rm))
        item_Rm = QTableWidgetItem(str(G))
        item_phi0 = QTableWidgetItem(str(phi0))
        item_permeability = QTableWidgetItem(str(permeability))
        self.ui.TableWidget.setItem(layer, 1, item_bd)
        self.ui.TableWidget.setItem(layer, 2, item_h)
        self.ui.TableWidget.setItem(layer, 5, item_E)
        self.ui.TableWidget.setItem(layer, 4, item_G)
        self.ui.TableWidget.setItem(layer, 3, item_Rm)
        self.ui.TableWidget.setItem(layer, 6, item_phi0)
        self.ui.TableWidget.setItem(layer, 7, item_permeability)

    def delete(self):
        current_row = self.ui.TableWidget.currentRow()
        self.ui.TableWidget.removeRow(current_row)
        # self.ui.TableWidget.insertRow(current_row)
        lithology = QComboBox(self.ui.TableWidget)
        lithology.addItems([u"\u6ce5\u5ca9", u"\u9875\u5ca9", u"\u7802\u5ca9"])
        # self.ui.TableWidget.setCellWidget(current_row, 0, lithology)
        self.ui.layer1.setText('当前未选定岩层')
        # self.ui.comboBox.setCurrentIndex(self.ui.TableWidget.currentRow())
        pass

    def save(self):  
        for row in range(self.ui.TableWidget.rowCount()):
            self.data['岩层'] = self.ui.TableWidget.cellWidget(row, 0).currentText()
            self.data[row] = {}
            for col in range(1, self.ui.TableWidget.columnCount()):
                if self.ui.TableWidget.item(row, col) == None:
                    QMessageBox.information(self.ui.btn_save, '警告', '存在未输入数据', QMessageBox.Yes)
                    return 
                self.data[row][col] = self.ui.TableWidget.item(row, col).text()
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet('岩层参数')
        self.list1 = [self.ui.doubleSpinBox_thick.value(), self.ui.doubleSpinBox_depth.value(), self.ui.doubleSpinBox_stress.value(), self.ui.doubleSpinBox_Cm_col.value(), self.ui.doubleSpinBox_phi.value()]
        worksheet.write(0, 0, str(self.list1))
        for row in range(self.ui.TableWidget.rowCount()):
            worksheet.write(row+1, 0, self.ui.TableWidget.cellWidget(row, 0).currentText())
            for col in range(1, self.ui.TableWidget.columnCount()):
                worksheet.write(row+1, col, self.ui.TableWidget.item(row, col).text())
        workbook.save('1.xls') 
        self.table_signal.emit(str(self.data))
        # self.general_para.emit(self.ui.doubleSpinBox_thick.value(), self.ui.doubleSpinBox_depth.value())
        QMessageBox.information(self.ui.btn_save, '提示', '保存成功', QMessageBox.Yes)

        pass
    def resave(self):
        workbook = xlrd.open_workbook('1.xls')
        sheet = workbook.sheet_by_index(0)
        self.ui.TableWidget.setColumnCount(8)
        self.ui.TableWidget.setRowCount(sheet.nrows-1)
        self.ui.TableWidget.setHorizontalHeaderLabels(['岩性', '容重/KN/m³', '层厚/m', '弹性模量/Gpa', '内聚力/Mpa', '抗拉强度/Mpa', '内摩擦角/°', '渗透率/mD'])
        for i in range(0, sheet.nrows-1):
            self.lithology = QComboBox(self.ui.TableWidget)
            self.lithology.addItems([u"\u6ce5\u5ca9", u"\u9875\u5ca9", u"\u7802\u5ca9"])
            self.ui.TableWidget.setCellWidget(i, 0, self.lithology)
        for i in range(sheet.nrows-1):
            rowlist = sheet.row_values(i+1)
            self.ui.TableWidget.cellWidget(i,0).setCurrentText(rowlist[0])
            for j in range(1, len(rowlist)):
                newItem = QTableWidgetItem(rowlist[j])
                self.ui.TableWidget.setItem(i, j, newItem)

    def clear(self):
        self.ui.TableWidget.clearContents()
        layer = self.ui.comboBox.currentIndex()+1
        for i in range(0, layer+1):
            lithology = QComboBox(self.ui.TableWidget)
            lithology.addItems([u"\u6ce5\u5ca9", u"\u9875\u5ca9", u"\u7802\u5ca9"])
            self.ui.TableWidget.setCellWidget(i, 0, lithology)
        pass

class ChildWindow2(QDialog):    # 权重设置界面
    def __init__(self):
        QDialog.__init__(self)
        self.ui = SubWindow2()
        self.ui.setupUi(self)
        self.setWindowTitle('总评价指标权重设置')
        self.setWindowIcon(QIcon('./Material/Ui.png'))
        self.resize(430, 320)
        self.ui.doubleSpinBox_electric.setValue(0.4)
        self.ui.doubleSpinBox_permeability.setValue(0.25)
        self.ui.doubleSpinBox_Stable.setValue(0.25)
        self.ui.doubleSpinBox_structure.setValue(0.1)
    def getValue(self):
        pass
    
class st():
    def __init__(self) -> None:
        self.ui = QUiLoader().load('st.ui')
        self.ui.setWindowTitle('渗透率参数设置')
        self.ui.pushButton.clicked.connect(self.close)
    def value(self):
        return self.ui.lineEdit.text()
    def close(self):
        self.ui.close()

class lxcs():
    def __init__(self) -> None:
        self.ui = QUiLoader().load('lxcs.ui')
        self.ui.setWindowTitle('力学参数设置')
        self.ui.pushButton.clicked.connect(self.close)
    def value(self):
        return self.ui.lineEdit.text()
    def close(self):
        self.ui.close()

class wdx():
    def __init__(self) -> None:
        self.ui = QUiLoader().load('wdx.ui')
        self.ui.setWindowTitle('稳定性参数设置')
        self.ui.pushButton.clicked.connect(self.close)
    def value(self):
        return self.ui.lineEdit.text()
    def close(self):
        self.ui.close()

class jg():
    def __init__(self) -> None:
        self.ui = QUiLoader().load('jg.ui')
        self.ui.setWindowTitle('断层构造结构设置')
        self.ui.pushButton.clicked.connect(self.close)
    def value(self):
        return self.ui.lineEdit.text()
    def close(self):
        self.ui.close()


# Algorithm
def destroy_depth(self, phi, m, gama, h):
    K1 = (1+np.sin(phi))/(1-np.sin(phi))
    F = (K1 - 1)/sqrt(K1) + ((K1 - 1)/sqrt(K1))**2 * np.arctan(sqrt(K1))
    x_alpha = m/F*np.log(10*gama*h)  # A.H.Wilson 曲屈服区长度计算
    e1 = x_alpha*np.cos(phi)/(2*np.cos(np.pi/4+phi/2))
    e2 = e2 = np.e**((np.pi/4 + phi/2)* np.tan(phi))
    return e1 * e2

def uneven(series, n):
        Ue = 0
        count = 0
        series = series.apply(lambda x: (x-series.min())/(series.max()-series.min())) 
        for i in range(len(series)):
            s = []
            for j in range(len(series)):
                if i != j and abs(i-j)<n:
                    a = abs(series.iloc[i] - series.iloc[j])/(abs(i-j))
                    Ue += a
                    count += 1
        return 10*Ue/count  # 根据结果去求结果 doesn't make any sense

def mul(df1, df2):
    l1 = df1.values.tolist()
    l2 = df2.values.tolist()
    l3 = np.multiply(l1, l2)
    return DataFrame(l3)

def rho_3(n, filename, a, reverse=False):  # 原始数据处理
    # 处理原始数据得出
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
    #data_r.to_csv('d:/kong/aaa_/3ar.csv', encoding='gb2312')
    return data_r

def Ef(A, M, N, rho, mesh, delta_x=0.25,):  # 网格电阻值赋值
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

def mainFunc(filename, space, combo=0):
    # Grid and assignment
    mesh = DataFrame([[[0]] * 200] * 200)
    for row in range(len(mesh.index)):
        for col in range(len(mesh.columns)):
            mesh[row][col] = [0]
    mesh = mesh.to_numpy()
    n = 6
    reverse = True
    rho_s = rho_3(n=n, filename=filename, a=space, reverse=reverse)
    #rho_ss = rho_2(n=n, a=space, reverse=reverse)
    for A in rho_s.index:
        for M in range(A, len(rho_s.columns) - 1):
            Ef(A, M + 1, M + 2, rho_s.iloc[A][M], mesh=mesh)  # rho_3
            #Ef(A, M, M + 2, rho_ss.iloc[A][M])  # rho_2
    mesh = DataFrame(mesh)
    result = mesh.applymap(lambda x: sum(list(set(x))) / (len(list(set(x))) - 1) if x != [0] else np.nan)
    result.dropna(axis=1, how='all', inplace=True)
    result.dropna(axis=0, how='all', inplace=True)
    result = DataFrame(fancyimpute.KNN(k=6).fit_transform(result))
    # if not reverse:
    #     mesh.to_csv('d:/kong/aaa_/forward/meshf{}.csv'.format(len(rho_s.index)), encoding='gb2312')  # Unprocessed grid data
    #     result.to_csv('d:/kong/aaa_/forward/resultf{}.csv'.format(len(rho_s.index)), encoding='gb2312')  # Grid data processed by mean
    # elif reverse:
    #     mesh.to_csv('d:/kong/aaa_/backward/meshb{}.csv'.format(len(rho_s.index)), encoding='gb2312')  # Unprocessed grid data
    #     result.to_csv('d:/kong/aaa_/backward/resultb{}.csv'.format(len(rho_s.index)), encoding='gb2312')  # Grid data processed by mean
    return result


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(window.width(),window.height())
    window.show()
    app.setStyleSheet(  # 设置界面样式
        '''
        QTextBrowser {
            background-color: #DDDDDD;
            color: #000000;
        }

        '''
    )
    sys.exit(app.exec())

