"""Logging configuration."""
import logging
import os
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')


def get_logger(name):
    """Get a configured logger."""
    os.makedirs(LOG_DIR, exist_ok=True)
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        # File handler
        today = datetime.now().strftime('%Y-%m-%d')
        fh = logging.FileHandler(os.path.join(LOG_DIR, f'{name}_{today}.log'))
        fh.setLevel(logging.DEBUG)
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # Format
        fmt = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s: %(message)s')
        fh.setFormatter(fmt)
        ch.setFormatter(fmt)
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger
