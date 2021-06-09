import mysql.connector
def connection():
    """for making connection between MySql and Python"""
    
    try:
        
        mydb =mysql.connector.connect(
            host="localhost",
            user="root",
            password="7350",
            database="student_Admin"
        )
        return mydb
            
    
    except mysql.connector.ProgrammingError :
        print("something went wrong\n")
        print("please Try Again\n")
        

connect=connection()                
       
def close_connection():
    """for disconnecting from DB"""
    print("your connection is closed")
    connect.close()
    





