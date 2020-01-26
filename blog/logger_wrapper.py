import logging
import logging.handlers
import traceback
from blog.blog_exception import LoggerException


class LoggerWrapper:

    def __init__(self):
        self.logger = None

    def get_logger(self):

        try:

            self.logger = logging.getLogger('blog.engine')
            if not len(self.logger.handlers):
                file_name = "blog.log"
                logger_hdlr = logging.FileHandler(file_name)
                log_formatter = logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(thread)d - %(threadName)s - [%(module)s] - [%('
                    'funcName)s] - %(message)s')
                logger_hdlr.setFormatter(log_formatter)
                self.logger.addHandler(logger_hdlr)
                self.logger.setLevel(logging.DEBUG)
            return self.logger
        except LoggerException:
            print("Failed to get the logger object")
            print(traceback.format_exc())
