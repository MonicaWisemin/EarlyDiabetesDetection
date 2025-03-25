from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class HoverButton(QPushButton):
    """自定义按钮类，支持鼠标悬停和离开事件"""
    def __init__(self, text, description, parent=None):
        super().__init__(text, parent)  # 将 parent 参数传递给父类的构造函数
        self.description = description  # 添加一个属性来存储简介文本
        self.init_ui()

    def init_ui(self):
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(60)
        self.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                border: none;
                border-radius: 6px;
                font-size: 16pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QPushButton:pressed {
                background-color: #1B4F72;
            }
        """)

    def enterEvent(self, event):
        """鼠标悬停时触发"""
        super().enterEvent(event)  # 调用父类的 enterEvent 方法
        self.parent().show_description(self.description)  # 显示简介文本

    def leaveEvent(self, event):
        """鼠标离开时触发"""
        super().leaveEvent(event)  # 调用父类的 leaveEvent 方法
        self.parent().clear_description(event)


class StartPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Diabetes Prediction Tool")
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Start Page")
        self.setFixedSize(800, 650)

        # 设置背景颜色为淡蓝色
        self.setStyleSheet("background-color: #E6F3FF;")

        # 主布局
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(20)

        # 标题
        title_label = QLabel("Diabetes Prediction Tool")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title_label.setStyleSheet("color: #2C3E50; padding: 10px;")
        main_layout.addWidget(title_label)

        # 按钮 1
        btn1 = HoverButton("Model w D1", "This dataset can be used to predict patients with these features:\n Glucose, BMI, Age, Pregnancies, DPF, Blood Pressure, Insulin", self)
        btn1.clicked.connect(self.go_to_main_page)
        main_layout.addWidget(btn1)

        # 按钮 2
        btn2 = HoverButton("Model w D2", "This dataset can be used to predict patients with these features:\n Gender, AGE, Urea, Cr, HbA1c, Chol, TG, HDL, LDL, VLDL, BII", self)
        btn2.clicked.connect(self.go_to_main2_page)
        main_layout.addWidget(btn2)

        # 按钮 3
        btn3 = HoverButton("Model w D3", "This dataset can be used to predict patients with these features:\n Hour of the day, Date of the Month, Month in a year, Value of Blood Sugar", self)
        btn3.clicked.connect(self.go_to_main3_page)
        main_layout.addWidget(btn3)

        # 添加一个占位符，将标题推到顶部
        main_layout.addStretch(1)

        # 简介显示区域
        self.description_label = QLabel()
        self.description_label.setFixedHeight(300)
        self.description_label.setStyleSheet("""
            background-color: #77BBFF;  /* 淡蓝色背景 */
            color: #333333;            /* 深灰色文字 */
            font-size: 14pt;           /* 字体大小 */
            font-family: Arial;        /* 字体类型 */
            text-align: center;        /* 文字居中对齐 */
            padding: 10px;             /* 内边距 */
        """)
        self.description_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.description_label)

        # 设置主布局
        self.setLayout(main_layout)

    def show_description(self, text):
        """显示简介"""
        self.description_label.setText(text)

    def clear_description(self, event):
        """清除简介"""
        self.description_label.clear()

    def go_to_main_page(self):
        """切换到主界面"""
        self.stacked_widget.setFixedSize(800, 800)
        self.stacked_widget.setCurrentIndex(1)

    def go_to_main2_page(self):
        """切换到主界面"""
        self.stacked_widget.setFixedSize(800, 800)
        self.stacked_widget.setCurrentIndex(2)

    def go_to_main3_page(self):
        self.stacked_widget.setFixedSize(800, 800)
        self.stacked_widget.setCurrentIndex(3)


    def go_to_main_page(self):
        """切换到主界面"""
        self.stacked_widget.setFixedSize(800, 800)
        self.stacked_widget.setCurrentIndex(1)

    def go_to_main2_page(self):
        """切换到主界面"""
        self.stacked_widget.setFixedSize(800, 800)
        self.stacked_widget.setCurrentIndex(2)

    def go_to_main3_page(self):
        self.stacked_widget.setFixedSize(800, 800)
        self.stacked_widget.setCurrentIndex(3)