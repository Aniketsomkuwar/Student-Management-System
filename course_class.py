from database import Database
from connection import connect



class Course:
    """class for course"""
    def __init__(self,student_id,course_id,course_name):
        self.__course_name=course_name
        self.__course_id=course_id
        self.__student_id=student_id

    def set_course_name(self,course_name):
        self.__course_name=course_name
    
    def get_course_name(self):
        return self.__course_name

    def set_course_id(self,course_id):
        self.__course_id=course_id

    def get_course_id(self):
        return self.__course_id
    
    def set_student_id(self,new_id):
        self.__student_id=new_id

    def get_student_id(self):
        return self.__student_id

    def course_detail(self):
        sql = "INSERT INTO course_data VALUES (%s,%s,%s)"
        val = [
            (self.get_course_id(),self.get_course_name(),self.get_student_id())            
        ]
        data=Database(sql,val)
        data.query_insert()