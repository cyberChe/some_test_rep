import pyodbc
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DBConnection:

	def __init__(self, config: dict) -> pyodbc.Connection:
		self.__config = config

	def __get_connection_string(self) -> str : 
		return f'DRIVER=ODBC Driver 18 for SQL Server;'\
			f'SERVER={self.__config["db_host"]};'\
   			f'DATABASE={self.__config["db_database"]};'\
      		f'PORT={self.__config["db_port"]};'\
        	f'UID={self.__config["db_user"]};'\
         	f'PWD={self.__config["db_password"]};'\
          	'TrustServerCertificate=YES'

	def __connect(self) -> pyodbc.Connection:
		connection_string = self.__get_connection_string()
		try:
			connection = pyodbc.connect(connection_string)
			logger.info('db connected')
			return connection
		except Exception as e:
			logger.error(e)
			logger.info(self.__config)
			raise
   
	def get_connection(self) -> pyodbc.Connection:
		return self.__connect()

	@staticmethod
	def close_connection(connection: pyodbc.Connection) -> None:
		connection.close()
		logger.info('db connection closed')
 