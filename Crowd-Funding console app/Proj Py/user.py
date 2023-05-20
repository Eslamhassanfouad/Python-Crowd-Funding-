from project import projList
import re
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="root",database="test")
mycursor = mydb.cursor()


class user:
    
    @staticmethod    
    def registeration():
        
        while True:
            name_regex='^[A-Za-z]+(?:\s[A-Za-z]+)*$'
            f_name=input("please enter your first name : ")
        
            if (re.search(name_regex,f_name)):
                break
            else:
                print("fname entered is not a string")
                
        while True:
            name_regex='^[A-Za-z]+(?:\s[A-Za-z]+)*$'
            l_name=input("please enter your last name : ")
                    
            if (re.match(name_regex,l_name)):
                
                break
                
            else:
                print("lname entered is not a string") 
                 
                      
        while True:
            regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
            email=input("please enter your email: ")
                
            if(re.search(regex,email)):
                #to insert a new record in test database
                mycursor.execute(f"SELECT * FROM user WHERE email = '{email}'")
                myresult = mycursor.fetchall()
                if myresult:
                    print('Email already exists')
                    continue
                
                else:
                    break
                    
                    
                        
                        
            else:
                print("please enter valid email")
        while True:
            password=input("please enter your password : ")
            password_conf=input("please confirm your password : ")
            if (password_conf==password):
                break
            else:
                print("not matching passwords")
                            
        while True:
            mobile_regex = '^01[0125][0-9]{8}$'
            mobile=input("please enter your phonr number:  ")
                        
            if (re.search(mobile_regex,mobile)):
                
                break
            else:
                print("please enter valid phone number")
                
        sql = "INSERT INTO user (fname, lname, email, pass, mobile) VALUES (%s, %s, %s, %s, %s)"
        val = (f_name, l_name,email, password, mobile) 
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        print("registeration done successfully =)")
        
     
        
    def login(self):    
        self.logEmail=input("please enter your email: ")          
        self.logPassword=input("please enter your password : ")
        login=False
    
        mycursor.execute(f"SELECT * FROM user WHERE email = '{self.logEmail}'")
        myresult = mycursor.fetchall()
        for x in myresult:
            if self.logEmail==x[2]:
                mycursor.execute(f"SELECT * FROM user WHERE pass = '{self.logPassword}'")
                myresult = mycursor.fetchall()
                for y in myresult:
                    if y[3]==self.logPassword:
                            print(f"Your User info is {x}")
                            print('You have successfully logged in')
                            login=True
                            print('-'*50)
                            projList(self.logEmail)                              
        if not login: 
            print('Invalid Email or Password')

while True:
    user1=user()  
    print('1) Registration')    
    print('2) Login')
    print('3) Exit')
    choice=input('Please enter your choice: ')
    if choice=='1':
        user1.registeration()
    elif choice=='2':
        user1.login()
    elif choice=='3':
        break
    else:
        print('invalid option')
        
            
 