from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QGridLayout
)
import sys

class  Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Calculator")
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        topLayout = QFormLayout()
        # Add a label and a line edit to the form layout
        result = topLayout.addRow("Result:", QLineEdit())
        # Create a layout for the checkboxes
        optionsLayout = QGridLayout()
        # Add some buttons to the layout
        b_function_clear = optionsLayout.addWidget(QPushButton("Clear"),0,0)
        b_function_back = optionsLayout.addWidget(QPushButton("Back"),0,1)
        b_function_reset = optionsLayout.addWidget(QPushButton("Reset"),0,2)
        b_function_sqrt = optionsLayout.addWidget(QPushButton("\u221A"),0,3)
        b_num_7 = optionsLayout.addWidget(QPushButton("7"),1,0)
        b_num_8 = optionsLayout.addWidget(QPushButton("8"),1,1)
        b_num_9 = optionsLayout.addWidget(QPushButton("9"),1,2)
        b_op_sub = optionsLayout.addWidget(QPushButton("-"),1,3)
        b_num_4 = optionsLayout.addWidget(QPushButton("4"),2,0)
        b_num_5 = optionsLayout.addWidget(QPushButton("5"),2,1)
        b_num_6 = optionsLayout.addWidget(QPushButton("6"),2,2)
        b_op_add = optionsLayout.addWidget(QPushButton("+"),2,3)
        b_num_1 = optionsLayout.addWidget(QPushButton("1"),3,0)
        b_num_2 = optionsLayout.addWidget(QPushButton("2"),3,1)
        b_num_3 = optionsLayout.addWidget(QPushButton("3"),3,2)
        b_op_equals = optionsLayout.addWidget(QPushButton("="),3,3)
        b_num_0 = optionsLayout.addWidget(QPushButton("0"),4,0)
        b_op_dot = optionsLayout.addWidget(QPushButton("."),4,1)
        b_op_div = optionsLayout.addWidget(QPushButton("/"),4,2)
        b_op_mult = optionsLayout.addWidget(QPushButton("*"),4,3)
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(optionsLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

def main():
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    screen_width, screen_height = screen_resolution.width(), screen_resolution.height()
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()