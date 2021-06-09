


class Details:
    """FOR TAKING INPUT FROM THE USER """

    def __init__(self):
        self.name=None
        self.student_id=None
        self.dob=None
        self.semester=None
        self.branch=None
        self.address=None
        self.roll_no=None
        self.email=None
        self.phone_no=None
        self.course_id=None
        self.course_name=None
        self.subject_code=None
        self.subject_name = None
        self.marks = None
        self.out_of_marks = None
        self.grade = None



    def set_name(self):                                                #FOR NAME
        
        self.name=input("enter  name\n")
        return self.name.upper()

    def get_name(self):
        return self.name
    
    def set_student_id(self):                                           #FOR STUDENT_ID
        self.student_id=input("enter  student_id\n")
        return self.student_id.upper()

    def get_student_id(self):
        return self.student_id.upper()

        
    def set_dob(self):                                                  #FOR DOB
        self.dob=input("enter the date of birth  in format 'yyyy-mm-dd'\n")
        return self.dob

    def set_semester(self):                                             #FOR SEMESTER
        while(True):
            self.semester=int(input("you are in which semester?\n"))
            if self.semester<=8:
                break
            else:
                print("enter valid semester ")

        return self.semester

    def get_semester(self):
        return self.semester

    def set_branch(self):                                               #FOR BRANCH
        while(True):                                                                  
            self.branch=(input("enter branch\n"))
            branch_list=['ETC','CSE','MECH','ELEC','ETRX','CIVIL','IT','AI']
            if self.branch.upper() in branch_list:
                
                break
            else:
                print("enter valid branch")
                print(" college have this branches only\n",branch_list)
                True
        return self.branch.upper()

    def get_branch(self):
        return self.branch.upper()
    
    def set_address(self):                                              #FOR ADDRESS
        """input the plotno, lane_name, area_name, city_name"""
        plot_no=input("enter the plot no\n")
        lane=input("enter the lane name\n")
        area=input("enter the area name \n")
        city=input("enter the city name \n")
        self.address=plot_no+", "+lane+", "+area+", "+city

        return self.address.upper()

    def set_rollno(self):                                               #FOR ROLLNO
        self.roll_no=int(input("enter the rollno\n"))
        return self.roll_no

    def set_email(self):                                                   #FOR EMAIL
        self.email=input("enter mail id\n")
        return self.email.upper()

    def set_phoneno(self):                                                  #FOR PHONE_NUMBER
        while(True):                                                                  
            self.phone_no=(int(input("enter phone number\n")))                   
            if len(str(self.phone_no))==10:
                break
            else:
                print("enter valid number")
                True
        return self.phone_no
    

#course class setter

    def set_course_id(self):                                            #for course-id
        
        self.course_id=str(self.get_semester())+"-"+self.get_branch()
        return self.course_id
        

    
    def set_course_name(self):                                          #for course name 
        branch=['ETC','CSE','MECH','ELEC','ETRX','CIVIL','IT','AI']
        course_name=["Electronics and Telecommunication","Computer Science","Mechanical","Electrical","Electronics","Civil","Information Technology","Artificical Intelligence"]
        for i in range(len(branch)):
            if self.get_branch()==branch[i]:
                    self.course_name=course_name[i]+" Engineering"
                    break
        return self.course_name



#subject class setter

    def set_subject_code(self):
        subject = input("enter the code of subject\n")
        
        self.subject_code =subject.upper()

        return self.subject_code

    def set_subject_name(self):
        subject_name = input("enter the name of subject\n")
        self.subject_name = subject_name.upper()

        return self.subject_name

#marks class setter
    def set_marks(self):
        while(True):
            mark=int(input("enter the marks of the student\n"))
            self.marks= mark
            if mark>0 and mark<=50:
                    if mark>40 and mark<=50:
                        self.grade = 'A'
                    elif mark>30 and mark<=40:
                        self.grade = 'B'
                    elif mark>20 and mark<=30:
                        self.grade = 'C'
                    elif mark>10 and mark<=20:
                        self.grade = 'D'
                    else:
                        self.grade = 'E'
                    break
            else:
                print("entered incorret marks ,please input valid value",end=" ")
                True

        return self.marks

    def set_grade(self):
        return self.grade

    def set_out_of_marks(self):
        mark=int(input("enter the out of marks\n"))
        self.out_of_marks= mark
        return self.out_of_marks

    

    
