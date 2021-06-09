from database import Database
from connection import connect



class MarkSheet:
    """this class will produce marksheet of given student_id"""
    def __init__(self,student_id):
        self.__student_id =student_id


    def set_student_id(self,student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id
        

    def info(self):
        try:
            """main method for prinitng the marksheet"""
            print("\n")
            attribute_list =['NAME','student_id','branch']
            for i in attribute_list:
                print(f"{i.upper()}:  ",end="")
                sql=f"select {i} from students where student_id= %s"
                val=[self.get_student_id()]
                data=Database(sql,val)
                Que=(data.query_select_one())
                str1 = ''.join(Que)
                print(str1)
            self.marks() 
        except TypeError:
            print("Something went wrong")   

    def marks(self):
        #for marks 
        print("\n")    
        sql=f"select Subject_id ,Marks,Out_of_marks,Grade from marks where student_id= '{self.get_student_id()}'"
        print("SubjectId      Marks      Out of marks       Grade")
     
        Que=(Database.query_show(sql))
        for i in range(len(Que)):
            print(""+(Que[i][0])+"\t\t"+str((Que[i][1]))+"\t\t" +str((Que[i][2]))+"\t\t"+(Que[i][3]))
        self.percentage()

    def percentage(self):
        #for percentage and total
        sql=f"select (sum(marks)) , sum(out_of_marks)  ,((sum(marks)/sum(out_of_marks))*100) from marks where student_id= '{self.get_student_id()}' ;"
        Que=Database.query_show(sql)
        print("Total"+"           "+str(Que[0][0])+"\t\t"+str(Que[0][1])+"\t\t"+str(round((Que[0][2]),2))+" %")
        print("\n")


        
        

