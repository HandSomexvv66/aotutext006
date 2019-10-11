import pymysql
class mysql1:
    def connet_con(self):
        self.con = pymysql.Connect(host ='localhost',user ='root',password='root',database='books',autocommit=True)


    def connet_cousor(self):
        self.cousr = self.con.cursor()

    def close_con(self):
        self.con.close()
    def close_cousor(self):
        self.cousr.close()

    def excuse_sql(self,par1):
        self.cousr.execute("select * from t_book where id ={} ".format(par1))
        date = self.cousr.fetchone()
        print(date)
mql = mysql1()
mql.connet_con()
mql.connet_cousor()
mql.excuse_sql(3)
mql.close_cousor()
mql.connet_con()
