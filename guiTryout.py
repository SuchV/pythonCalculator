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
import sys, logging

#add other variable that holds whole operation as a string and put it somewhere, ...
# ...instead of only the result

class MyButton(QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    equation = ""
    result = 0
        
    def print_equation(self, resultWindow, name, printable, operation_type):
        if printable:
                self.equation +=name
                resultWindow.setText(self.equation)
        
        if operation_type == "number":
            self.result += int(name)
                

            
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
        equationWindow = QLineEdit()
        equationWindow.setReadOnly(True)
        topLayout.addRow("Equation:", equationWindow)
        
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
                button = MyButton(f"{y*3+x+1}")
                button.setText(f"{y*3+x+1}")
                optionsLayout.addWidget(button, y, x)
                button.pressed.connect(lambda name=button.name: button.print_equation(equationWindow, name, printable=True, operation_type = "number"))
        
        # Loop adding basic arithemtic buttons
        for x in range(4):
            match x:
                case 0:
                    button = MyButton("+")
                    button.setText("+")
                    optionsLayout.addWidget(button,3,x)
                    button.pressed.connect(lambda name=button.name: button.print_equation(equationWindow, name, printable=True))
                    
                    button = MyButton("clear")
                    button.setText("clear")
                    optionsLayout.addWidget(button,x,3)
                    button.pressed.connect(lambda name=button.name: button.print_equation(equationWindow, name, result_value))
                    
                    button = MyButton("*")
                    button.setText("*")
                    optionsLayout.addWidget(button,4,x)
                    button.pressed.connect(lambda name=button.name: button.print_equation(equationWindow, name, result_value))
                case 1:
                    button = MyButton("0")
                    button.setText("0")
                    optionsLayout.addWidget(button,3,x)
                    button.pressed.connect(lambda name=button.name: button.print_equation(equationWindow, name))
                    
                    button = MyButton("back")
                    button.setText("back")
                    optionsLayout.addWidget(button,x,3)
                    button.pressed.connect(lambda name=button.name: button.print_equation(equationWindow, name, result_value))
                    
                    button = MyButton(".")
                    button.setText(".")
                    optionsLayout.addWidget(button,4,x)
                    button.pressed.connect(lambda name=button.name: button.print_equation(equationWindow, name, result_value))
                case 2:
                    button = MyButton("-")
                    button.setText("-")
                    optionsLayout.addWidget(button,3,x)
                    button.pressed.connect(lambda name=button.name: button.print_equation(equationWindow, name, result_value))                     
                    
                    button = MyButton("reset")
                    button.setText("reset")
                    optionsLayout.addWidget(button,x,3)
                    button.pressed.connect(lambda name=button.name: button.print_equation(equationWindow, name, result_value)) 
                    
                    button = MyButton("/")
                    button.setText("/")
                    optionsLayout.addWidget(button,4,x)
                    button.pressed.connect(lambda name=button.name: button.print_equation(equationWindow, name, result_value))         
                case 3:
                    button = MyButton("=")
                    button.setText("=")
                    optionsLayout.addWidget(button,3,x)
                    button.pressed.connect(lambda name=button.name: button.print_equation(equationWindow, name, result_value)) 
                    
                    button = MyButton("\u221A")
                    button.setText("\u221A")
                    optionsLayout.addWidget(button,4,x)
                    button.pressed.connect(lambda name=button.name: button.print_equation(equationWindow, name, result_value))   
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