import inspect

import pytest
import logging

from distutils import version


# Define base class to use keep all the common code
# Base class to make use of fixtures
@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        # __name__ to print test case name into logger filr
        logger = logging.getLogger(loggerName)
        # logger is object to print all the information into log file all warnings, debug info, errors will be
        # printed into one file by addHandler method and it takes file handler object file handler object
        fileHandler = logging.FileHandler('logfile.log')

        # asctime indicates date and time
        # levelname indicates whether it is error or warning
        # name indicates test case name
        # message indicates error message
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)")
        # connecting formatter to file
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        # to set the level / order of information to be printed on Log file (Info, warning, error and critical will
        # be available)
        logger.setLevel(logging.INFO)

        # It just prints the message into output/one file i.e, log file
        return logger
