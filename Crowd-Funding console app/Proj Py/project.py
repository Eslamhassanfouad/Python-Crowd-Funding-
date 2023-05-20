# from user import user
import re
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="root",database="test")
mycursor = mydb.cursor()




class project:
    
    @staticmethod      
    def create(email):
        while True:
            title_regex='^[A-Za-z]+(?:\s[A-Za-z]+)*$' 
            title=input('Please enter the title: ')
            if (re.search(title_regex,title)):
                break
            else:
                print("title entered is not a string")
        while True:
            target_regex='^[0-9]+$'
            target=input('Please enter the total target: ')
            if (re.search(target_regex,target)):
                break
            else:
                print('Target is only numbers')
        while True:
            date_regex='\d{4}-\d{2}-\d{2}'
            
            startDate=input('Please enter the startDate as YYYY-MM-DD: ')
            endtDate=input('Please enter the endtDate as YYYY-MM-DD: ')
            if (re.search(date_regex,startDate)):
                #to insert a new record in test databasesql 
                sql= "INSERT INTO proj (title, email, target, startDate, endDate) VALUES (%s, %s, %s, %s, %s)"
                val = (title, email ,target, startDate, endtDate) 
                print(val)
                mycursor.execute(sql, val)

                mydb.commit()

                print(mycursor.rowcount, "record inserted.")

                break
            else:
                print('Please enter date in the right format')
            
         
    def view(self):
        
        Vquery = " SELECT * FROM PROJ"
        mycursor.execute(Vquery)
        rows=mycursor.fetchall()
        column_names = [i[0] for i in mycursor.description] #lamda expression ;)
        print(column_names) 
        print(rows)
    
        
    @staticmethod        
    def edit(email):
        print('1) Edit Title\n2) Edit target\n3) Edit EndDate')
        choiceEdit=input('Please enter Edit Option: ')
        if choiceEdit == '1':
            editTitle = input('Please enter the new title: ')
            oldTitle = f"SELECT title FROM proj WHERE email='{email}'"
            mycursor.execute(oldTitle)
            oldTitle = mycursor.fetchone()[0]
            newTitle = f"UPDATE proj SET title='{editTitle}' WHERE email='{email}'"
            mycursor.execute(newTitle)
            mydb.commit()
            print(f"You have changed your title from {oldTitle} to {editTitle}")
            record = f"SELECT * FROM proj WHERE email='{email}'"
            mycursor.execute(record)
            print(f"Your new info is {mycursor.fetchall()}")
            
            
        elif choiceEdit == '2':
            editTarget = input('Please enter the new target: ')
            oldTarget = f"SELECT target FROM proj WHERE email='{email}'"
            mycursor.execute(oldTarget)
            oldTarget = mycursor.fetchone()[0]
            newTarget = "UPDATE proj SET target = %s WHERE email = %s"
            mycursor.execute(newTarget, (int(editTarget), email))
            mydb.commit()
            print(f"You have changed your target from {oldTarget} to {editTarget}")
            record = f"SELECT * FROM proj WHERE email='{email}'"
            mycursor.execute(record)
            print(f"Your new info is {mycursor.fetchall()}")
            
        elif choiceEdit == '3':
            editDate = input('Please enter the new endDate with Format as in ex: 2022-03-14: ')
            oldDate = f"SELECT endDate FROM proj WHERE email='{email}'"
            mycursor.execute(oldDate)
            oldDate = mycursor.fetchone()[0]
            newDate = "UPDATE proj SET endDate = %s WHERE email = %s"
            mycursor.execute(newDate, (editDate, email))
            mydb.commit()
            print(f"You have changed your endDate from {oldDate} to {editDate}")
            record = f"SELECT * FROM proj WHERE email='{email}'"
            mycursor.execute(record)
            print(f"Your new info is {mycursor.fetchall()}")
        else:
            print('invalid choice')
    @staticmethod
    def donate(email):
        while True:
            donate_regex='^[0-9]+$'
            donate=int(input('Please enter the amount you want to donate: '))
            if (re.search(donate_regex,str(donate))):
                target_query = f"SELECT target FROM proj WHERE email='{email}'"
                mycursor.execute(target_query)
                target = int(mycursor.fetchone()[0])
                if target >= donate:
                    new_target = target - donate
                    amount_query = f"UPDATE proj SET target='{new_target}' WHERE email='{email}'"
                    mycursor.execute(amount_query)
                    mydb.commit()
                    print(f"The remaining target after your donation is: {new_target}")
                    break
                elif target==0:
                    print('We have achieved our target, Thank You!')
                    break
                else:
                    print('The amount donated is more than our target, You are a Generous person!')
            else:
                print('your input is not a number')
                    
                
            
        
    @staticmethod
    def delete(email):
        while True:
            title_regex='^[A-Za-z]+(?:\s[A-Za-z]+)*$' 
            delete=input('Enter the title of the project you want to delete: ')
            if (re.search(title_regex,delete)):
                dbmail=mycursor.execute(f"SELECT email FROM proj WHERE title='{delete}'")
                title = mycursor.fetchone()
                
                
                if(email==dbmail):
                    mycursor.execute(f"SELECT * FROM proj WHERE title='{delete}'")
                    title = mycursor.fetchone()
                    if title:                   
                        mycursor.execute(f"DELETE FROM proj WHERE title='{delete}'")
                        mydb.commit()
                        print(f"You have deleted project {delete}")
                        break
                    else:
                        print(f"There is no project with the name: {delete}")
                else:
                    print('You are not the owner of the project')
                
        
        
    @staticmethod
    def search(email):
        while True:
            title_regex='^[A-Za-z]+(?:\s[A-Za-z]+)*$' 
            search=input('Enter the title of the project you want to search: ')
            if (re.search(title_regex,search)):
                mycursor.execute(f"SELECT * FROM proj WHERE title='{search}'")
                title = mycursor.fetchone()
                if title:                   
                    mycursor.execute(f"SELECT * FROM proj WHERE title='{search}'")
                    result = mycursor.fetchone()
                    mydb.commit()
                    print(f"Here is the project you are searching for: {result}")
                    break
                else:
                    print(f"There is no project with the name: {search}")
    
    
# it is a caller function same level with the class project to call the inside functions with email passed to it as it is my primary key    
def projList(email):
    while True:
        project1=project()
        print('1) Create project\n2) View Project\n3) Edit Project\n4) Donate\n5) Delete Project\n6) Search For a Project')
        choiceProj=input('Please Enter Your Choice:  ')
        if choiceProj=='1':
            project1.create(email)
        elif choiceProj=='2':
            project1.view()
        elif choiceProj=='3':
            project1.edit(email)
        elif choiceProj=='4':
            project1.donate(email)
        elif choiceProj=='5':
            project1.delete(email)
        elif choiceProj=='6':
            project1.search(email)
        else:
            print('invalid option') 
            
            

   
    
        
        
    
    
    #_________________________________________________________________________________________________#
    # #LOGIN
    #     user1=project()
    #     user1.login()

   
#____________________________________________________________________________________________________________#
#PROJECT CREATION

# project1=project()
# project1.create()
