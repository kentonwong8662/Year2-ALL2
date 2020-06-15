#!C:\Users\User\AppData\Local\Programs\Python\Python36-32\python.exe

import tkinter as tk
import pymysql
import time
import tkinter.scrolledtext as tkst
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL
from tkinter import *

global l
l = 0

class Login():
    
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x400')
        self.root.title("Cloudson Limited")
        
        self.usrlabel = tk.Label(self.root,text = 'Username :')
        self.usrlabel.place(x=5,y=30)
        self.usrentry = tk.Entry(self.root,width= 25)
        self.usrentry.place(x=75, y=30)
        
        self.passlabel = tk.Label(self.root,text = 'Password :')
        self.passlabel.place(x = 5,y = 80)
        self.passentry = tk.Entry(self.root, show="*",width= 25)
        self.passentry.place(x = 75, y = 80)    
        
        self.btn1 = tk.Button(self.root, text='Enter', \
                              command=self.check)
        self.btn1.place(x=5,y=155)
        
        self.username, self.password = [], []
        connection = pymysql.connect(host='localhost', user='root', password='', db='pos')
 
        try:
   
            with connection.cursor() as cursor:
        
                sql = "SELECT sf_Username, sf_Password FROM staff "
                
                cursor.execute(sql)

                print()
 
            for row in cursor:
                self.username.append(row[0])
                self.password.append(row[1])     
              
        finally:
    
            connection.close()
            

            
    def check(self):       
        
        usrcheck = 0
        passcheck = 0
        x = 0
        y = 0
        
        while(x == 0):
            if self.username[y] == self.usrentry.get():
                usrcheck = 1
                
            if self.password[y] == self.passentry.get():
                passcheck = 1
            
            if y == len(self.username)-1:
                x = 1                
           
            y = y + 1
               
        if usrcheck == 1 and passcheck == 1:  
            self.menu()
            
        elif usrcheck == 0 :
            self.passlabel = tk.Label(self.root,text = 'Wrong username')
            self.passlabel.place(x = 5,y = 50)
            self.passlabel = tk.Label(self.root,text = '                                                                                        ')
            self.passlabel.place(x = 5,y = 100)
        
        elif passcheck == 0:
            self.passlabel = tk.Label(self.root,text = 'Wrong password')
            self.passlabel.place(x = 5,y = 100)
            self.passlabel = tk.Label(self.root,text = '                                                                                        ')
            self.passlabel.place(x = 5,y = 50)
        
        else :
            self.__init__()       
            
                
    def menu(self):
        global l
        l = 1
        self.root.destroy()

checkflag = 0

    
class menu:
    def __init__(self, root):
           
        self.root = root
        self.root.geometry('600x600')
        self.root.title("Cloudson Limited")
        self.nb = ttk.Notebook(root)
        
        self.page0 = ttk.Frame(self.nb)
        self.page1 = ttk.Frame(self.nb)
        self.page2 = ttk.Frame(self.nb)
        self.page3 = ttk.Frame(self.nb)
        self.page4 = ttk.Frame(self.nb)
        self.a = 1
        
        self.ID, self.name, self.brand, self.type, self.Rom, self.price, self.stock = [], [], [], [], [], [], []
        connection = pymysql.connect(host='localhost', user='root', password='', db='pos')
 
        try:
   
            with connection.cursor() as cursor:
        
                sql = "SELECT * FROM `products` "
                
                cursor.execute(sql)

                print()
 
            for row in cursor:
                self.ID.append(row[0])
                self.name.append(row[1])     
                self.brand.append(row[2])
                self.type.append(row[3])
                self.Rom.append(row[4])
                self.price.append(row[5])
                self.stock.append(row[6])
        finally:
    
            connection.close()
            
        self.nb.add(self.page0, text='Pay')        
        self.nb.add(self.page1, text='Check Products')
        self.nb.add(self.page2, text='Product Update')
        self.nb.add(self.page3, text='Delete Products')
        self.nb.add(self.page4, text='Z-report')
        self.ovlmoney = 0
        '''
        pay
        '''
        self.pay = 0
        self.sell = 0
        self.allmoney = 0
        self.money = 0       
        self.nb.pack(expand=1, fill="both")        
        self.editArea1 = tkst.ScrolledText(self.page0,width=40,height=20)
        self.editArea1.pack(fill="x", expand=True) 
        self.editArea1.tag_configure("b", justify="right")
        self.editArea1.config(state = NORMAL)
        
        self.editArea1.insert(tk.INSERT,('%-15s%-30s%15s%10s\n'%
                                    ('Product ID','Product Name','Price','Number')))
        
        self.paylabel = tk.Label(self.page0,text = 'Please enter The ID of the product:')
        self.paylabel.place(x=5,y=5)
        self.payentry = tk.Entry(self.page0,width= 30)
        self.payentry.place(x=5, y=30)
        
        self.paylabel1 = tk.Label(self.page0,text = 'Please enter The number of the product:')
        self.paylabel1.place(x=5,y=70)
        self.payentry1 = tk.Entry(self.page0,width= 10)
        self.payentry1.place(x=5, y=90)
        
        self.paybutton=tk.Button(self.page0, text='Enter',command=lambda: self.payment())
        self.paybutton.place(x = 250, y = 85)
        self.paybutton.config(state=NORMAL)
        
        self.paybutton1=tk.Button(self.page0, text='Delete',command=lambda: self.delpay())
        self.paybutton1.place(x = 300, y = 85)
        self.paybutton1.config(state=NORMAL)
        
        tk.Label(self.page0, bg='grey93',text = '~'*70).place(x = 0, y = 130)
        
        self.paybutton=tk.Button(self.page0, text='Pay',command=lambda: self.finpay())
        self.paybutton.place(x = 5, y = 425)
        self.paybutton.config(state=NORMAL)
        
        '''
        check product
        '''
        self.checkLabel1 = tk.Label(self.page1, bg='grey93',text = 'Product checking :')
        self.checkLabel1.place(x=5,y=5)
        self.checkLabel2 = tk.Label(self.page1, bg='grey93',text = 'The data that base on:')
        self.checkLabel2.place(x = 5,y = 35)
        
        self.checkOption1= ttk.Combobox(self.page1, width=12, textvariable=type)
        self.checkOption1['values'] = ('product ID', 'Product name', 'Overall') 
        self.checkOption1.grid(column=1, row=1)
        self.checkOption1.current(0)
        self.checkOption1.place(x = 5, y = 65)
        
        self.paybutton=tk.Button(self.page1, text='Enter',command=lambda: self.check_products())
        self.paybutton.place(x = 250, y = 60)
        self.paybutton.config(state=NORMAL)

        
        tk.Label(self.page1, bg='grey93',text = '~'*70).place(x = 0, y = 105)
        
        
        '''
        update
        '''

        self.updateLabel1 = tk.Label(self.page2, bg='grey93',text = 'Please input the Product ID if you want to update that Product :')
        self.updateLabel1.place(x=5,y=5)
        
        self.updateLabel2 = tk.Label(self.page2, bg='grey93',text = 'Please enter the product ID :')
        self.updateLabel2.place(x = 5,y = 35)
        self.updateEntry2 = tk.Entry(self.page2,width= 15)
        self.updateEntry2.place(x = 5, y = 65)
        
        self.updateSearch=tk.Button(self.page2, text='Enter',command=self.showdata)
        self.updateSearch.place(x = 250, y = 60)
        self.updateSearch.config(state=NORMAL)
                    
        tk.Label(self.page2, bg='grey93',text = '~'*70).place(x = 0, y = 105)
        
        self.updateLabel3 = tk.Label(self.page2, bg='grey93',text = ' ')
        self.updateLabel3.place(x=5,y=155)
        
        self.updateLabel4 = tk.Label(self.page2, bg='grey93',text = 'Please choose the data type of the product:')
        self.updateLabel4.place(x = 5,y = 200)

        self.updateOption1= ttk.Combobox(self.page2, width=12, textvariable=type)
        self.updateOption1['values'] = ('product ID', 'Product name', 'Brand', 'Type', 'Rom', 'Price', 'Stock') 
        self.updateOption1.grid(column=1, row=1)
        self.updateOption1.current(0)
        self.updateOption1.place(x = 5, y = 225)
        
        self.updateLabel6 = tk.Label(self.page2, bg='grey93',text = 'New data:')
        self.updateLabel6.place(x = 5,y = 265)
        self.updateEntry6 = tk.Entry(self.page2,width= 15)
        self.updateEntry6.place(x = 5, y = 290)
        
        self.updateSubmit=tk.Button(self.page2, text='submit', \
            command=lambda: self.updateProduct())
        self.updateSubmit.place(x = 5, y=335)
        self.updateSubmit.config(state=NORMAL)                
        
        self.updateEntry2.config(state=NORMAL)
        self.updateEntry6.config(state=NORMAL)
        self.updateOption1.config(state=NORMAL) 
        
        '''
        delete
        '''
        
        self.delLabel1 = tk.Label(self.page3, bg='grey93',text = 'Please input the Product ID if you want to delete that Product :')
        self.delLabel1.place(x=5,y=5)
        
        self.delLabel2 = tk.Label(self.page3, bg='grey93',text = 'Please enter the product ID :')
        self.delLabel2.place(x = 5,y = 35)
        self.delEntry2 = tk.Entry(self.page3,width= 15)
        self.delEntry2.place(x = 5, y = 65)
        
        tk.Label(self.page3, bg='grey93',text = '~'*70).place(x = 5, y = 105)
        
        self.delLabel3 = tk.Label(self.page3, bg='grey93',text = ' ')
        self.delLabel3.place(x=5,y=155)
        
        self.delSearch=tk.Button(self.page3, text='Enter', \
            command=self.showdata2)
        self.delSearch.place(x = 250, y = 60)
        self.delSearch.config(state=NORMAL)
        
        
        self.delDel=tk.Button(self.page3, text='Delete', \
            command=self.deldata)
        self.delDel.place(x = 20, y=200)
        self.delDel.config(state=NORMAL)
        
        '''
        zreport
        '''
        self.zLabel = tk.Label(self.page4, bg='grey93',text = 'Please enter the amount of cash is the cash register :')
        self.zLabel.place(x = 5,y = 5)
        self.zEnrty = tk.Entry(self.page4,width= 15)
        self.zEnrty.place(x = 5, y = 25)
        self.zbutton=tk.Button(self.page4, text='Generate z-report', \
            command=self.zreport)
        self.zbutton.place(x = 5, y=65)
        self.zbutton.config(state=NORMAL)     
        
    def zreport(self):  
        numcheck = 0
        a = 0
        try:
            a = int(self.zEnrty.get()) - 1  
            self.zLabel = tk.Label(self.page4,text = '                                                                                                                          ')
            self.zLabel.place(x=5,y=45) 
            
        except:
            print(numcheck)
            self.zLabel = tk.Label(self.page4,text = 'Invalid input!!! Please enter a number!!!')
            self.zLabel.place(x=5,y=45)
            
        finally:
            numcheck = 1
        
        if (numcheck == 1):
            localtime = time.asctime( time.localtime(time.time()) )
            tk.Label(self.page4, bg='grey93',text = '~'*70).place(x = 5, y = 95)
            self.zLabel1 = tk.Label(self.page4, bg='grey93',text = 'Z-Report')
            self.zLabel1.place(x = 5,y = 115)
            tk.Label(self.page4, bg='grey93',text = '~'*70).place(x = 5, y = 135)
            self.zLabel1 = tk.Label(self.page4, bg='grey93',text = 'Store: Cloudson')
            self.zLabel1.place(x = 5,y = 155)
            self.zLabel1 = tk.Label(self.page4, bg='grey93',text = '%s'%localtime)
            self.zLabel1.place(x = 5,y = 175)
            tk.Label(self.page4, bg='grey93',text = '~'*70).place(x = 5, y = 195)
            self.zLabel1 = tk.Label(self.page4, bg='grey93',text = 'Total sales: %s'%self.allmoney)
            self.zLabel1.place(x = 5,y = 215)
            a = int(self.zEnrty.get()) - self.allmoney
            self.zLabel1 = tk.Label(self.page4, bg='grey93',text = 'Balance: %d'%a)
            self.zLabel1.place(x = 5,y = 235)  
        
    def delpay(self):
        self.outlabel = tk.Label(self.page0,text = '                                                                                                                     ')
        self.outlabel.place(x = 200,y = 425)
        self.ID, self.name, self.brand, self.type, self.Rom, self.price, self.stock = [], [], [], [], [], [], []
        connection = pymysql.connect(host='localhost', user='root', password='', db='pos')
 
        try:
   
            with connection.cursor() as cursor:
        
                sql = "SELECT * FROM `products` "
                
                cursor.execute(sql)

                print()
 
            for row in cursor:
                self.ID.append(row[0])
                self.name.append(row[1])     
                self.brand.append(row[2])
                self.type.append(row[3])
                self.Rom.append(row[4])
                self.price.append(row[5])
                self.stock.append(row[6])
        finally:
    
            connection.close()
        self.editArea1.config(state = NORMAL)
        checkflag = 0
        IDcheck = 0
        numcheck = 0
        x = 0
        y = 0
        try:
            a = int(self.payentry1.get()) + 1
            self.paylabel = tk.Label(self.page0,text = '                                                                                                               ')
            self.paylabel.place(x=5,y=110)
            numcheck = 1
            
        except:
            self.paylabel = tk.Label(self.page0,text = 'Invalid input!!! Please enter a number!!!')
            self.paylabel.place(x=5,y=110)
            numcheck = 0
            
        finally:
            numcheck = 1
        
        while(x == 0):
            if(self.ID[y] == self.payentry.get()):
                IDcheck = 1
                checkflag = y 
                x = 1
            
            y = y + 1
            
            if(y == len(self.ID)-1):
                x = 1       
        
        if IDcheck == 1 and numcheck == 1:                                                                  
            self.paylabel2 = tk.Label(self.page0,text = '                                                                                                                        ')
            self.paylabel2.place(x=5,y=50)                   
            self.editArea1.insert(tk.INSERT,('%-15s%-30s%15s%10s\n'%
                                    (self.ID[checkflag],self.name[checkflag],self.price[checkflag],'-'+self.payentry1.get())))    
                
            self.money = self.money - (int(self.price[checkflag])*int(self.payentry1.get()))
            
            connection = pymysql.connect(host='localhost', user='root', password='', db='pos')
        
            try:
   
                with connection.cursor() as cursor:
                    
                    val = int(self.stock[checkflag])+int(self.payentry1.get())
        
                    sql = "UPDATE products SET pd_Stock = '"+str(val)+"' WHERE pd_ID = '"+self.ID[checkflag]+"'"
                
                    cursor.execute(sql)
                
                    connection.commit()

            finally:
    
                connection.close()
        
        else:
            self.paylabel = tk.Label(self.page0,text = 'This ID does not exist!!!')
            self.paylabel.place(x=5,y=50)
        
        self.ovllabel1 = tk.Label(self.page0,text = '                                                                                                                         ')
        self.ovllabel1.place(x=400,y=425) 
        self.ovllabel1 = tk.Label(self.page0,text='Total: %d'%self.money)
        self.ovllabel1.place(x=400,y=425)
        self.editArea1.config(state = DISABLED)
        
    def payment(self):
        print(self.pay)
        if self.pay == 1:
            self.editArea1.delete('1.1', END)
        self.pay = 0
        self.clearlabel1 = tk.Label(self.page0,text = '                                                                                                                                ')
        self.clearlabel1.place(x=5,y=450)
        self.clearlabel1 = tk.Label(self.page0,text = '                                                                                                                                ')
        self.clearlabel1.place(x=5,y=470)
        self.clearlabel1 = tk.Label(self.page0,text = '                                                                                                                                ')
        self.clearlabel1.place(x=300,y=465)
        self.clearlabel1 = tk.Label(self.page0,text = '                                                                                                                                ')
        self.clearlabel1.place(x=5,y=490)
        self.clearlabel1 = tk.Label(self.page0,text = '                                                                                                                                ')
        self.clearlabel1.place(x=5,y=520)
        self.ID, self.name, self.brand, self.type, self.Rom, self.price, self.stock = [], [], [], [], [], [], []
        connection = pymysql.connect(host='localhost', user='root', password='', db='pos')
 
        try:
   
            with connection.cursor() as cursor:
        
                sql = "SELECT * FROM `products` "
                
                cursor.execute(sql)

                print()
 
            for row in cursor:
                self.ID.append(row[0])
                self.name.append(row[1])     
                self.brand.append(row[2])
                self.type.append(row[3])
                self.Rom.append(row[4])
                self.price.append(row[5])
                self.stock.append(row[6])
        finally:
    
            connection.close()
        self.editArea1.config(state = NORMAL)
        checkflag = 0
        IDcheck = 0
        numcheck = 0
        x = 0
        y = 0
        try:
            a = int(self.payentry1.get()) + 1
            self.paylabel = tk.Label(self.page0,text = '                                                                                                               ')
            self.paylabel.place(x=5,y=110)
            numcheck = 1
            
        except:
            self.paylabel = tk.Label(self.page0,text = 'Invalid input!!! Please enter a number!!!')
            self.paylabel.place(x=5,y=110)
            numcheck = 0
        
        
        while(x == 0):
            if(self.ID[y] == self.payentry.get()):
                IDcheck = 1
                checkflag = y 
                x = 1
            
            y = y + 1
            
            if(y == len(self.ID)-1):
                x = 1       
        
        if IDcheck == 1 and numcheck == 1:
            if int(self.stock[checkflag]) == 0:
                self.outlabel = tk.Label(self.page0,text = 'This product is out of stock!!')
                self.outlabel.place(x = 200,y = 425)
                
            else: 
                self.outlabel = tk.Label(self.page0,text = '                                                                                                                     ')
                self.outlabel.place(x = 200,y = 425)   
                self.paylabel2 = tk.Label(self.page0,text = '                                                                                                                    ')
                self.paylabel2.place(x=5,y=50)                   
                self.editArea1.insert(tk.INSERT,('%-15s%-30s%15s%10s\n'%
                                                (self.ID[checkflag],self.name[checkflag],self.price[checkflag],self.payentry1.get())))    
                
                self.money = self.money + (int(self.price[checkflag])*int(self.payentry1.get()))
            
                connection = pymysql.connect(host='localhost', user='root', password='', db='pos')
        
                try:
   
                    with connection.cursor() as cursor:
                    
                        val = int(self.stock[checkflag])-int(self.payentry1.get())
        
                        sql = "UPDATE products SET pd_Stock = '"+str(val)+"' WHERE pd_ID = '"+self.ID[checkflag]+"'"
                
                        cursor.execute(sql)
                
                        connection.commit()

                finally:
    
                    connection.close()
        
        else:
            self.paylabel = tk.Label(self.page0,text = 'This ID does not exist!!!')
            self.paylabel.place(x=5,y=50)
        
        self.ovllabel1 = tk.Label(self.page0,text = '                                                                                                                          ')
        self.ovllabel1.place(x=400,y=425) 
        self.ovllabel1 = tk.Label(self.page0,text = 'Total: %d'%self.money)
        self.ovllabel1.place(x=400,y=425)
        self.editArea1.config(state = DISABLED)      
                 
    def finpay(self):
        pay = 0
        
        self.finpaylabel1 = tk.Label(self.page0,text = 'Please enter the amount of money that pay:')
        self.finpaylabel1.place(x=5,y=450)
        self.finpayentry1 = tk.Entry(self.page0,width= 10)
        self.finpayentry1.place(x=5, y=470)
        self.paybutton=tk.Button(self.page0, text='Finish',command=lambda: self.finpay1())
        self.paybutton.place(x = 300, y = 465)
        self.paybutton.config(state=NORMAL)
        
    def finpay1(self):
        pay = 0
        try:
            pay = int(self.finpayentry1.get()) - self.money
            self.finpayerrlabel1 = tk.Label(self.page0,text = '                                                                                                                     ')
            self.finpayerrlabel1.place(x=5,y=490)
        except:         
            self.finpayerrlabel1 = tk.Label(self.page0,text = 'Invalid input!!Please input a number!!!')
            self.finpayerrlabel1.place(x=5,y=490)
        finally:
            if pay  >= 0:
                self.endpaylabel1 = tk.Label(self.page0,text = '                                                                                                                    ')
                self.endpaylabel1.place(x=5,y=520)
                self.endpaylabel1 = tk.Label(self.page0,text = 'Give change: %d'%pay)
                self.endpaylabel1.place(x=5,y=520)
                self.allmoney = self.allmoney + self.money
            else:
                self.endpaylabel1 = tk.Label(self.page0,text = '                                                                                                                    ')
                self.endpaylabel1.place(x=5,y=520)
                self.endpaylabel1 = tk.Label(self.page0,text = 'The money is not enough to pay the price!!!')
                self.endpaylabel1.place(x=5,y=520) 
        self.pay = 1               
        self.editArea1.delete('1.100',END)    
    def showdata(self):
        IDcheck = 0
        self.checkflag = 0
        x = 0
        y = 0
        
        while(x == 0):
            if(self.ID[y] == self.updateEntry2.get()):
                IDcheck = 1
                self.checkflag = y 
                x = 1
            
            else:
                self.dataLabel11 = tk.Label(self.page2, bg='grey93',text ="ID does not exist!!! Please enter the correct product ID!!!")
                self.dataLabel11.place(x=5,y=85)
            
            if(y == len(self.ID)-1):
                x = 1             
            y = y + 1
            
        if(IDcheck == 1):
            
            self.dataLabel11 = tk.Label(self.page2, bg='grey93',text ="                                                                                                               ")
            self.dataLabel11.place(x=5,y=85)
            
            self.clearLabel1 = tk.Label(self.page2, bg='grey93',text ="                                                                                                               ")
            self.clearLabel1.place(x=10,y=135)
            self.clearLabel1 = tk.Label(self.page2, bg='grey93',text ="                                                                                                               ")
            self.clearLabel1.place(x=10,y=155)
            
            
            self.dataLabel1 = tk.Label(self.page2, bg='grey93',text =(self.ID[self.checkflag]))
            self.dataLabel1.place(x=10,y=155)
            self.dataLabel11 = tk.Label(self.page2, bg='grey93',text ="ID")
            self.dataLabel11.place(x=10,y=135)
            
            self.dataLabel2 = tk.Label(self.page2, bg='grey93',text =(self.name[self.checkflag]))
            self.dataLabel2.place(x=60,y=155)
            self.dataLabel12 = tk.Label(self.page2, bg='grey93',text ="Product name")
            self.dataLabel12.place(x=60,y=135)
            
            self.dataLabel3 = tk.Label(self.page2, bg='grey93',text =(self.brand[self.checkflag]))
            self.dataLabel3.place(x=170,y=155)
            self.dataLabel13 = tk.Label(self.page2, bg='grey93',text ="Brand")
            self.dataLabel13.place(x=170,y=135)            
            
            self.dataLabel4 = tk.Label(self.page2, bg='grey93',text =(self.type[self.checkflag]))
            self.dataLabel4.place(x=220,y=155)
            self.dataLabel14 = tk.Label(self.page2, bg='grey93',text ="Type")
            self.dataLabel14.place(x=220,y=135)        
            
            self.dataLabel5 = tk.Label(self.page2, bg='grey93',text =(self.Rom[self.checkflag]))
            self.dataLabel5.place(x=370,y=155)
            self.dataLabel15 = tk.Label(self.page2, bg='grey93',text ="Rom")
            self.dataLabel15.place(x=370,y=135)
            
            self.dataLabel6 = tk.Label(self.page2, bg='grey93',text =(self.price[self.checkflag]))
            self.dataLabel6.place(x=420,y=155)
            self.dataLabel16 = tk.Label(self.page2, bg='grey93',text ="Price")
            self.dataLabel16.place(x=420,y=135)            
            
            self.dataLabel7 = tk.Label(self.page2, bg='grey93',text =(self.stock[self.checkflag]))
            self.dataLabel7.place(x=480,y=155)
            self.dataLabel17 = tk.Label(self.page2, bg='grey93',text ="Stock")
            self.dataLabel17.place(x=480,y=135)
                     
    def showdata2(self):
        IDcheck = 0
        self.checkflag = 0
        x = 0
        y = 0
        
        while(x == 0):
            if(self.ID[y] == self.delEntry2.get()):
                IDcheck = 1
                self.checkflag = y 
                x = 1
            
            else:
                self.dataLabel12 = tk.Label(self.page3, bg='grey93',text ="ID does not exist!!! Please enter the correct product ID!!!")
                self.dataLabel12.place(x=5,y=85)
            
            if(y == len(self.ID)-1):
                x = 1             
            y = y + 1
            
        if(IDcheck == 1):
            
            self.dataLabel11 = tk.Label(self.page3, bg='grey93',text ="                                                                                                               ")
            self.dataLabel11.place(x=5,y=85)
            
            self.clearLabel1 = tk.Label(self.page3, bg='grey93',text ="                                                                                                               ")
            self.clearLabel1.place(x=10,y=135)
            self.clearLabel1 = tk.Label(self.page3, bg='grey93',text ="                                                                                                               ")
            self.clearLabel1.place(x=10,y=155)
            
            
            self.dataLabel1 = tk.Label(self.page3, bg='grey93',text =(self.ID[self.checkflag]))
            self.dataLabel1.place(x=10,y=155)
            self.dataLabel11 = tk.Label(self.page3, bg='grey93',text ="ID")
            self.dataLabel11.place(x=10,y=135)
            
            self.dataLabel2 = tk.Label(self.page3, bg='grey93',text =(self.name[self.checkflag]))
            self.dataLabel2.place(x=60,y=155)
            self.dataLabel12 = tk.Label(self.page3, bg='grey93',text ="Product name")
            self.dataLabel12.place(x=60,y=135)
            
            self.dataLabel3 = tk.Label(self.page3, bg='grey93',text =(self.brand[self.checkflag]))
            self.dataLabel3.place(x=170,y=155)
            self.dataLabel13 = tk.Label(self.page3, bg='grey93',text ="Brand")
            self.dataLabel13.place(x=170,y=135)            
            
            self.dataLabel4 = tk.Label(self.page3, bg='grey93',text =(self.type[self.checkflag]))
            self.dataLabel4.place(x=220,y=155)
            self.dataLabel14 = tk.Label(self.page3, bg='grey93',text ="Type")
            self.dataLabel14.place(x=220,y=135)        
            
            self.dataLabel5 = tk.Label(self.page3, bg='grey93',text =(self.Rom[self.checkflag]))
            self.dataLabel5.place(x=370,y=155)
            self.dataLabel15 = tk.Label(self.page3, bg='grey93',text ="Rom")
            self.dataLabel15.place(x=370,y=135)
            
            self.dataLabel6 = tk.Label(self.page3, bg='grey93',text =(self.price[self.checkflag]))
            self.dataLabel6.place(x=420,y=155)
            self.dataLabel16 = tk.Label(self.page3, bg='grey93',text ="Price")
            self.dataLabel16.place(x=420,y=135)            
            
            self.dataLabel7 = tk.Label(self.page3, bg='grey93',text =(self.stock[self.checkflag]))
            self.dataLabel7.place(x=480,y=155)
            self.dataLabel17 = tk.Label(self.page3, bg='grey93',text ="Stock")
            self.dataLabel17.place(x=480,y=135)  
            
    def showdata1(self):
        IDcheck = 0
        self.checkflag = 0
        x = 0
        y = 0
        while(x == 0):
            if(self.ID[y] == self.checkentry.get() or self.name[y] == self.checkentry.get()):
                IDcheck = 1
                self.checkflag = y 
                x = 1

            y = y + 1
            
            if(y == len(self.ID)-1):
                x = 1             
        
        if(IDcheck == 1):
            
            self.data1Label1 = tk.Label(self.page1, bg='grey93',text =(self.ID[self.checkflag]))
            self.data1Label1.place(x=10,y=215)
            self.data1Label11 = tk.Label(self.page1, bg='grey93',text ="ID")
            self.data1Label11.place(x=10,y=185)
            
            self.data1Label2 = tk.Label(self.page1, bg='grey93',text =(self.name[self.checkflag]))
            self.data1Label2.place(x=60,y=215)
            self.data1Label12 = tk.Label(self.page1, bg='grey93',text ="Product name")
            self.data1Label12.place(x=60,y=185)
            
            self.data1Label3 = tk.Label(self.page1, bg='grey93',text =(self.brand[self.checkflag]))
            self.data1Label3.place(x=170,y=215)
            self.data1Label13 = tk.Label(self.page1, bg='grey93',text ="Brand")
            self.data1Label13.place(x=170,y=185)            
            
            self.data1Label4 = tk.Label(self.page1, bg='grey93',text =(self.type[self.checkflag]))
            self.data1Label4.place(x=220,y=215)
            self.data1Label14 = tk.Label(self.page1, bg='grey93',text ="Type")
            self.data1Label14.place(x=220,y=185)        
            
            self.data1Label5 = tk.Label(self.page1, bg='grey93',text =(self.Rom[self.checkflag]))
            self.data1Label5.place(x=370,y=215)
            self.data1Label15 = tk.Label(self.page1, bg='grey93',text ="Rom")
            self.data1Label15.place(x=370,y=185)
            
            self.data1Label6 = tk.Label(self.page1, bg='grey93',text =(self.price[self.checkflag]))
            self.data1Label6.place(x=420,y=215)
            self.data1Label16 = tk.Label(self.page1, bg='grey93',text ="Price")
            self.data1Label16.place(x=420,y=185)            
            
            self.data1Label7 = tk.Label(self.page1, bg='grey93',text =(self.stock[self.checkflag]))
            self.data1Label7.place(x=480,y=215)
            self.data1Label17 = tk.Label(self.page1, bg='grey93',text ="Stock")
            self.data1Label17.place(x=480,y=185)
                    
    def deldata(self):
        
        connection = pymysql.connect(host='localhost', user='root', password='', db='pos')
        
        try:
   
            with connection.cursor() as cursor:
        
                sql = "DELETE FROM products WHERE pd_ID = '"+self.delEntry2.get()+"'"
                
                cursor.execute(sql)
                
                connection.commit()

        finally:
    
            connection.close()  
            
        self.data1Label17 = tk.Label(self.page3, bg='grey93',text ="Delete success!!!")
        self.data1Label17.place(x=5,y=220)           
    
    def updateProduct(self):
        
        self.ID, self.name, self.brand, self.type, self.Rom, self.price, self.stock = [], [], [], [], [], [], []
        connection = pymysql.connect(host='localhost', user='root', password='', db='pos')
        
        try:
   
            with connection.cursor() as cursor:
        
                sql = "SELECT * FROM `products` "
                
                cursor.execute(sql)

                print()
 
            for row in cursor:
                self.ID.append(row[0])
                self.name.append(row[1])     
                self.brand.append(row[2])
                self.type.append(row[3])
                self.Rom.append(row[4])
                self.price.append(row[5])
                self.stock.append(row[6])
        finally:
    
            connection.close()
        
        a = 0
        
        test = self.updateOption1.get()
        
        if (test == "product ID"):
            if(self.updateEntry2.get() == self.updateEntry6.get()):
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = '                                                                                                    ')
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = 'This ID is the same!! Please enter another ID if update are needed!!')
                self.warnLabel1.place(x = 5,y = 310)
            test1 = 'pd_ID'
            a = 1
        
        elif (test == "Product name"):
            if(self.updateEntry6.get() == self.name[self.checkflag]):
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = '                                                                                                    ')
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = 'This product name is the same!! Please enter another product name if update are needed!!')
                self.warnLabel1.place(x = 5,y = 310)
            test1 = 'pd_Name'
            a = 1
            
        elif (test == "Brand"):
            if(self.updateEntry6.get() == self.brand[self.checkflag]):
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = '                                                                                                    ')
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = 'This brand is the same!! Please enter another brand if update are needed!!')
                self.warnLabel1.place(x = 5,y = 310)
            test1 = 'pd_Brand'
            a = 1
            
        elif (test == "Type"):
            if(self.updateEntry6.get() == self.type[self.checkflag]):
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = '                                                                                                    ')
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = 'This product type is the same!! Please enter another product type if update are needed!!')
                self.warnLabel1.place(x = 5,y = 310)
            test1 = 'pd_Type'
            a = 1
            
        elif (test == "Rom"):
            if(self.updateEntry6.get() == self.Rom[self.checkflag]):
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = '                                                                                                    ')
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = 'The size of Rom of this product is the same!! Please enter another size of Rom if update are needed!!')
                self.warnLabel1.place(x = 5,y = 310)
            test1 = 'pd_Rom(GB)'
            a = 1
            
        elif (test == "Price"):
            if(self.updateEntry6.get() == self.price[self.checkflag]):
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = '                                                                                                    ')
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = 'This price is still the same!! Please enter another price if update are needed!!')
                self.warnLabel1.place(x = 5,y = 310) 
            test1 = 'pd_Price($HKD)'
            a = 1
            
        elif (test == "Stock"):
            if(self.updateEntry6.get() == self.stock[self.checkflag]):
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = '                                                                                                    ')
                self.warnLabel1 = tk.Label(self.page2, bg='grey93',text = 'This number of stock is the same!! Please enter another ID if update are needed!!')
                self.warnLabel1.place(x = 5,y = 310) 
            test1 = 'pd_Stock'
            a = 1
                       
        else:
            a = 1
            
             
        if a == 1:   
            connection = pymysql.connect(host='localhost', user='root', password='', db='pos')
        
            try:
   
                with connection.cursor() as cursor: 
                    
                    sql = "UPDATE products SET "+test1+" = '"+self.updateEntry6.get()+"' WHERE pd_ID = '"+self.updateEntry2.get()+"'"
                
                    cursor.execute(sql)
                
                    connection.commit()

            finally:
                a = 0
                connection.close()
                        
    def check_products(self):

        self.ID, self.name, self.brand, self.type, self.Rom, self.price, self.stock = [], [], [], [], [], [], []
        connection = pymysql.connect(host='localhost', user='root', password='', db='pos')
 
        try:
   
            with connection.cursor() as cursor:
        
                sql = "SELECT * FROM `products` "
                
                cursor.execute(sql)

                print()
 
            for row in cursor:
                self.ID.append(row[0])
                self.name.append(row[1])     
                self.brand.append(row[2])
                self.type.append(row[3])
                self.Rom.append(row[4])
                self.price.append(row[5])
                self.stock.append(row[6])
        finally:
    
            connection.close()

        
        type1 = self.checkOption1.get()
        h = 1
        if (type1 == 'product ID'):
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=5,y=130)
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=5,y=145)
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=5,y=160)
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=10,y=215)
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=10,y=185)
            self.checklabel = tk.Label(self.page1,text = 'The ID of the product:')
            self.checklabel.place(x=5,y=130)
            self.checkentry = tk.Entry(self.page1,width= 30)
            self.checkentry.place(x=5, y=160)
            
            self.checkenter=tk.Button(self.page1, text='Enter', \
                                      command=self.showdata1)
            self.checkenter.place(x = 250, y = 155)
            self.checkenter.config(state=NORMAL)
                        
        if (type1 == 'Product name'):
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=5,y=130)
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=5,y=145)
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=5,y=160)
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=10,y=215)
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=10,y=185)
            self.checklabel1 = tk.Label(self.page1,text = 'The name of the product:')
            self.checklabel1.place(x=5,y=130)
            self.checkentry = tk.Entry(self.page1,width= 30)
            self.checkentry.place(x=5, y=160)
        
            self.checkenter=tk.Button(self.page1, text='Enter', 
                                      command=self.showdata1)
            self.checkenter.place(x = 250, y = 155)
            self.checkenter.config(state=NORMAL)
            
        if (type1 == 'Overall'):       
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=5,y=130)
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=5,y=145)
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=5,y=160)
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=10,y=215)
            self.clearlabel = tk.Label(self.page1,text = '                                                                                                                                  ')
            self.clearlabel.place(x=10,y=185)
            if (h == 1):            
                self.editArea = tkst.ScrolledText(self.page1,width=40,height=20)
                self.editArea.pack(fill="x", expand=True) 
                self.editArea.tag_configure("b", justify="right")
            self.editArea.insert(tk.INSERT,('%-15s%-20s%-7s%-12s%-8s%-10s%-10s\n'%
                                            ('Product ID','Product Name','Brand','Type','Rom','Price','Stock')))
            self.editArea.insert(tk.INSERT,'-'*80+'\n') 
            line = len(self.ID)
            a = 0
            while a != line:
                self.editArea.insert(tk.INSERT,('%-15s%-20s%-7s%7s%5s%10s%10s\n'%   
                                   (self.ID[a],self.name[a],self.brand[a],self.type[a],self.Rom[a],self.price[a],self.stock[a])))
                a = a + 1

            self.editArea.config(state = DISABLED)
            h = 0  



    def new_products(self):
        
        self.ID, self.name, self.brand, self.type, self.Rom, self.price, self.stock = [], [], [], [], [], [], []
        connection = pymysql.connect(host='localhost', user='root', password='', db='pos')
 
        try:
   
            with connection.cursor() as cursor:
        
                sql = "SELECT * FROM `products` "
                
                cursor.execute(sql)

                print()
 
            for row in cursor:
                self.ID.append(row[0])
                self.name.append(row[1])     
                self.brand.append(row[2])
                self.type.append(row[3])
                self.Rom.append(row[4])
                self.price.append(row[5])
                self.stock.append(row[6])
        finally:
    
            connection.close()
            
        self.IDlabel = tk.Label(self.root,text = 'The ID of new product:')
        self.IDlabel.place(x=5,y=30)
        self.IDentry = tk.Entry(self.root,width= 70)
        self.IDentry.place(x=5, y=50)
        
        self.namelabel = tk.Label(self.root,text = 'The name of new product:')
        self.namelabel.place(x = 5,y = 80)
        self.nameentry = tk.Entry(self.root,width= 70)
        self.nameentry.place(x = 5, y = 100) 

        self.brandlabel = tk.Label(self.root,text = 'The brand of new product:')
        self.brandlabel.place(x = 5,y = 130)
        self.brandentry = tk.Entry(self.root,width= 70)
        self.brandentry.place(x = 5, y = 150)
        
        self.typelabel = tk.Label(self.root,text = 'The type of new product:')
        self.typelabel.place(x = 5,y = 180)
        self.typeentry = tk.Entry(self.root,width= 70)
        self.typeentry.place(x = 5, y = 200)
        
        self.Romlabel = tk.Label(self.root,text = 'The Rom of new product:')
        self.Romlabel.place(x = 5,y = 230)
        self.Romentry = tk.Entry(self.root,width= 70)
        self.Romentry.place(x = 5, y = 250)

        self.pricelabel = tk.Label(self.root,text = 'The price of new product:')
        self.pricelabel.place(x = 5,y = 280)
        self.priceentry = tk.Entry(self.root,width= 70)
        self.priceentry.place(x = 5, y = 300) 

        self.stocklabel = tk.Label(self.root,text = 'The stock of new product:')
        self.stocklabel.place(x = 5,y = 330)
        self.stockentry = tk.Entry(self.root,width= 70)
        self.stockentry.place(x = 5, y = 350)
        
        self.smt = tk.Button(self.root, text='Enter', \
                              command=self.check_insert)
        self.smt.place(x=10,y=370)                    
        
 



def main():
    root = tk.Tk()
    Login(root)
    root.mainloop()
    
def main1():
    print(l)
    if l == 1:
        root = tk.Tk()
        menu(root)
        root.mainloop()
        
if __name__ == '__main__':
    main()
    main1()
        
        
