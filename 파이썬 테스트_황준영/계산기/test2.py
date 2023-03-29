import sys
import math
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("test2.ui")[0] #ui 파일연결

class MainWindow(QMainWindow, form_class):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.flag = False  # 결과 출력 여부
        self.chk  = False  # 연산자 중복 여부
        self.chk4 = False  # 오류 여부
        
    def onButton(self) :
        if self.chk4  == True:
            self.chk4 = False
            self.flag  = False
            self.label.setText('')
        if self.label.text() == '0':
            self.label.setText('')
        if self.flag == True:
            self.label2.setText('')
            self.label.setText('')
            self.flag = False
        widget = self.sender()
        t = widget.text()
        o = self.label.text()
        o = o + t
        self.label.setText(o)
        self.chk = False
        
    def btnMul(self):
        if self.chk == True:
            return
        if self.chk4 == True:
            return
        widget = self.sender()
        t = widget.text()
        o = self.label.text()
        b = self.label2.text()
        
        for a in (' x ',' + ',' - ',' ÷ '):    
            if b.find(a):
                if self.label.text() != '':
                    try:
                        expr = self.label2.text() + self.label.text()
                        expr = expr.replace(' x ',' * ')
                        expr = expr.replace(' ÷ ',' / ')
                        expr = expr.replace(' = ','')
                        num = str(eval(expr))
                        index = num.find('.')
                        if index != -1:
                            fnum = int(num[index+1:])
                            if fnum > 0:
                             self.label2.setText(num + t)
                            else:
                             iTotal = str(int(float(num)))
                             self.label2.setText(iTotal + t)
                        else:
                            self.label2.setText(num + t)
                    except:
                        self.label.setText("0으로 나눌 수 없습니다.")
                        self.chk4 = True
            if self.flag == True:
                self.label2.setText(self.label.text() +t)
                self.label.setText('')
                self.flag = False
                return
            self.label.setText('')
            self.chk = True

    def btnDot(self):
        if self.label.text().find('.') != -1:
            return
        widget = self.sender()
        t = widget.text()
        o = self.label.text()
        o = o + t
        self.label.setText(o)

    def btnChange(self):
         if float(self.label.text()) > 0:
             self.label.setText('-' + self.label.text())
         elif float(self.label.text()) < 0:
               self.label.setText(self.label.text().replace('-',''))

    def btnDouble(self):
        if self.label.text() == '':
            return
        self.label.setText(str(eval(self.label.text()+'**2')))

    def btnRute(self):
        if self.label.text() == '':
            return
        self.label.setText(str(eval(self.label.text()+'**(1/2)')))

    def btnOdiv(self):
        if self.label.text() == '':
            return
        self.label.setText(str(eval('1/'+self.label.text())))

    def btnPercent(self):
        if self.label.text() == '0':
            return
        self.label.setText(str(eval(self.label.text()+'/100')))

    def btnBack(self):
        if self.label.text() == '':
            return
        txt = self.label.text()
        index = len(txt) - 1
        self.label.setText(txt[:index])
        if index == 0:
            self.label.setText('0')
        
    def btnTotal(self):
        b = self.label.text()
        if b == '':
            self.label.setText('0')    
            return
        for a in ('x','÷','*','/'):
            index = b.find(a)
            if index == 0:
                expr = self.label2.text() + self.label.text()
                expr = expr.replace('x','*')
                expr = expr.replace('÷','/')
                expr = expr.replace('=','')
                print(expr)
                num = str(eval(expr))
                index = num.find('.')
                if index != -1:
                    fnum = int(num[index+1:])
                    if fnum > 0:
                        self.label2.setText(num + a)
                    else:
                        iTotal = str(int(float(num)))
                        self.label2.setText(iTotal + a)
                else:
                    self.label2.setText(num + a)
            elif index != -1:
                try:
                    expr = self.label.text()
                    expr = expr.replace('x',' * ')
                    expr = expr.replace('÷',' / ')
                    num = str(eval(expr))
                    index = num.find('.')
                    if index != -1:
                        fnum = int(num[index+1:])
                        if fnum > 0:
                             self.label2.setText(expr)
                             self.label.setText(num)
                        else:
                             iTotal = str(int(float(num)))
                             self.label2.setText(iTotal + t)
                    else:
                        self.label2.setText(expr + ' = ')
                        self.label.setText(str(num))
                        return
                except:
                    self.label.setText("수식이 잘못되었습니다.")
                    self.chk4 = True
                    return
                        
        try:
            if self.label2.text().find('=') != -1:
                try:
                    if self.label2.text() == '':
                        self.label2.setText(self.label.text() + ' = ')
                        return
                    txt = self.label2.text()
                    index = txt.find(' ')
                    txt = txt[:index]
                    txt2 = self.label2.text()
                    txt3 = self.label.text()
                    expr = txt2.replace(txt,txt3)
                    expr = expr.replace(' x ',' * ')
                    expr = expr.replace(' ÷ ',' / ')
                    expr = expr.replace(' = ','')
                    num = str(eval(expr))
                    index = num.find('.')
                    if index != -1:
                        fnum = int(num[index+1:])
                        if fnum > 0:
                             self.label.setText(num)
                        else:
                             iTotal = str(int(float(num)))
                             self.label.setText(iTotal)
                    else:
                        self.label.setText(num)
                    expr = expr.replace(' * ',' x ')
                    expr = expr.replace(' / ',' ÷ ')
                    self.label2.setText('%s = ' %(expr))
                    self.flag = True
                    return
                except:
                    return
            if self.label2.text() == '':
                    self.label2.setText(self.label.text() + ' = ')
                    return
            expr = self.label2.text() + self.label.text()
            expr = expr.replace(' x ',' * ')
            expr = expr.replace(' ÷ ',' / ')
            num = str(eval(expr))
            index = num.find('.')
            if index != -1:
                fnum = int(num[index+1:])
                if fnum > 0:
                     self.label.setText(num)
                else:
                     iTotal = str(int(float(num)))
                     self.label.setText(iTotal)
            else:
                self.label.setText(num)
            expr = expr.replace(' * ',' x ')
            expr = expr.replace(' / ',' ÷ ')
            self.label2.setText('%s = ' %(expr))
            self.flag = True
        except:
            self.label.setText("0으로 나눌 수 없습니다.")
            self.chk4 = True

    def btnClear(self):
        self.flag = self.chk = False 
        self.label.setText('0')
        

if __name__=="__main__":
    app = QApplication(sys.argv) #실행클래스 객체생성
    myWindow = MainWindow()      # 메인윈도우 객체생성
    myWindow.show()              # 메인객체 출력
    app.exec_()                  # 실행객체 실행
