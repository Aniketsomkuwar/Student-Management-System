from student_class import Students
from input_class import Details
import connection
from course_class import Course
from subject_class import Subject
from  marks_class import Mark
from marksSheet_class import MarkSheet




output=Details()            #FOR CALLING INPUT FUNCTION FROM INPUT.PY


print("____________________________Welcome To Student Administration_____________________________")


while(True):
    print("\n CHOOSE THE OPERATION YOU WANT TO PERFORM")
    print("\n 1.READ/EDIT STUDENTS DETAIL")
    print("\n 2.EXAM DATA")
    print("\n 3.SUBJECTS")
    print("\n 4.EXIT")

    choice=int(input("\t"))
    if choice==1:
        while(True):
            print("\n CHOOSE THE OPERATION YOU WANT TO PERFORM")
            print("\n 1.SHOW STUDENTS")
            print("\n 2.SHOW ONE STUDENT")
            print("\n 3.INSERT STUDENT")
            print("\n 4.UPDATE STUDENT")
            print("\n 5.DELETE STUDENT")
            print("\n 6.BACK")


            choice=int(input("\t"))
            if choice==1:                     #THIS WILL SHOW THE WHOLE TABLE
                Students.show()                 

            elif choice==2:                               #THIS WILL SHOW THE PARTICULAR STUDENT BASED ON STUDENT_ID
                Students.select_one(output.set_student_id())                

            elif choice==3:#THIS WILL INSERT THE NEW STUDENT TO TABLE 

                enter=Students(output.set_name(),output.set_student_id(),output.set_dob(),output.set_semester(),output.set_branch(),output.set_address(),output.set_rollno(),output.set_email(),output.set_phoneno())
                enter.insert()
                auto_Course=Course(output.get_student_id(),output.set_course_id(),output.set_course_name())
                auto_Course.course_detail()


            elif choice==4:                                       #THIS WILL UPDATE THE PARTICULAR STUDENT DETAILS
                while(True):                                        
                    print("\n CHOOSE IN WHICH CATEGORY YOU WANT TO MAKE CHANGES")
                    print("\n 1.NAME")
                    print("\n 2.DOB")
                    print("\n 3.SEMESTER")
                    print("\n 4.BRANCH")
                    print("\n 5.ADDRESS")
                    print("\n 6.ROLL_NO")
                    print("\n 7.CELLPHONE")
                    print("\n 8.EMAIL")
                    print("\n 9.IF YOU FINISHED UPDATING DATA ENTER 0 AND EXIT.......")

                    info=int(input(">"))
                    if info==1:                                                               
                        Students.update(output.set_student_id(),"name",output.set_name())                #for  name
                    elif info==2:
                        Students.update(output.set_student_id(),"dob",output.set_dob())                 #for dob
                    elif info==3:
                        Students.update(output.set_student_id(),"semester",output.set_semester())           #for semester
                    elif info==4:
                        Students.update(output.set_student_id(),"branch",output.set_branch())           #for branch
                    elif info==5:
                        Students.update(output.set_student_id(),"address",output.set_address())             #for address
                    elif info==6:
                        Students.update(output.set_student_id(),"rollno",output.set_rollno())           #for roll_no
                    elif info==7:
                        Students.update(output.set_student_id(),"phone_no",output.set_phoneno())           #for phone_no
                    elif info==8:
                        Students.update(output.set_student_id(),"email",output.set_email())         #for email
                    else:
                        print("you chose to exit...")
                        break

            elif choice==5:                               #FOR DELETING THE PARTICULAR DATA FROM TABLE BASED ON STUDENT_ID
                Students.delete(output.set_student_id())

            else:
                break
    
    elif choice==2:
        while(True):
            print("\n CHOOSE THE OPERATION YOU WANT TO PERFORM")
            print("\n 1.ENTER MARKS")
            print("\n 2.EDIT MARKS")
            print("\n 3.MARKSHEET OF STUDENT")
            print("\n 4.BACK")

            choice=int(input("\t"))
            if choice==1:
                Subject.show_subjects()
                data = Mark(output.set_student_id(),output.set_subject_code(),output.set_marks(),output.set_out_of_marks(),output.set_grade())
                data.add_marks()
            elif choice==2: 
                Subject.show_subjects()
                data = Mark(output.set_student_id(),output.set_subject_code(),output.set_marks(),output.set_out_of_marks(),output.set_grade())
                data.update_marks()
            elif choice ==3:
                data= MarkSheet(output.set_student_id())
                data.info()
            else:
                break

    elif choice==3:
        while(True):
            print("\n CHOOSE THE OPERATION YOU WANT TO PERFORM")
            print("\n 1.ADD SUBJECTS")
            print("\n 2.SHOW SUBJECTS")
            print("\n 3.BACK ")
            choice=int(input("\t"))
            if choice==1:                    
                show = Subject(output.set_subject_code(),output.set_subject_name())
                show.add_subject()
    
            elif choice==2:
                Subject.show_subjects()

            else:
                break



    else:
        connection.close_connection()
        print("you chose to exit.......")
        break
    