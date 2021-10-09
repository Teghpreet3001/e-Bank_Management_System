#!/usr/bin/env python
# coding: utf-8

# # e-Bank Management System using Python and MySQL

# e-Bank Management System is a comphrehensive Python-Based GUI-Prototype Project that enables a user to experience basic Bank Functions like Login and Registration and Complex Bank Functions like Money Deposit and Withdrawl. Python Programming Language (Version-3.7 and IDLE-Jupyter Notebook) and its built in libraries like pymysql (Database Management)and Tkinter (GUI Development).The project also explores MySQL through phpMyAdmin (Server-127.0.0.1) and uses a subset of queries to work in between Python and MySQL softwares.
# 
# Login: The Login form is a User friendly interface that allows an existing user to login to their account, by entering their email id and password. Incomplete Details and Non-Existing users are prompted by appropriate linking to concerned database. 
# 
# Registration: The Registration form is a User friendly interface that allows an new user to register with their account, by entering their details and confirming password. Incomplete Details and mismatched passwords are prompted by appropriate linking to concerned database. 
# 
# e-Bank: On successful registration or login through the respective interface, the user can debit oe credit the money from their bank accounts similar to an ATM or e-Banking System. Various options present are Deposit, Withdrawl, Check Balance and Change Password. All the transactions made are also updated in the RDBMS by appropriate linking to concerned database. 
# 
# RDBMS: Using the XAMPP Control Panel (Version-3.3.0), we hAave created a table 'registerform' in the database 'register' using MySQL through phpMyAdmin (Server-127.0.0.1). The columns along with their datatypes are id (Primary) [int(15)], fname [varchar(15)], lname [varchar(15)], mail [varchar(30)], pass [varchar(30)] and amount [int(50)]. The default value for amount is 0 and gets updated when a user makes a transaction. 
# 
# 

# In[2]:


pip install pymysql


# In[8]:


from tkinter import *
import pymysql
class register:
    def __init__(self):
        self.root = Tk()
        self.root.title('e-Bank Management Sysyem')
        
        self.root.geometry('700x500')
        self.root.resizable(False,False)
        self.root.configure(bg='#34a8eb')
        
        self.heading = Label(self.root, text='LOGIN FORM', font=('Times New Roman',40,'bold'),bg='#001f99',fg='#f7dc43')
        self.heading.place(x=0,y=30,relwidth=1)
        
        self.f1 = Frame(self.root, bg="#34a8eb")
        self.f1.place(x=0,y=100,relheight=1,relwidth=1)
        
        self.mail = Label(self.f1,text='Enter E-mail ID :',font=('Times New Roman',16,''),bg="#34a8eb",fg='black')
        self.mail.place(x=70,y=50)
        
        self.entermail = Entry(self.f1,bg="white",fg='black')
        self.entermail.place(x=240,y=50,height=35,width=400)
        
        self.password = Label(self.f1,text='Password :',font=('Times New Roman',16,''),bg="#34a8eb",fg='black')
        self.password.place(x=70,y=100)
        
        self.enterpass = Entry(self.f1,bg="white",fg='black')
        self.enterpass.place(x=240,y=100,height=35,width=400)
        
        self.b1 = Button(self.f1,text='Login',command = self.logfunc, fg='#044970',font=('Glacial Indiffernece',14,''),bg='#f7dc43')
        self.b1.place(x=70,y=150,width=570,height=35)
        
        self.registernow = Label(self.f1,text='Don\'t have an account? Register Now!',font=('Times New Roman',16,''), bg="#34a8eb",fg='black')
        self.registernow.place(x=70,y=200)
        
        self.b2 = Button(self.f1,text='Register',command = self.regfunc, fg='#044970',font=('Glacial Indiffernece',14,''),bg='#f7dc43')
        self.b2.place(x=70,y=250,width=570,height=35)
        
        self.root.mainloop()
        
    def logfunc(self):
        getmail = self.entermail.get()
        p1 = self.enterpass.get()
        try:
            mycon = pymysql.connect(host='localhost', user='root',password='', database='register')
            mycursor = mycon.cursor()
            mycursor.execute('select * from registerform where mail=%s',(getmail))
            row = mycursor.fetchone()
            if getmail == ''or p1=='':
                print('Please enter all fields')
                return
            elif row==None:
                print('No user with that Email exists!\n Please Create a New Acoount')
                return
            else:
                print('Login Successful!')
            mycon.close()
        except Exception as e:
            print('Error : ',e)
        
        self.heading.place_forget()
        self.mail.place_forget()
        self.entermail.place_forget()
        self.password.place_forget()
        self.enterpass.place_forget()
        self.b1.place_forget()
        self.registernow.place_forget()
        self.b2.place_forget()
        
        self.heading2 = Label(self.root, text='WELCOME TO E-BANK!', font=('Times New Roman',40,'bold'),bg='#001f99',fg='#fa9b1e')
        self.heading2.place(x=0,y=30,relwidth=1)
        
        self.option = Label(self.f1,text='Choose any one option from the following',font=('Times New Roman',20,''),bg="#34a8eb",fg='black')
        self.option.place(x=20,y=50,relwidth=1)
        
        self.withdrawl = Button(self.f1,command= self.withdraw,text='Withdrawl',font=('Times New Roman',20,''),bg="#ffbe69",fg='black')
        self.withdrawl.place(x=100,y=100,width=500)
        
        self.deposit = Button(self.f1,command = self.deposit,text='Deposit',font=('Times New Roman',20,''),bg="#ffbe69",fg='black')
        self.deposit.place(x=100,y=175,width=500)
        
        self.balance = Button(self.f1,command = self.balance,text='Balance',font=('Times New Roman',20,''),bg="#ffbe69",fg='black')
        self.balance.place(x=100,y=250,width=500)
        
        self.changepin = Button(self.f1,command= self.change,text='Change Pin',font=('Times New Roman',20,''),bg="#ffbe69",fg='black')
        self.changepin.place(x=100,y=325,width=500)
        
        self.exit = Button(self.f1,command=lambda:self.f1.place_forget(),text='Exit',font=('Times New Roman',20,''),bg="#ffbe69",fg='black')
        self.exit.place(x=100,y=400,width=500)
    
    def balance(self):
        getmail = self.entermail.get()
        p1 = self.enterpass.get()
        
        self.frame3=Frame(self.root,bg='#b3dafc')
        self.frame3.place(x=50,y=50,height=400,width=300)
        
        mycon=pymysql.connect(host='localhost',user='root',password='',database='register')
        mycursor=mycon.cursor()
        mycursor.execute('select * from registerform where mail=%s and pass=%s',(getmail,p1))
        row=mycursor.fetchone()
        
        self.baldisplay=Label(self.frame3,text=f'Your Balance is {row[5]}',font=('Times New Roman',12,''),bg='#b3dafc')
        self.baldisplay.place(x=100,y=100)
        
        self.b=Button(self.frame3,command=lambda:self.frame3.place_forget(),text='Go Back',bg='#eef7eb',fg='black')
        self.b.place(x=50,y=200,height=30,width=200)


    def deposit(self):
        def dep():
            getmail = self.entermail.get()
            p1 = self.enterpass.get()
            mycon=pymysql.connect(host='localhost',user='root',password='',database='register')
            mycursor=mycon.cursor()
            mycursor.execute('select * from registerform where mail=%s and pass=%s',(getmail,p1))
            row=mycursor.fetchone()
            print(row[5])
            bal=row[5] + int(self.amount.get())
            print(bal)
            mycursor.execute('update registerform set amount=%s where mail=%s and pass=%s',(bal,getmail,p1))
            mycon.commit()
            result=Label(self.frame4,text=f'Your Last Updated Balance is {bal}',font=('Times New Roman',12,''),bg='#b3dafc')
            result.place(x=50,y=250)
            mycon.close()
            
        self.frame4=Frame(self.root,bg='#b3dafc')
        self.frame4.place(x=50,y=50,height=400,width=300)
        
        self.text=Label(self.frame4,text='Enter the amount to deposit',font=('Times New Roman',12,''),fg='black',bg='#b3dafc')
        self.text.place(x=50,y=100)
        
        self.amount=Entry(self.frame4,bg='white',fg='black',bd=2)
        self.amount.place(x=50,y=150,height=25,width=200)
        
        self.button=Button(self.frame4,command=dep,text='Submit',font=('Times New Roman',12,''),bg='#eef7eb',fg='black')
        self.button.place(x=50,y=200,height=30,width=100)
        
        self.b=Button(self.frame4,command=lambda:self.frame4.place_forget(),text='Go Back',font=('Times New Roman',12,''),bg='#eef7eb',fg='black')
        self.b.place(x=50,y=300,height=30,width=100)
       
    def withdraw(self):
        self.frame5=Frame(self.root,bg='#b3dafc')
        self.frame5.place(x=50,y=50,height=400,width=300)
        
        self.text=Label(self.frame5,text='Enter the amount to withdraw',font=('Times New Roman',12,''),fg='black',bg='#b3dafc')
        self.text.place(x=50,y=100)
        
        self.wamount=Entry(self.frame5,bg='white',fg='black',bd=2)
        self.wamount.place(x=50,y=150,height=25,width=200)
        
        def amt():
            getmail = self.entermail.get()
            p1 = self.enterpass.get()
            mycon=pymysql.connect(host='localhost',user='root',password='',database='register')
            mycursor=mycon.cursor()
            mycursor.execute('select * from registerform where mail=%s and pass=%s',(getmail,p1))
            row=mycursor.fetchone()
            print(row[5])
            bal=row[5] - int(self.wamount.get())
            print(bal)
            mycursor.execute('update registerform set amount=%s where mail=%s and pass=%s',(bal,getmail,p1))
            mycon.commit()
            result=Label(self.frame5,text=f'Your Last Updated Balance is {bal}',font=('Times New Roman',12,''),bg='#b3dafc')
            result.place(x=50,y=250)
            mycon.close()
            
        self.button=Button(self.frame5,command=amt,text='Submit',font=('Times New Roman',12,''),bg='#eef7eb',fg='black')
        self.button.place(x=50,y=200,height=30,width=100)
        
        self.b=Button(self.frame5,command=lambda:self.frame5.place_forget(),text='Go Back',bg='#eef7eb',fg='black')
        self.b.place(x=50,y=300,height=30,width=100)

    def change(self):
        self.frame6=Frame(self.root,bg='#b3dafc')
        self.frame6.place(x=50,y=50,height=400,width=300)
        
        self.text=Label(self.frame6,text='Enter new PIN',font=('Times New Roman',12,''),fg='black',bg='#b3dafc')
        self.text.place(x=50,y=100)
        
        self.newpass=Entry(self.frame6,bg='white',fg='black',bd=2)
        self.newpass.place(x=50,y=150,height=25,width=200)
        
        def newpass():
            getmail = self.entermail.get()
            p1 = self.enterpass.get()
            p2 = self.newpass.get()
            mycon=pymysql.connect(host='localhost',user='root',password='',database='register')
            mycursor=mycon.cursor()
            mycursor.execute('update registerform set pass=%s where mail=%s and pass=%s',(p2,getmail,p1))
            row=mycursor.fetchone()
            baldisplay=Label(self.frame6,text='Your password is updated.',font=('Times New Roman',12,''),bg='#b3dafc')
            baldisplay.place(x=50,y=250)
            
        self.button=Button(self.frame6,command = newpass,text='Submit',font=('Times New Roman',12,''),bg='#eef7eb',fg='black')
        self.button.place(x=50,y=200,height=30,width=100)
        
        self.b=Button(self.frame6,command=lambda:self.frame6.place_forget(),text='Go Back',bg='#eef7eb',fg='black')
        self.b.place(x=50,y=300,height=30,width=100)
    
    def regfunc(self):
        self.heading.place_forget()
        self.entermail.place_forget()
        self.enterpass.place_forget()
        self.b1.place_forget()
        self.registernow.place_forget()
        self.b2.place_forget()
        
        self.heading2=Label(self.root,text='REGISTRATION FORM',font=('Times New Roman',40,'bold'),bg='#001f99',fg='#ff709b')
        self.heading2.place(x=0,y=30,relwidth=1)

        self.f1=Frame(self.root,bg="#34a8eb")
        self.f1.place(x=0,y=100,relheight=1,relwidth=1)

        self.entername=Label(self.f1,text='Name :',font=('Times New Roman',14,''),bg="#34a8eb",fg='black')
        self.entername.place(x=70,y=45)

        self.fnamelabel=Label(self.f1,text='first name:',font=('Times New Roman',10,''),bg="#dedede",fg='#787878')
        self.fnamelabel.place(x=240,y=20)

        self.lnamelabel=Label(self.f1,text='last name:',font=('Times New Roman',10,''),bg="#dedede",fg='#787878')
        self.lnamelabel.place(x=450,y=20)

        self.fname=Entry(self.f1,bg="white",fg='black')
        self.fname.place(x=240,y=40,height=35,width=200)

        self.lname=Entry(self.f1,bg="white",fg='black')
        self.lname.place(x=450,y=40,height=35,width=200)

        self.entermail2=Label(self.f1,text='Email :',font=('Times New Roman',14,''),bg="#34a8eb",fg='black')
        self.entermail2.place(x=70,y=85)

        self.mail=Entry(self.f1,bg="white",fg='black')
        self.mail.place(x=240,y=80,width=410,height=35)

        self.enterpass2=Label(self.f1,text='Password :',font=('Times New Roman',14,''),bg="#34a8eb",fg='black')
        self.enterpass2.place(x=70,y=145)

        self.password=Entry(self.f1,bg="white",fg='black')
        self.password.place(x=240,y=140,width=410,height=35)

        self.enterconfirm=Label(self.f1,text='Confirm Password :',font=('Times New Roman',14,''),bg="#34a8eb",fg='black')
        self.enterconfirm.place(x=70,y=185)

        self.password2=Entry(self.f1,bg="white",fg='black')
        self.password2.place(x=240,y=180,width=410,height=35)

        self.b3=Button(self.f1,command=self.create,text='Create Account',fg='#044970',font=('Glacial Indiffernece',12,''),bg='#faa7c0',bd=0)
        self.b3.place(x=70,y=220,width=600,height=35)

        self.b4=Button(self.f1,text='Already Have an Account? Login Here',fg='#044970',font=('Glacial Indiffernece',12,''),bg='#faa7c0',bd=0)
        self.b4.place(x=70,y=260,width=600,height=35)
        
        self.b5=Button(self.f1,text='Go Back',command=self.__init__,fg='#044970',font=('Glacial Indiffernece',12,''),bg='#faa7c0',bd=0)
        self.b5.place(x=70,y=300,width=600,height=35)
        
    def create(self):
        fn = self.fname.get()
        ln = self.lname.get()
        ml = self.mail.get()
        p1 = self.password.get()
        p2 = self.password2.get()
        if fn == '' or ln=='' or ml=='' or p1=='' or p2=='':
            print('Please enter all fields')
            return
        elif p1!=p2 :
            print('Passwords and Comfirm password do not match')
            return
        else:
            try:
                mycon=pymysql.connect(host='localhost',user='root',password='', database='register')
                mycursor = mycon.cursor()
                mycursor.execute('select * from registerform where mail=%s',(ml))
                row = mycursor.fetchone()
                if row==None:
                    mycursor.execute('insert into registerform(fname, lname, mail, pass) values(%s, %s, %s, %s)',(fn,ln,ml,p1))
                    mycon.commit()
                    print('Registration Successful')
                else:
                    print('User already exists:', row[1])
                mycon.close()
            except Exception as e:
                print('Error:',e)
ob=register()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




