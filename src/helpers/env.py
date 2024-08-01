from dotenv import load_dotenv
from os import getenv

load_dotenv()

def get_env_var_by_key(var_key: str) -> str:
    return getenv(var_key)

def get_db_env_vars() -> dict:
	return {
		'db_host' : getenv('db_host'),
		'db_port' : getenv('db_port'),
		'db_database' : getenv('db_database'),
		'db_password' : getenv('db_password'),
		'db_user' : getenv('db_user'),
	}
 
def get_telegram_env_vars() -> dict:
    return {
		'bot_api_token': getenv('tg_bot_api_key'),
		'chat_id': getenv('tg_chat_id'),
	}