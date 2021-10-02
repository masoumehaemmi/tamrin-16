import math
from sympy import cot
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
import sympy

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()


        loader = QUiLoader()
        self.ui = loader.load("cal.ui" , None)
        self.ui.show()

        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_sum.clicked.connect(self.sub)
        self.ui.btn_sum.clicked.connect(self.mul)
        self.ui.btn_sum.clicked.connect(self.div)
        self.ui.btn_sum.clicked.connect(self.flo)
        self.ui.btn_sum.clicked.connect(self.pers)
        self.ui.btn_sum.clicked.connect(self.sin)
        self.ui.btn_sum.clicked.connect(self.cos)
        self.ui.btn_sum.clicked.connect(self.tan)
        self.ui.btn_sum.clicked.connect(self.log)
        self.ui.btn_sum.clicked.connect(self.cot)
        self.ui.btn_sum.clicked.connect(self.sqrt)
        


        self.ui.btn1.clicked.connect(self.btn1)
        self.ui.btn2.clicked.connect(self.btn2)
        self.ui.btn3.clicked.connect(self.btn3)
        self.ui.btn4.clicked.connect(self.btn4)
        self.ui.btn5.clicked.connect(self.btn5)
        self.ui.btn6.clicked.connect(self.btn6)
        self.ui.btn7.clicked.connect(self.btn7)
        self.ui.btn8.clicked.connect(self.btn8)
        self.ui.btn9.clicked.connect(self.btn9)
        self.ui.btn0.clicked.connect(self.btn0)

        

        self.ui.btn_C.clicked.connect(self.clear)

    def btn1(self):
        self.ui.output.setText(self.ui.output.text()+ '1')
    def btn2(self):
        self.ui.output.setText(self.ui.output.text()+ '2')
    def btn3(self):
        self.ui.output.setText(self.ui.output.text()+ '3')
    def btn4(self):
        self.ui.output.setText(self.ui.output.text()+ '4')
    def btn5(self):
        self.ui.output.setText(self.ui.output.text()+ '5')
    def btn6(self):
        self.ui.output.setText(self.ui.output.text()+ '6')
    def btn7(self):
        self.ui.output.setText(self.ui.output.text()+ '7')
    def btn8(self):
        self.ui.output.setText(self.ui.output.text()+ '8')
    def btn9(self):
        self.ui.output.setText(self.ui.output.text()+ '9')
    def btn0(self):
        self.ui.output.setText(self.ui.output.text()+ '0')
    
    def sum(self):
       
       self.num1 = float(self.ui.output.text())
       self.ui.output.setText("")
       self. Computing = "+"
 
    def equal(self):
        if self.Computing =="+" :

            self.num2 = float(self.ui.output.text())

            result = self.num1 + self.num2
            self.ui.output.setText(str(result))

        if self.Computing == "-" :

            self.num2 = float(self.ui.output.text())

            result = self.num1 - self.num2
            self.ui.output.setText(str(result))

        if self.Computing == "*" :

            self.num2 = float(self.ui.output.text())

            result = self.num1 * self.num2
            self.ui.output.setText(str(result))

        if self.Computing == "/" :
            if self.num2 != 0 :

                self.num2 = float(self.ui.output.text())

                result = self.num1 / self.num2
            self.ui.output.setText(str(result))

        if self.Computing == "%":

            self.num2 = float((self.ui.output.text()) / 100)
            self.ui.output.setText(str(result))

        if self.Computing == "." :

            self.num2 = float(self.ui.output.text())

            result = self.num1 + self.num2
            self.ui.output.setText(str(result))


    def sub(self):
       
       self.num1 = float(self.ui.output.text())
       self.ui.output.setText("")
       self. Computing = "-"

    def mul(self):
       
       self.num1 = float(self.ui.output.text())
       self.ui.output.setText("")
       self. Computing = "*"
    def div(self):
       
       self.num1 = float(self.ui.output.text())
       self.ui.output.setText("")
       self. Computing = "/"
    def sin(self):
       
       self.num1 = float(self.ui.output.text())
       result=math.sin(math.radians(self.num1))
       self.ui.output.setText(str(result))

    def cos(self):
       
       self.num1 = float(self.ui.output.text())
       result=math.cos(math.radians(self.num1))
       self.ui.output.setText(str(result))
    
    def log(self):
       
       self.num1 = float(self.ui.output.text())
       result=math.log(self.num1)
       self.ui.output.setText(str(result))

    def tan(self):
        self.num1 = float(self.ui.output.text())
        result=math.tan(math.radians(self.num1))
        self.ui.output.setText(str(result))

    def cot(self):
       
       self.num1 = float(self.ui.output.text())
       result=cot(math.radians(self.num1))
       self.ui.output.setText(str(result))

    def sqrt(self):
       
       self.num1 = float(self.ui.output.text())
       result=math.sqrt(self.num1)
       self.ui.output.setText(str(result))

    def flo(self):
       
        for i in self.ui.output.text():
            if '.' not in self.ui.output.text():
                self.ui.output.setText(self.ui.output.text()+ '.')
    

    def pers(self):
       
       self.num1 = int(self.ui.output.text())
       self.ui.output.setText("")

    def clear(self):
        self.ui.output.setText('')

app = QApplication([])
window = Calculator()



app.exec()


