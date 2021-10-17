import logging
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Logged every second
# Interval of 1 second
handler = TimedRotatingFileHandler('logs/app.log', when='s', interval=1, backupCount=5)
logger.addHandler(handler)

for i in range(10):
    time.sleep(1) # wait for a second
    logger.info("This is info message")
    logger.error("This is error message")
    logger.warn("This is warning message")