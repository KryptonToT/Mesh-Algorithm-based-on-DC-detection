import sys
import os
# 替换 sys.path.append("..")
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from run import *
from modules.app_Settings import Settings

# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class UIFunctions(MainWindow):
    # -----------窗口最大化与还原调整---------------
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
            self.ui.maxBtn.setToolTip("Restore")
            self.ui.maxBtn.setIcon(QIcon(u":/icons/images/icons/restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.verticalLayout_20.setContentsMargins(10, 10, 10, 10)
            self.ui.maxBtn.setToolTip("Maximize")
            self.ui.maxBtn.setIcon(QIcon(u":/icons/images/icons/maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()
    #---------------------------------------------------
    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE
    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status
    # 
    # START - GUI DEFINITIONS
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        self.ui.TopContent.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            self.ui.TopContent.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minBtn.hide()
            self.ui.maxBtn.hide()
            self.ui.exitBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.BackGround.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maxBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.exitBtn.clicked.connect(lambda: self.close())

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS

    def toggleMenu(self, enable):
        if enable:
            # get width
            width = self.ui.leftMenu.width()
            maxExtend = Settings.MENU_WIDTH
            color = Settings.TOGGLE_BUTTON_COLOR
            standard = 75
            style = self.ui.toggleButton.styleSheet()
            
            # set max width
            if width == 75:
                widthExtend = maxExtend
                self.ui.toggleButton.setStyleSheet(style + color)
            else:
                widthExtend = standard
                self.ui.toggleButton.setStyleSheet(style.replace(color, ''))

            # Animation
            self.animation = QPropertyAnimation(self.ui.leftMenu, b'minimumWidth')
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtend)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def toggleLeftBox(self, enable):
        if enable:
            # get width
            width  = self.ui.extraLeftBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0
            
            # get btn style
            style = self.ui.toggleButton.styleSheet()

            #set max width 
            if width == 0:
                widthExtended = maxExtend
                # select btn
                self.ui.toggleButton.setStyleSheet(style + color)
            else:
                widthExtended = standard
                # reset btn
                self.ui.toggleButton.setStyleSheet(style.replace(color, ''))

        UIFunctions.start_box_animation(self, width, "left")

    def LeftBox(self, enable):
        if enable:
            # get width
            width = self.ui.extraLeftBox.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 0
            # set max width
            if width == 0:
                widthExtend = maxExtend
            else:
                widthExtend = standard

            # Animation
            self.animation = QPropertyAnimation(self.ui.extraLeftBox, b'minimumWidth')
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtend)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            
    def start_box_animation(self, left_box_width, direction):
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION 组合动画
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.start()
    # Select Menu
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect
    def selectStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))
            elif w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))    

