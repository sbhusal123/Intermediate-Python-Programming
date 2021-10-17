import logging

logger = logging.getLogger(__name__)

# define handlers
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("file.log") # name of the file

# set loglevels for handlers
stream_handler.setLevel(logging.WARNING) # logs messages above and equal WARN level
file_handler.setLevel(logging.ERROR) # logs messages above and equal ERROR level

# define formatters
stream_formatter = logging.Formatter("%(asctime)s--%(name)s--%(levelname)s--%(message)s")
file_formatter = logging.Formatter("%(asctime)s--%(name)s--%(levelname)s--%(message)s")

# setting formatters
stream_handler.setFormatter(stream_formatter)
file_handler.setFormatter(stream_formatter)

# add handler to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warn("This is a warning")
logger.error("This is an error")
