import logging
import Username

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formater = logging.Formatter('%(levelname)s : %(message)s')

file_handler = logging.FileHandler('sample2.log')
file_handler.setFormatter(formater)

logger.addHandler(file_handler)

logger.info("Testing the Logger File !!!!!")
