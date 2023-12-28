import logging
import os


def setup_logger():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logger = logging.getLogger()
    default_level = logging.DEBUG if os.environ.get("DEBUG") else logging.INFO
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(default_level)

    return logger


logger = setup_logger()
