import datetime
from database import Database
from connection import connect
from prettytable import PrettyTable

"""-----------------------------------------Student_class------------------------------------------------"""
class Students:
    """ this class is used to maintain the data of students""" 
    def __init__(self,name,student_id,dob,semester,branch,address,rollno,email,phone_no):
        self.__name=name
        self.__student_id=student_id
        self.__dob=dob
        self.__semester=semester
        self.__branch=branch
        self.__address=address
        self.__rollno=rollno
        self.__email=email
        self.__phone_no=phone_no
    ##############------------getter setter methods-------------##############

    #this function is used to correct the name if any corrections are there
    def set_name(self,correct_name):       
        self.__name=correct_name
      
    def get_name(self):
        return self.__name
    
    #function for editing student_id
    def set_student_id(self,new_id):
        self.__student_id=new_id

    def get_student_id(self):
        return self.__student_id

    #function for making correction in DOB
    def set_dob(self,dob):
        self.__dob=dob
    
    def get_dob(self):
        return self.__dob

    #function for pramoting student to next semester
    def set_semester(self,new_semester):
        self.__semester=new_semester

    def get_semester(self):
        return self.__semester

    #fucntion for changing branch of student 
    def set_branch(self,_new_branch):
        self.__branch=_new_branch

    def get_branch(self):
        return self.__branch.upper()   #because all branches are set in uppercase

    #fucntion for setting new_address
    def set_address(self,new_address):
        self.__address=new_address
    
    def get_address(self):
        return self.__address

    #function for setting the roll no of students
    def set_roll(self,new_rollno):
        self.__rollno=new_rollno

    def get_roll(self):
        return self.__rollno

    #fucntion for setting new_phone_number
    def set_phone(self,new_phone_no):
        self.__phone_no=new_phone_no

    def get_phone(self):
        return self.__phone_no

    #function for setting new_email_id
    def set_email(self,new_email):
        self.__email=new_email
        
    def get_email(self):
        return self.__email





    ##############------------------insert method------------------################

    def insert(self):
        """inject the data into the DB-----for inserting new data into the database"""

        
        sql = "INSERT INTO students VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = [
            (self.get_name(),
            self.get_student_id(),
            self.get_dob(),
            self.get_semester(),
            self.get_branch(),
            self.get_address(),
            self.get_roll(),
            self.get_email(),
            self.get_phone())            
        ]
        data=Database(sql,val)
        data.query_insert()




    
    ################-------------------show_method------------------###################
    @classmethod
    def show(cls):
        """show all the data in the DB"""
        sql="select * from students ORDER BY roll_no"
        data=Database.query_show(sql)
        mytable= PrettyTable(["NAME","STUDENT_ID","DOB","SEMESTER","BRANCH","ADDRESS","ROLLNO","EMAIL","PHONE_NO"])
        for i in range(len(data)):
            mytable.add_row([data[i][0],data[i][1],str(data[i][2]),str(data[i][3]),data[i][4],data[i][5],str(data[i][6]),data[i][7],data[i][8]])
        print(mytable)
       





    #################-------------------update_method------------------###################
    @classmethod
    def update(cls,student_id,value_to_be_replaced,replaced_value):
        """update the particular data of given student_id and save it into the database"""
        sql = (f"update students set {value_to_be_replaced}='{replaced_value}'  where student_id='{student_id}'")         #write your update query
        Database.update(sql)
        




    #################------------------delete_method-------------------###############
    @classmethod
    def delete(cls,student_id):
        """ take the student_id of particular student whose data we want to remove"""

        sql = f"DELETE FROM students WHERE student_id='{student_id}'" 
        Database.update(sql)
 


        
    
    ###############-------------------select_one_method------------------#################
    @classmethod
    def select_one(cls,student_id):
        try:
            sql=f"select * from students where student_id= %s"
            val=[student_id]

            data=Database(sql,val)
            mytable= PrettyTable(["NAME","STUDENT_ID","DOB","SEMESTER","BRANCH","ADDRESS","ROLLNO","EMAIL","PHONE_NO"])
            value=data.query_select_one()
    
            mytable.add_row([value[0],value[1],str(value[2]),str(value[3]),value[4],value[5],str(value[6]),value[7],value[8]])
            print(mytable)
        except TypeError:
            print("Incorrect student_id ,Enter again")

