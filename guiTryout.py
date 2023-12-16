from PyQt5 import  QtGui
from copy import deepcopy
from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QGridLayout
)
import sys, logging

#add other variable that holds whole operation as a string and put it somewhere, ...
# ...instead of only the result
#Temporary solution using global variables

historyWindow_value = ""
resultWindow_value = ""


class NumberButton(QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    l_value = ""
    r_value = ""
    temp = ""
    
        
    def take_number(self, historyWindow, name, historyWindow_value):
        if OperationButton.op_type == "none":
            historyWindow_value = historyWindow.text()
            historyWindow_value += name
            NumberButton.l_value = historyWindow_value
            historyWindow.setText(historyWindow_value)
            print(NumberButton.l_value)
        else:
            historyWindow_value = historyWindow.text()
            NumberButton.temp += name
            NumberButton.r_value = NumberButton.temp
            historyWindow_value += NumberButton.r_value
            historyWindow.setText(historyWindow_value)
            print(NumberButton.r_value)
        
        
class OperationButton(QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    op_type = "none"
        
    # [IDEA] doesnt work when you add - or + before any number is given
    def take_operator(self, historyWindow, name, historyWindow_value):
        if OperationButton.op_type ==  "none":
            historyWindow_value = historyWindow.text()
            historyWindow_value += name
            OperationButton.op_type = name
            historyWindow.setText(historyWindow_value)
            
    def equals_operation(self, resultWindow, resultWindow_value):
        if OperationButton.op_type == "+":
            print(NumberButton.l_value)
            resultWindow_value = float(NumberButton.l_value) + float(NumberButton.r_value)
            resultWindow.setText(str(resultWindow_value))
        elif OperationButton.op_type == "-":
            resultWindow_value = float(NumberButton.l_value) - float(NumberButton.r_value)
            resultWindow.setText(str(resultWindow_value))
        elif OperationButton.op_type == "*":
            resultWindow_value = float(NumberButton.l_value) * float(NumberButton.r_value)
            resultWindow.setText(str(resultWindow_value))
        elif OperationButton.op_type == "/":
            resultWindow_value = float(NumberButton.l_value) / float(NumberButton.r_value)
            resultWindow.setText(str(resultWindow_value))
        else:
            logging.warning("Equals operation error!")
        OperationButton.op_type = ""
            
            
            
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
        historyWindow = QLineEdit()
        historyWindow.setReadOnly(True)
        topLayout.addRow("Equation:", historyWindow)
        
        # Add a label and a line edit to the layout
        resultWindow = QLineEdit()
        resultWindow.setReadOnly(True)
        topLayout.addRow("Result:", resultWindow)
        
        # Create a layout for the buttons
        optionsLayout = QGridLayout()
        
        # Add some buttons to the layout
        # Loop adding numerical buttons (1:9)
        for x in range(2,-1,-1):
            for y in range(0,3):
                buttonN = NumberButton(f"{y*3+x+1}")
                buttonN.setText(f"{y*3+x+1}")
                optionsLayout.addWidget(buttonN, y, x)
                buttonN.pressed.connect(lambda name=buttonN.name: buttonN.take_number(historyWindow, name, historyWindow_value))
        
        # Loop adding basic arithemtic buttons
        for x in range(4):
            match x:
                case 0:
                    button = OperationButton("+")
                    button.setText("+")
                    optionsLayout.addWidget(button,3,x)
                    button.pressed.connect(lambda name=button.name: button.take_operator(historyWindow, name, historyWindow_value))
                    
                    button = OperationButton("clear")
                    button.setText("clear")
                    optionsLayout.addWidget(button,x,3)
                    button.pressed.connect(lambda name=button.name: button.take_operator(historyWindow, name, historyWindow_value))
                    
                    button = OperationButton("*")
                    button.setText("*")
                    optionsLayout.addWidget(button,4,x)
                    button.pressed.connect(lambda name=button.name: button.take_operator(historyWindow, name, historyWindow_value))
                case 1:
                    buttonN = NumberButton("0")
                    buttonN.setText("0")
                    optionsLayout.addWidget(buttonN,3,x)
                    buttonN.pressed.connect(lambda name=buttonN.name: buttonN.take_number(historyWindow, name, historyWindow_value))
                    
                    button = OperationButton("back")
                    button.setText("back")
                    optionsLayout.addWidget(button,x,3)
                    button.pressed.connect(lambda name=button.name: button.take_operator(historyWindow, name, historyWindow_value))
                    
                    button = NumberButton(".")
                    button.setText(".")
                    optionsLayout.addWidget(button,4,x)
                    button.pressed.connect(lambda name=button.name: button.take_number(historyWindow, name, historyWindow_value))
                case 2:
                    button = OperationButton("-")
                    button.setText("-")
                    optionsLayout.addWidget(button,3,x)
                    button.pressed.connect(lambda name=button.name: button.take_operator(historyWindow, name, historyWindow_value))                     
                    
                    button = OperationButton("reset")
                    button.setText("reset")
                    optionsLayout.addWidget(button,x,3)
                    button.pressed.connect(lambda name=button.name: button.take_operator(historyWindow, name, historyWindow_value))
                    
                    button = OperationButton("/")
                    button.setText("/")
                    optionsLayout.addWidget(button,4,x)
                    button.pressed.connect(lambda name=button.name: button.take_operator(historyWindow, name, historyWindow_value))        
                case 3:
                    button = OperationButton("=")
                    button.setText("=")
                    optionsLayout.addWidget(button,3,x)
                    button.pressed.connect(lambda name=button.name: button.take_operator(historyWindow, name, historyWindow_value))
                    button.pressed.connect(lambda name=button.name: button.equals_operation(resultWindow, resultWindow_value))
                    
                    button = OperationButton("\u221A")
                    button.setText("\u221A")
                    optionsLayout.addWidget(button,4,x)
                    button.pressed.connect(lambda name=button.name: button.take_operator(historyWindow, name, historyWindow_value)) 
                case _:
                    logging.warning("Arithmetic button adder error!")
                    
        
        # # Nest the inner layouts into the outer layout
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(optionsLayout)
        
        # Set the window's main layout
        self.setLayout(outerLayout)

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