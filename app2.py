from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")



@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      print('requesting from server...')
      try:
         print('inside try')
         f_name = request.form['f_name']
         l_name = request.form['l_name']
         Email = request.form['email']
         phone = request.form['phone']
         print('data collected')
#somehow this is getting skipped and only except is getting runn
         try:
             conn = sqlite3.connect("database1.db")
         except Error as e:
             print(e)
         print('database connected')
         cur = conn.cursor
         print('cursor created')
         sql_query = """INSERT INTO ContactS(f_name,l_name,email,phone) VALUES (?,?,?,?)"""
         print('ch1')
         data =(f_name,l_name,Email,phone)
         print('ch2')
         conn.execute(sql_query,data)
         print('data inserted')
#        i think we require to mention the data types in the sql statement INSERT, isn;t it
         conn.commit()
         #cur.commit()
         print('ch3')
         msg = "Record successfully added"
      except:
         conn.rollback()
         msg = "error in insert operation"
      finally:
         return render_template("submit1.html",msg = msg)
         conn.close()


@app.route('/dbselect')
def dbselect():
      print('in select')
      try:
         conn = sqlite3.connect("database1.db")
      except Error as e:
         print(e)
      print('database connected')
      conn.row_factory = sqlite3.Row
      query2 = """Select * from ContactS"""
      cur = conn.cursor()
      cur.execute(query2)
      rows = cur.fetchall();
      #conn.close()
      return render_template("dbtable.html", rows = rows)


if __name__ == '__main__':
       app.run(debug = True)
