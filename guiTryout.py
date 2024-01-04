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
        else:
            historyWindow_value = historyWindow.text()
            NumberButton.temp += name
            NumberButton.r_value = NumberButton.temp
            historyWindow_value += name
            historyWindow.setText(historyWindow_value)
            
class ResetButton(QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def reset(self, historyWindow, resultWindow):
        # Reset the text in the history and result windows
        historyWindow.setText("")
        resultWindow.setText("")

        # Reset the variables in the NumberButton and OperationButton classes
        NumberButton.temp = ""
        NumberButton.r_value = ""
        OperationButton.op_type = "none"
        OperationButton.temp = ""
        
class ClearHistoryButton(QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def clear_history(self, historyWindow):
        # Reset the text in the history window
        historyWindow.setText("")
        
class BackButton(QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def back(self, historyWindow):
        # Check if the history window is not empty
        if historyWindow.text():
            # Remove the last character from the history window
            historyWindow.setText(historyWindow.text()[:-1])

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
    
        
    # [IDEA] doesnt work when you add - or + before any number is given
    def take_operator(self, historyWindow, name, historyWindow_value):
        if OperationButton.op_type ==  "none":
                historyWindow_value = historyWindow.text()
                historyWindow_value += name
                historyWindow.setText(historyWindow_value)
                OperationButton.op_type = name
            
    def equals_operation(self, resultWindow, resultWindow_value):
        if OperationButton.op_type == "+":
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
        
        if NumberButton.r_value != "" and NumberButton.l_value != "":
            NumberButton.l_value = str(resultWindow_value)
            NumberButton.r_value = ""
            NumberButton.temp = ""
            OperationButton.op_type = "none"
            
            
            
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
        topLayout.addRow("History:", historyWindow)
        
        currentEquation = QLineEdit()
        currentEquation.setReadOnly(True)
        topLayout.addRow("Current Equation:", currentEquation)
        
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
                    
                    clearHistorybutton = ClearHistoryButton("clear")
                    clearHistorybutton.setText("clear history")
                    optionsLayout.addWidget(clearHistorybutton,x,3)
                    clearHistorybutton.pressed.connect(lambda: clearHistorybutton.clear_history(historyWindow))    
                                    
                    button = OperationButton("*")
                    button.setText("*")
                    optionsLayout.addWidget(button,4,x)
                    button.pressed.connect(lambda name=button.name: button.take_operator(historyWindow, name, historyWindow_value))
                case 1:
                    buttonN = NumberButton("0")
                    buttonN.setText("0")
                    optionsLayout.addWidget(buttonN,3,x)
                    buttonN.pressed.connect(lambda name=buttonN.name: buttonN.take_number(historyWindow, name, historyWindow_value))
                    
                    backButton = BackButton("back")
                    backButton.setText("back")
                    optionsLayout.addWidget(backButton,x,3)
                    backButton.clicked.connect(lambda: backButton.back(historyWindow))
                    
                    button = NumberButton(".")
                    button.setText(".")
                    optionsLayout.addWidget(button,4,x)
                    button.pressed.connect(lambda name=button.name: button.take_number(historyWindow, name, historyWindow_value))
                case 2:
                    button = OperationButton("-")
                    button.setText("-")
                    optionsLayout.addWidget(button,3,x)
                    button.pressed.connect(lambda name=button.name: button.take_operator(historyWindow, name, historyWindow_value))                     
                    
                    resetButton = ResetButton("reset")
                    resetButton.setText("reset")
                    optionsLayout.addWidget(resetButton,x,3)
                    resetButton.clicked.connect(lambda: resetButton.reset(historyWindow, resultWindow))
                    
                    button = OperationButton("/")
                    button.setText("/")
                    optionsLayout.addWidget(button,4,x)
                    button.pressed.connect(lambda name=button.name: button.take_operator(historyWindow, name, historyWindow_value))        
                case 3:
                    button = OperationButton("=")
                    button.setText("=")
                    optionsLayout.addWidget(button,3,x)
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