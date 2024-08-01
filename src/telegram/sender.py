import os
import telebot
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_tg_message(message: str, bot_api_token: str, chat_id: str, ) -> bool:
    try:
        bot = telebot.TeleBot(bot_api_token)
        bot.send_message(chat_id, message, disable_web_page_preview=True)
        logger.info('telegram message sent')
        return True
    except Exception as e:
        logger.error(e)
        return False