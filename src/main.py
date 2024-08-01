import logging
from datetime import datetime

from db.query import DBQuery
from helpers import db_queries, text_convert, env
from telegram.sender import send_tg_message


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
	logger.info(f'[{datetime.now()}] started')
 
	tg_env_vars = env.get_telegram_env_vars()
	db_env_vars = env.get_db_env_vars()
 
	db = DBQuery(db_env_vars)
 
	reviews = db.select(query=db_queries.get_select_reviews_query())
	reviews_count = len(reviews)
	logger.info('found '+ str(reviews_count) + ' reviews')	
 
	for review in reviews:
		review_id = review[0]
		logger.info('processing review id ' + review_id)	
  
		tg_message = text_convert.convert_message(review)
  
		if send_tg_message(message=tg_message, **tg_env_vars):
			update_query = db_queries.get_update_review_query(review_id=review_id)
			db.update(query=update_query)
		
	db.close_connection()
	logger.info(f'[{datetime.now()}] ended')


if __name__ == "__main__":
	main()