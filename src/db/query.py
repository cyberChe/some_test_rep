from db.connection import DBConnection
from pyodbc import Row
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DBQuery:
    
	def __init__(self, db_config: dict) -> None:
		self.__db = DBConnection(config=db_config)
		self.__connection = self.__db.get_connection()
		self.__cursor = self.__connection.cursor()
    
	def select(self, query: str) -> list[Row]:
		self.__cursor.execute(query)
		return self.__cursor.fetchall()
    
	def update(self, query: str):
		self.__cursor.execute(query)
		
	def commit(self):
		self.__cursor.commit()
		self.__cursor.close()
		logger.info('db commited')
  
	def close_connection(self):
		self.__db.close_connection(self.__connection)