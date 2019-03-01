import pymysql

class DbHandle(object):
	"""docstring for _db"""
	def __init__(self, database, user, password, host='127.0.0.1', port='80', charset='utf8mb4'):

		self.database = database
		self.user = user
		self.password = password
		self.charset = charset
		self.host = host
		self.port = port

	def connect_db(self, database=None):
		database = database or self.database
		try:
			conn=pymysql.connect(
				host=self.host, 
				user=self.user, 
				password=self.password, 
				db=self.database, 
				charset=self.charset)
			return conn
		except Exception as e:
		
			raise e

	def connect(self):
		
		try:
			conn=pymysql.connect(
				host=self.host, 
				user=self.user, 
				password=self.password, 
				charset=self.charset)
			return conn
		except Exception as e:
		
			raise e

	def excute_sql(self, conn, sql):

		try:

			cursor = conn.cursor()
			# print('will execute sql: ', sql)
			result = cursor.execute(sql)
			# print('succeed to execute sql: ', sql)
			conn.commit()
			cursor.close()
			# conn.close()
			return result

		except Exception as e:	
			# conn.close()
			# raise e
			print('fail to execute sql: ', sql)
			print('--'*20)
			print("resaon: ", str(e))
			print('--'*20)
			pass

	def select_sql(self, conn, sql):

		try:

			cursor = conn.cursor()
			cursor.execute(sql)
			rows = cursor.fetchall()

			conn.commit()
			cursor.close()
			# conn.close()
			return rows

		except Exception as e:	
			# conn.close()
			raise e


	def create_db(self):
		try:
			conn = self.connect()
			cursor = conn.cursor()
			cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(self.database))
			cursor.close()
			conn.close()

		except Exception as e:
			
			raise e

	def is_new_db(self):
		try:
			conn = self.connect_db()
			conn.close()
		except Exception as e:
			print(e)
			strerror= str(e)
			code = strerror.find("1049")
			msg = strerror.find("Unknown database")

			if (code != -1) and (msg != -1):
				print("[Warning]It's seem that database doesnot exist, will be create new one")
				self.create_db()
			# conn.close()



def create_table(command):
	try:
		conn=pymysql.connect(
			host=self.host, 
			user=self.user, 
			password=self.password,
			db=self.database)
		cursor = conn.cursor()
		cursor.execute(command)
		cursor.close()
		conn.close()

	except Exception as e:
		
		raise e

def create_top_baidu_table():
	file = os.path.join('.', 'table', 'topbaidu.sql')
	import codecs
	with codecs.open(file, 'rb', 'utf-8') as file_obj:
		sql_list = file_obj.read().strip().split(';')[:-1]
		for sql in sql_list:
			create_table(sql)

def create_top_news_table():
	file = os.path.join('.', 'table', 'topnews.sql')
	import codecs
	with codecs.open(file, 'rb', 'utf-8') as file_obj:
		sql_list = file_obj.read().strip().split(';')[:-1]
		for sql in sql_list:
			create_table(sql)

def create_news_details_table():
	file = os.path.join('.', 'table', 'newsdetails.sql')
	import codecs
	with codecs.open(file, 'rb', 'utf-8') as file_obj:
		sql_list = file_obj.read().strip().split(';')[:-1]
		for sql in sql_list:
			create_table(sql)

# is_new_db()
# create_top_baidu_table()
# create_top_news_table()
# create_news_details_table()

