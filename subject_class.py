from database import Database
from connection import connect
from prettytable import PrettyTable

class Subject:
    def __init__(self,subject_code,subject_name):
        self.__subject_code = subject_code
        self.__subject_name = subject_name



    def set_sub_code(self,subject_code):
        self.__subject_code = subject_code

    def get_sub_code(self):
        return self.__subject_code

    def set_sub_name(self,subject_name):
        self.__subject_name = subject_name

    def get_sub_name(self):
        return self.__subject_name

    def add_subject(self):
        

        sql = "INSERT INTO subject VALUES (%s,%s)"
        val = [
            (self.get_sub_code(),
        self.get_sub_name())
        ]
        data=Database(sql,val)
        data.query_insert()

    def delete_subject(self):

        
        sql = f"DELETE FROM course WHERE subject_id=%s" 
        val=[self.get_sub_name()]

        data=Database(sql,val)
        data.query_delete()


    @classmethod
    def show_subjects(self):
        sql="select * from subject"
        data=Database.query_show(sql)
        mytable= PrettyTable(["SUBJECT CODE","SUBJECT NAME"])
        for i in range(len(data)):
            mytable.add_row([data[i][0],data[i][1]])
        print(mytable)



