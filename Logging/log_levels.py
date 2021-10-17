import logging


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s--%(name)s--%(levelname)s--%(message)s",
                    datefmt='%m/%d/%Y %H:%M:%S')

"""
By default only the level >=WARN is handled.
"""
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

""" Output
10/17/2021 10:52:34--root--DEBUG--Debug message
10/17/2021 10:52:34--root--INFO--Info message
10/17/2021 10:52:34--root--WARNING--Warning message
10/17/2021 10:52:34--root--ERROR--Error message
10/17/2021 10:52:34--root--CRITICAL--Critical message
"""