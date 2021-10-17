import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s--%(name)s--%(levelname)s--%(message)s",
                    datefmt='%m/%d/%Y %H:%M:%S')

import helper # note that the import should be after declaration of logger

""" Output
10/17/2021 11:09:07--helper--INFO--This is info message
"""