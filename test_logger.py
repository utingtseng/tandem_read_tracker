import logging

# Create a logger object
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Create handlers
fh = logging.FileHandler("my_logger.log")
ch = logging.StreamHandler()

# Create a formatter and set it for both handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# Test logging messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
