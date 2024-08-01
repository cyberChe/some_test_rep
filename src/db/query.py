from db.connection import DBConnection
from pyodbc import Row
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DBQuery:
    
	def __init__(self, db_config: dict) -> None:
		self.__db = DBConnection(config=db_config)
		self.__connection = self.__db.get_connection()
    
	def select(self, query: str) -> list[Row]:
		try:
			with self.__connection.cursor() as cursor:
				cursor.execute(query)
				return cursor.fetchall()
		except Exception as e:
			logger.error(f"Error executing select query: {e}")
			raise
    
	def update(self, query: str) -> None:
		try:
			with self.__connection.cursor() as cursor:
				cursor.execute(query)
				self.__connection.commit()
				logger.info("updated and commited")
		except Exception as e:
			logger.error(f"error executing update query: {e}")
			raise
  
	def close_connection(self):
		self.__db.close_connection(self.__connection)