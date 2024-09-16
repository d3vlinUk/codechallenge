
import logging
logger = logging.getLogger(__name__)

def logging_noncompliant():
    filename = input("Enter a filename: ")
    logger.info("Processing %s", filename)