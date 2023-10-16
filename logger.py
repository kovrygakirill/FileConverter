import os
from loguru import logger

LOG_DIR = 'logs'
LOG_FILENAME = 'file_converter.log'  # noqa
LOGGER_FORMAT = (
	"<green>{time:YYYY-MM-DD HH:mm:ss}</green> | {level} |"
	"<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - {message}"
)

os.makedirs(LOG_DIR, exist_ok=True)

log_file = os.path.join(LOG_DIR, LOG_FILENAME)

logger.add(
	log_file,
	rotation="00:00",
	retention="3 days",
	compression="zip",
	enqueue=True,
	format=LOGGER_FORMAT,
)


def get_logger():
	return logger
