

from PyQt5 import (QtWidgets,
                   QtCore,
                   QtGui,
                   uic,)
import sys
from sqlite3 import *
def connection():
    conn = connect('usersAndFilms.db')
    cur = conn.cursor()
    return conn, cur
def SearchForUser(username):
    conn, cur = connection()
    cur.execute('Select UserID, username, password FROM users WHERE username =?',(username,))
    returnData = cur.fetchall()
    conn.close()
    return returnData


class Login(QtWidgets.QMainWindow): 
    def __init__(self):
        super(Login, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('log in.ui',self) #Loads window design from the ui file
        self.show() #Window is shown when an instance of the class is made
        
        #Handles the event of buttons being clicked
        self.submitButton.clicked.connect(self.loginButtonMethod)
        self.clearButton.clicked.connect(self.clearButtonMethod)
    
        self.defaultUser = 'username'
        self.defaultUser = 'password'

    
    def loginButtonMethod(self):
        username = self.input1.text()
        password = self.input2.text()
        
        if username == "" or password == "":
            self.messageBox('Blank fields', 'Please enter both a username and password!','warning')
        else:
            userdata = SearchForUser(username)
            if len(userdata) > 0:
                if userdata[0][2] == password:
                    self.messageBox('Login Succesful ', 'You have logged in succesfully !', 'warning')
                    self.clearButtonMethod()
                    self.close()
                else:
                    self.messageBox('Log in Failed', 'Incorrect password entered','info')
                    self.clearButtonMethod()
            else:
                    self.messageBox('Log in Failed', 'Incorrect username entered','info')
                    self.clearButtonMethod()
                
                
                
    def clearButtonMethod(self):
        self.input1.setText('')
        self.input2.setText('')

    def messageBox(self, title, content, iconType="info"):
        #A message box object is created
        msgBox = QtWidgets.QMessageBox()
        #Sets the message box icon based on icon type passed as a parameter
        if iconType == "info":
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
        elif iconType == "question":
            msgBox.setIcon(QtWidgets.QMessageBox.Question)
        elif iconType == "warning":
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        else:
            msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        #Sets text and title to arguments passed into the function
        msgBox.setText(content)
        msgBox.setWindowTitle(title)
        #Shows the message box to the user
        msgBox.exec()
        
    
     
def main1():
    app = QtWidgets.QApplication(sys.argv)
    #Initialises various menus
    loginWindow = Login()
    #Starts menu execution
    app.exec()
    #Quits menu execution when all windows are closed
    QtWidgets.QApplication.quit()
        
main1()





class Calculator(QtWidgets.QMainWindow): 
    def __init__(self):
        super(Calculator, self).__init__() 
        uic.loadUi('calculator.ui',self)
        self.operator = False
        self.eq = ''
        self.show()
        self.Clear.clicked.connect(self.Aclear)
        self.Equals.clicked.connect(self.calc)
        self.Button9.clicked.connect(lambda:self.press_it('9',False))
        self.Button8.clicked.connect(lambda:self.press_it('8',False))
        self.Button7.clicked.connect(lambda:self.press_it('7',False))
        self.Button6.clicked.connect(lambda:self.press_it('6',False))
        self.Button5.clicked.connect(lambda:self.press_it('5',False))
        self.Button4.clicked.connect(lambda:self.press_it('4',False))
        self.Button3.clicked.connect(lambda:self.press_it('3',False))
        self.Button2.clicked.connect(lambda:self.press_it('2',False))
        self.Button1.clicked.connect(lambda:self.press_it('1',False))
        self.Button0.clicked.connect(lambda:self.press_it('0',False))
        self.Sub.clicked.connect(lambda:self.press_it('-',True))
        self.Add.clicked.connect(lambda:self.press_it('+',True))
        self.Times.clicked.connect(lambda:self.press_it('*',True))
        self.Divide.clicked.connect(lambda:self.press_it('/',True))
              
    def calc(self):
        self.label.setText(str(eval(self.eq)))
        self.operator = False
        self.eq = self.label.text
    
    def press_it(self,op, operator):
        if operator != self.operator or operator == False:
            self.eq += op 
            self.label.setText(self.label.text() + op)
            self.operator = operator
    
    def Aclear(self):
        self.label.setText('')
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    CalcWindow = Calculator()
    app.exec()
        
main()