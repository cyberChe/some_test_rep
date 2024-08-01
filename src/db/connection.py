import pyodbc
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DBConnection:

	def __init__(self, config: dict) -> pyodbc.Connection:
		self.config = config

	def __get_connection_string(self) -> str : 
		return f'DRIVER=ODBC Driver 18 for SQL Server;'\
			f'SERVER={self.config["db_host"]};'\
   			f'DATABASE={self.config["db_database"]};'\
      		f'PORT={self.config["db_port"]};'\
        	f'UID={self.config["db_user"]};'\
         	f'PWD={self.config["db_password"]};'\
          	'TrustServerCertificate=YES'

	def __create_connection(self) -> pyodbc.Connection:
		connection_string = self.__get_connection_string()
		try:
			connection = pyodbc.connect(connection_string)
			logger.info('db connected')
			return connection
		except Exception as e:
			logger.error(e)
			exit
   
	def get_connection(self) -> pyodbc.Connection:
		return self.__create_connection()

	@staticmethod
	def close_connection(connection: pyodbc.Connection) -> None:
		connection.close()
		logger.info('db connection closed')
 