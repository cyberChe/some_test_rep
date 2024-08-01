import os
import telebot
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def send_tg_message(message: str) -> bool:
    chat_id = os.getenv('tg_chat_id')
    bot_api_token = os.getenv('tg_bot_api_key')

    try:
        bot = telebot.TeleBot(bot_api_token)
        bot.send_message(chat_id, message)
        logger.info('telegram message sent')
        return True
    except Exception as e:
        logger.error(e)
        return False