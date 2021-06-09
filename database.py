from connection import connect


class Database:

    mycursor =connect.cursor()         #class attribute mycursor     
    """database(query,list_of_values) \n
    this class is use for executing given query from the given condition 
        this will take two inputs
        1.query
        2.list of values
        
        """
    def __init__(self,query,list_of_values):
        self.query=query
        self.list_of_values=list_of_values


    
    def query_insert(self):  #for insert query
        self.mycursor.executemany(self.query,self.list_of_values)
        connect.commit()
        

    @classmethod
    def query_show(self,query):             #for show query
        self.mycursor.execute(query)              
        result=self.mycursor.fetchall()
        return result


    def query_update(self):                     #for update query
        self.mycursor.executemany(self.query,self.list_of_values)
        connect.commit()
        print(self.mycursor.rowcount, "records affected")



    def query_delete(self):                     #for delete query
        self.mycursor.executemany(self.query,self.list_of_values)                    
        connect.commit()
        print((self.mycursor.rowcount), "record(s) deleted")



    def query_select_one(self):                 #for select one query
        self.mycursor.execute(self.query,self.list_of_values)
        result=self.mycursor.fetchall()
        for x in result:
            return(x)



    @classmethod
    def update(self,query):
        self.mycursor.execute(query)
        connect.commit()
        print(self.mycursor.rowcount, "records affected")


    @classmethod
    def query_show_simple(self,query):             #for show query
        self.mycursor.execute(query)              
        result=self.mycursor.fetchall()
        for x in result:
            print(x)


    def query_select_one_simple(self):                 #for select one query
        self.mycursor.execute(self.query,self.list_of_values)
        result=self.mycursor.fetchall()
        for x in result:
            print(x)

    

    