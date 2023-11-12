import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('bot')
logger.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')

handler = RotatingFileHandler('bot.log', maxBytes=1024 * 1024, backupCount=5)  # 1 MB per file, keep 5 backup files
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

logger.addHandler(handler)
