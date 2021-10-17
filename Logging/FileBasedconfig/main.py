import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample') # simpleExample logger is defined in logging.conf file


logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

"""
Output:
2021-10-17 13:43:13,585 - simpleExample - WARNING - warn message
2021-10-17 13:43:13,585 - simpleExample - ERROR - error message
2021-10-17 13:43:13,585 - simpleExample - CRITICAL - critical message
"""