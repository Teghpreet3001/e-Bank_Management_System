# e-Bank_Management_System

e-Bank Management System is a comphrehensive Python-Based GUI-Prototype Project that enables a user to experience basic Bank Functions like Login and Registration and Complex Bank Functions like Money Deposit and Withdrawl. Python Programming Language (Version-3.7 and IDLE-Jupyter Notebook) and its built in libraries like pymysql (Database Management)and Tkinter (GUI Development).The project also explores MySQL through phpMyAdmin (Server-127.0.0.1) and uses a subset of queries to work in between Python and MySQL softwares. Some of its features are —

Login: The Login form is a User friendly interface that allows an existing user to login to their account, by entering their email id and password. Incomplete Details and Non-Existing users are prompted by appropriate linking to concerned database and are barged from entering the system further.  

Registration: The Registration form is a User friendly interface that allows an new user to register with their account, by entering their details and confirming password. Incomplete Details and mismatched passwords are prompted by appropriate linking to concerned database are barged from entering the system further.

e-Bank: On successful registration or login through the respective interface, the user can debit oe credit the money from their bank accounts similar to an ATM or e-Banking System. Various options present are Deposit, Withdrawl, Check Balance and Change Password. All the transactions made are also updated in the RDBMS by appropriate linking to concerned database. 

RDBMS: Using the XAMPP Control Panel (Version-3.3.0), we hAave created a table 'registerform' in the database 'register' using MySQL through phpMyAdmin (Server-127.0.0.1). The columns along with their datatypes and field-lengths are id (Primary) [int(15)], fname [varchar(15)], lname [varchar(15)], mail [varchar(30)], pass [varchar(30)] and amount [int(50)]. The default value for amount is 0 and gets updated when a user makes a transaction. 

Libraries: We have used tkinter Python Library for presentable/attractive GUI developement. Alongside using tkinter options like Frame, Buttons, Labels, Headings and Entries, we use used the keyword 'self' with all functions to avoid the attribute error from occuring. To move from interface to another, we have used the place_forget() function. 
