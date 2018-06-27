import sqlite3

class DBHelper:
	def __init__(self,dbname='bot.sqlite'):
		self.dbname=dbname
		self.conn=sqlite3.connect(dbname)

	def setup(self):
		stmnt_chat_data='CREATE TABLE IF NOT EXISTS CHAT_DATA (CHAT_ID INTEGER PRIMARY KEY,USERNAME text)'
		stmnt_movie_data='CREATE TABLE IF NOT EXISTS MOVIE_DATA(MOVIE_NAME text)'
		self.conn.execute(stmnt_chat_data)
		self.conn.execute(stmnt_movie_data)
		self.conn.commit()


	def get_id(self):
        stmt = "SELECT CHAT_ID FROM CHAT_DATA "
        return [x[0] for x in self.conn.execute(stmt)]


	def get_movie_list(self):
		stmnt='SELECT MOVIE_NAME FROM MOVIE_DATA'


	def add_movie(self,movie_name):
		stmnt='INSERT INTO MOVIE_DATA (MOVIE_NAME) VALUES(?) ',(movie_name)
		self.conn.execute(stmnt)
		self.conn.commit()
		


	def add_id(self,chat_id,username):
		stmnt='INSERT INTO CHAT_DATA(CHAT_ID,USERNAME) VALUES(?,?)'
		args=(chat_id,username)
		self.conn.execute(stmnt,args)
		self.conn.commit()

	def delete_id(self,chat_id):
		stmnt='DELETE FROM CHAT_DATA WHERE CHAT_ID=(?)',(chat_id)
		self.conn.execute(stmnt)
		self.conn.commit()

	def delete_movie(self,movie_name):
		stmnt='DELETE FROM MOVIE_DATA WHERE MOVIE_NAME =(?) ',(movie_name)
		self.conn.execute(stmnt)
		self.conn.commit()

