import logging
from PyQt5 import  QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QGridLayout
)
import sys

#add other variable that holds whole operation as a string and put it somewhere, ...
# ...instead of only the result


class MyButton(QPushButton):
    def __init__(self, name=None, additional_arg=None):
        super().__init__()
        self.name = name
        self.additional_arg = additional_arg
            
class  Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Calculator")
        self.initUI()
        
    def initUI(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        
        # Create a form layout for the label and line edit
        topLayout = QFormLayout()
        
        # Add a label and a line edit to the layout
        result = QLineEdit()
        result.setReadOnly(True)
        topLayout.addRow("Result:", result)
        
        # Create a layout for the buttons
        optionsLayout = QGridLayout()
        
        # Add some buttons to the layout
        # Loop adding numerical buttons (1:9)
        for x in range(2,-1,-1):
            for y in range(0,3):
                optionsLayout.addWidget(MyButton(f"{y*3+x+1}",f"b_num{y*3+x+1}"),y,x)
        
        # Loop adding basic arithemtic buttons
        for x in range(4):
            y=x
            match x:
                case 0:
                    optionsLayout.addWidget(QPushButton("+"),3,x)
                    optionsLayout.addWidget(QPushButton("clear"),x,3)
                case 1:
                    optionsLayout.addWidget(QPushButton("0"),3,x)
                    optionsLayout.addWidget(QPushButton("back"),x,3)
                case 2:
                    optionsLayout.addWidget(QPushButton("-"),3,x) 
                    optionsLayout.addWidget(QPushButton("reset"),x,3)
                case 3:
                    optionsLayout.addWidget(QPushButton("="),3,x)
                case _:
                    logging.warning("Arithmetic button adder error!")
            match y:
                case 0:
                    optionsLayout.addWidget(QPushButton("*"),4,x)
                case 1:
                    optionsLayout.addWidget(QPushButton("."),4,x)
                case 2:
                    optionsLayout.addWidget(QPushButton("/"),4,x) 
                case 3:
                    optionsLayout.addWidget(QPushButton("\u221A"),4,x)
                case _:
                    logging.warning("Arithmetic button adder error!")
            
        # b_num_1 = QPushButton("1")
        # b_num_1.setAccessibleName("b_num_1")
        # b_num_1.pressed.connect(lambda: self.add_user_operation(result)
        
        # # Nest the inner layouts into the outer layout
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(optionsLayout)
        
        # Set the window's main layout
        self.setLayout(outerLayout)

    def add_user_operation(self, result, name):
        result.setText(f"Button {name} pressed")
        


def main():
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    # [IDEA] Add here dynamic windows size based on screen resolution
    screen_width, screen_height = screen_resolution.width(), screen_resolution.height()
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()