import sys
import psycopg2
import psycopg2.extras
import traceback

class crud_ops():

    def __init__(self, argv):
        self.method = argv[1]
        self.data = argv
        host = 'localhost'
        database = 'postgres'
        user = 'postgres'
        port='5433'
        password = '1234'
        self.conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=port)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def execute_query(self,sql,res_flag):
        self.cur.execute(sql)
        lst = []
        if res_flag:
            ans =self.cur.fetchall()
            if len(ans)>0:
                for row in ans:
                    rec = str(row[0]) + " " + str(row[1]) + " " + str(row[2])
                    lst.append(rec)
        self.conn.commit()
        return lst

    def create_data(self):
        id_data = self.data[2]
        name_data = self.data[3]
        age_data = self.data[4]
        if(len(self.select_op("id",id_data))>0 ):
            print("Data already exists in database")
            return 1
        try:
            createData = "INSERT INTO crud_db.crud_table(id,name,age) VALUES('"+id_data+"','"+name_data+"','"+age_data+"');"
            self.execute_query(createData, False)
            createData = "select * from crud_db.crud_table where id ='"+id_data+"';"
            res = self.execute_query(createData, True)
            print("Data Created: "+str(res[0]))

        except :
            print("Error while executing query")
            traceback.print_exc(limit=1)
            print("User could not be created")



    def get_all_data(self):
        getData = "SELECT * FROM crud_db.crud_table;"
        res = self.execute_query(getData, True)
        print("data is "+str(res))

    def select_op(self, col, val):
        getData = "SELECT * FROM crud_db.crud_table where "+col+" = '"+val+"';"
        res = self.execute_query(getData, True)
        return res
    def get_data(self):
        name_data = self.data[2]
        result_set = self.select_op("name",name_data)
        result = str(result_set[0]) if len(result_set)==1 else [str(x) for x in result_set]
        if len(result_set)>0:
            print("Data found: "+str(result))
        else:
            print("Data not found")


    def update_data(self):
        upd_name_data = self.data[2]
        id_data = self.data[3]
        name_data = self.data[4]
        age_data = self.data[5]
        updateData = "UPDATE crud_db.crud_table SET id='"+id_data+"' , name='"+name_data+"', age='"+age_data+"' WHERE name='"+upd_name_data+"';"
        self.execute_query(updateData, False)
        print("Data updated: "+str(self.select_op("name",name_data)[0]))


    def delete_data(self):
        name_data = self.data[2]
        res = self.select_op("name",name_data)
        deleteData = "DELETE FROM crud_db.crud_table WHERE name= '"+name_data+"';"
        self.execute_query(deleteData, False)
        print("Data deleted: "+str(res[0]))

    def run(self):
        if self.method == "get_data": self.get_data()
        if self.method == "get_all_data": self.get_all_data()
        if self.method == "delete_data": self.delete_data()
        if self.method == "create_data": self.create_data()
        if self.method == "update_data": self.update_data()


if __name__ == "__main__":
    c = crud_ops(sys.argv)
    c.run()