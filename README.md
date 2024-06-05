# Mesh-Algorithm-based-on-DC-detection
a algorithm to explain the Geological Resistance under the mine
# 简介
## 程序功能
主要针对地下矿井巷道中底板及掘进迎头前方未知区域，以含油气瓦斯为对象，量化分析其涌出危险性并给出评估指标

## 工作原理
是通过地球物理探测手段提供前置数据，将物理探测得到的电位数据转化为岩层实时电阻率对地质情况进行解释

程序主要由两大部分组成:
- 第一部分关于岩层视电阻率算法，通过巷道底板布置电极，以恒定电流采集电压值，以发射电极到接收电极为半径形成的电位球面表征该球壳的视电阻率对岩层进行网格划分后，以球壳视电阻率代表曲线，对经过的网格进行赋值
<img src="https://github.com/KryptonToT/Mesh-Algorithm-based-on-DC-detection/blob/main/Resource/探测原理示意图.png" width="600px">
- 第二部分为数据处理后的可视化表现，及主程序载体即交互界面的制作

## [**油型气涌出危险性评价软件V2.0**](https://github.com/KryptonToT/Mesh-Algorithm-based-on-DC-detection/tree/main/My2.0)


### UI2.0主界面
<img src="https://github.com/KryptonToT/Mesh-Algorithm-based-on-DC-detection/blob/main/Resource/2.0init.png" width="600px">

### UI2.0 电法数据处理模块演示
<img src="https://github.com/KryptonToT/Mesh-Algorithm-based-on-DC-detection/blob/main/Resource/My2.0Elc.gif" width="600px">

### UI2.0 岩层地质参数模块演示
<img src="https://github.com/KryptonToT/Mesh-Algorithm-based-on-DC-detection/blob/main/Resource/My2.0geo.gif" width="600px">

### UI2.0 还没放入核心算法的计算模块演示
<img src="https://github.com/KryptonToT/Mesh-Algorithm-based-on-DC-detection/blob/main/Resource/My2.0tbd.gif" width="600px">

## [**油型气涌出危险性评价软件V1.0**](https://github.com/KryptonToT/Mesh-Algorithm-based-on-DC-detection/tree/main/My) 

### 早期完成的UI1.0流程演示😂😂😂
基本也是由这几大模块构成，不过没有什么艺术细胞，设计审美点确实乏善可陈，但主要功能还是在线的。

主要模块都采用子界面的方式来进行功能扩展，结果显示都堆在一块也是痛点所在。

<img src="https://github.com/KryptonToT/Mesh-Algorithm-based-on-DC-detection/blob/main/Resource/My1.0.gif" width="600px">

### UI1.0的计算结果画面
除了界面设计美化不足之外，还存在以下问题：
- 代码结构、注释很混乱导致阅读困难。
- 算法不够精简导致计算工程中程序会发生未响应的情况，暂时还没想到好的解决办法。

所以运行时间长，就没放运行过程的动图，截了个运行结果的图。

<img src="https://github.com/KryptonToT/Mesh-Algorithm-based-on-DC-detection/blob/main/Resource/1.0%E7%BB%93%E6%9E%9C.png" width="600px">

✨✨✨最后感谢许多大佬的例子，让我受益良多，成为我阴影迷雾中的指路明灯

✨✨✨Thank all of the light in my trudge grope

[**常用控件使用方法及例子**](https://github.com/PyQt5/PyQt)

[**常用qss样式**](https://github.com/GTRONICK/QSS)

[**大佬现代界面例子**](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6)

[**PySide入门手册**](https://github.com/se7enXF/pyside2)
