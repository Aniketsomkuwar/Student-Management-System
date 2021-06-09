from database import Database
from connection import connect


class Mark:
    def __init__(self,student_id,subject_id,marks,out_of_marks,grade):
        self.__student_id =student_id
        self.__subject_id =subject_id
        self.__marks = marks
        self.__out_of_marks = out_of_marks
        self.__grade = grade

    def get_student_id(self):
        return self.__student_id

    def get_subject_id(self):
        return self.__subject_id

    def set_marks(self,marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_out_of_marks(self,out_of_marks=50):
        self.__out_of_marks = out_of_marks
        

    def get_out_of_marks(self):
        return self.__out_of_marks 

    def set_grade(self,grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def add_marks(self):
                    
        sql = "INSERT INTO marks VALUES (%s,%s,%s,%s,%s)"
        val = [
            (self.get_student_id(),self.get_subject_id(),self.get_marks(),self.get_out_of_marks(),self.get_grade())
        ]
        data=Database(sql,val)
        data.query_insert()


    def update_marks(self):
        sql=f"update marks set marks =  {self.get_marks()}, grade= '{self.get_grade()}'  where student_id = '{self.get_student_id()}' and subject_id ='{self.get_subject_id()}';  "
        Database.update(sql)

  
