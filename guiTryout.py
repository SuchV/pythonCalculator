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

historyWindow_value = ""
resultWindow_value = ""

class NumberButton(QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    l_value = ""
    r_value = ""
    temp = ""
        
    def take_number(self, historyWindow, currentEquationWindow, name, historyWindow_value):
        if OperationButton.op_type == "none":
            historyWindow_value = historyWindow.text()
            historyWindow_value += name
            NumberButton.l_value = historyWindow_value
            historyWindow.setText(historyWindow_value)
            currentEquationWindow.setText(NumberButton.l_value)
        else:
            historyWindow_value = historyWindow.text()
            NumberButton.temp += name
            NumberButton.r_value = NumberButton.temp
            historyWindow_value += name
            historyWindow.setText(historyWindow_value)
            currentEquationWindow.setText(NumberButton.l_value + OperationButton.op_type + NumberButton.r_value)
            
class ResetButton(QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def reset(self, historyWindow, resultWindow, currentEquationWindow):
        # Reset the text in the history and result windows
        historyWindow.setText("")
        resultWindow.setText("")
        currentEquationWindow.setText("")
        
        # Reset the variables in the NumberButton and OperationButton classes
        NumberButton.temp = ""
        NumberButton.r_value = ""
        OperationButton.op_type = "none"
        OperationButton.temp = ""
        
class ClearButton(QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def clear_equation(self, currentEquationWindow):
        # Reset the text in the currentEquationWindow
        currentEquationWindow.setText("")
        
class BackButton(QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def back(self, historyWindow, currentEquationWindow):
        # Check if the history window is not empty
        if historyWindow.text():
            # Remove the last character from  currentEquationwindow
            currentEquationWindow.setText(currentEquationWindow.text()[:-1])

            # Remove the last character from the variables in the NumberButton class
            if NumberButton.temp:
                NumberButton.temp = NumberButton.temp[:-1]
            if NumberButton.r_value:
                NumberButton.r_value = NumberButton.r_value[:-1]

class OperationButton(QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    op_type = "none"
    temp = ""
    
    def take_operator(self, historyWindow, currentEquationWindow, name, historyWindow_value):
        if OperationButton.op_type ==  "none":
                historyWindow_value = historyWindow.text()
                historyWindow_value += name
                historyWindow.setText(historyWindow_value)
                currentEquationWindow.setText(NumberButton.l_value + name + NumberButton.r_value)
                OperationButton.op_type = name
            
    def equals_operation(self, resultWindow, currentEquationWindow, resultWindow_value):
        if OperationButton.op_type == "+":
            if NumberButton.r_value == "": NumberButton.r_value == "0"
            resultWindow_value = float(NumberButton.l_value) + float(NumberButton.r_value)
            resultWindow.setText(str(resultWindow_value))
            currentEquationWindow.setText(str(resultWindow_value))

        elif OperationButton.op_type == "-":
            if NumberButton.r_value == "": NumberButton.r_value == "0"
            resultWindow_value = float(NumberButton.l_value) - float(NumberButton.r_value)
            resultWindow.setText(str(resultWindow_value))
            currentEquationWindow.setText(str(resultWindow_value))

        elif OperationButton.op_type == "*":
            if NumberButton.r_value == "": NumberButton.r_value == "0"
            resultWindow_value = float(NumberButton.l_value) * float(NumberButton.r_value)
            resultWindow.setText(str(resultWindow_value))
            currentEquationWindow.setText(str(resultWindow_value))

        elif OperationButton.op_type == "/":
            if NumberButton.r_value == "": NumberButton.r_value == "0"
            resultWindow_value = float(NumberButton.l_value) / float(NumberButton.r_value)
            resultWindow.setText(str(resultWindow_value))
            currentEquationWindow.setText(str(resultWindow_value))
        
        elif OperationButton.op_type == "^":
            if NumberButton.r_value == "": NumberButton.r_value == "0"
            resultWindow_value = float(NumberButton.l_value) ** float(NumberButton.r_value)
            resultWindow.setText(str(resultWindow_value))
            currentEquationWindow.setText(str(resultWindow_value))

        else:
            print("Error: No operation selected!")
        
        if NumberButton.r_value != "" and NumberButton.l_value != "":
            currentEquationWindow.setText(NumberButton.l_value + OperationButton.op_type + NumberButton.r_value)
            NumberButton.l_value = str(resultWindow_value)
            NumberButton.r_value = ""
            NumberButton.temp = ""
            OperationButton.op_type = "none"
            
class  Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Calculator")
        self.initUI()
        
    def resize_buttons(self, layout):
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setFixedSize(100, 100)  
        
    def initUI(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        
        # Create a form layout for the label and line edit
        topLayout = QFormLayout()
        
        # Add a label and a line edit to the layout
        historyWindow = QLineEdit()
        historyWindow.setReadOnly(True)
        topLayout.addRow("History:", historyWindow)
        
        currentEquationWindow = QLineEdit()
        currentEquationWindow.setReadOnly(True)
        topLayout.addRow("Current Equation:", currentEquationWindow)
        
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
                buttonNumber = NumberButton(f"{y*3+x+1}")
                buttonNumber.setText(f"{y*3+x+1}")
                optionsLayout.addWidget(buttonNumber, y, x)
                buttonNumber.pressed.connect(lambda name=buttonNumber.name: buttonNumber.take_number(historyWindow, currentEquationWindow, name, historyWindow_value))
        
        # Loop adding basic arithemtic buttons
        for x in range(4):
            match x:
                case 0:
                    buttonOperator = OperationButton("+")
                    buttonOperator.setText("+")
                    optionsLayout.addWidget(buttonOperator,3,x)
                    buttonOperator.pressed.connect(lambda name=buttonOperator.name: buttonOperator.take_operator(historyWindow, currentEquationWindow, name, historyWindow_value))
                    
                    buttonClear = ClearButton("clear")
                    buttonClear.setText("clear")
                    optionsLayout.addWidget(buttonClear,x,3)
                    buttonClear.pressed.connect(lambda: buttonClear.clear_equation(currentEquationWindow))    
                                    
                    buttonOperator = OperationButton("*")
                    buttonOperator.setText("*")
                    optionsLayout.addWidget(buttonOperator,4,x)
                    buttonOperator.pressed.connect(lambda name=buttonOperator.name: buttonOperator.take_operator(historyWindow, currentEquationWindow, name, historyWindow_value))
                case 1:
                    buttonNumber = NumberButton("0")
                    buttonNumber.setText("0")
                    optionsLayout.addWidget(buttonNumber,3,x)
                    buttonNumber.pressed.connect(lambda name=buttonNumber.name: buttonNumber.take_number(historyWindow, currentEquationWindow, name, historyWindow_value))
                    
                    backButton = BackButton("back")
                    backButton.setText("back")
                    optionsLayout.addWidget(backButton,x,3)
                    backButton.clicked.connect(lambda: backButton.back(historyWindow, currentEquationWindow))
                    
                    buttonNumber = NumberButton(".")
                    buttonNumber.setText(".")
                    optionsLayout.addWidget(buttonNumber,4,x)
                    buttonNumber.pressed.connect(lambda name=buttonNumber.name: buttonNumber.take_number(historyWindow, currentEquationWindow, name, historyWindow_value))
                case 2:
                    buttonOperator = OperationButton("-")
                    buttonOperator.setText("-")
                    optionsLayout.addWidget(buttonOperator,3,x)
                    buttonOperator.pressed.connect(lambda name=buttonOperator.name: buttonOperator.take_operator(historyWindow, currentEquationWindow, name, historyWindow_value))                     
                    
                    resetButton = ResetButton("reset")
                    resetButton.setText("reset")
                    optionsLayout.addWidget(resetButton,x,3)
                    resetButton.clicked.connect(lambda: resetButton.reset(historyWindow, resultWindow, currentEquationWindow))
                    
                    buttonOperator = OperationButton("/")
                    buttonOperator.setText("/")
                    optionsLayout.addWidget(buttonOperator,4,x)
                    buttonOperator.pressed.connect(lambda name=buttonOperator.name: buttonOperator.take_operator(historyWindow, currentEquationWindow, name, historyWindow_value))        
                case 3:
                    buttonOperator = OperationButton("=")
                    buttonOperator.setText("=")
                    optionsLayout.addWidget(buttonOperator,3,x)
                    buttonOperator.pressed.connect(lambda name=buttonOperator.name: buttonOperator.equals_operation(resultWindow, currentEquationWindow, resultWindow_value))
                    
                    buttonOperator = OperationButton("^")
                    buttonOperator.setText("x^x")
                    optionsLayout.addWidget(buttonOperator,4,x)
                    buttonOperator.pressed.connect(lambda name=buttonOperator.name: buttonOperator.take_operator(historyWindow, currentEquationWindow, name, historyWindow_value)) 
                case _:
                    logging.warning("Arithmetic buttonOperator adder error!")
                    
        
        # # Nest the inner layouts into the outer layout
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(optionsLayout)
        
        # Set the window's main layout
        self.setLayout(outerLayout)

def main():
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    screen_width, screen_height = screen_resolution.width(), screen_resolution.height()
    window = Window()
    window.setGeometry(0,0,screen_width//8,screen_height//4)
    
    # Calculate center point of screen
    center_x = screen_width // 2
    center_y = screen_height // 2
    
    # Adjust center point by half the width and height of the window
    window_x = center_x - window.width() // 2
    window_y = center_y - window.height() // 2
    
    # Move window to adjusted center point
    window.move(window_x, window_y)
    
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()