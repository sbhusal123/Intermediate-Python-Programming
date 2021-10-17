import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# roll over after 2KB
# Keep backup logs: app.log.1, app.log.2, 
handler = RotatingFileHandler('logs/app.log', maxBytes=2000, backupCount=10)
logger.addHandler(handler)

for i in range(100000000):
    logger.info("This is info message")