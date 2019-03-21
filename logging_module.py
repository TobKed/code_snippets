import logging

FORMAT = '[%(asctime)-15s] [%(name)s] [%(levelname)s] - %(message)s'

logging.basicConfig(format=FORMAT)

logger = logging.getLogger("MY_LOGGER")

logger.error("My error message")

logger.warning("My warning message")
