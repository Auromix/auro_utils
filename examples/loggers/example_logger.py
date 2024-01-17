# Import Logger
from auro_utils.loggers.logger import Logger

# Instantiate logger
# Default console log level is "info"
# Console log level should be one of [debug, info, warning, error, critical]
# Default use_file_log is True
# If use_file_log is True, log file will be saved to "logs" folder
my_logger = Logger(console_log_level="debug", use_file_log=True)

# Log trace
my_logger.log_trace("This is a trace log test.")
# Log debug
my_logger.log_debug("This is a debug log test.")
# Log info
my_logger.log_info("This is an info log test.")
# Log success
my_logger.log_success("This is a success log test.")
# Log warning
my_logger.log_warning("This is a warning log test.")
# Log error
my_logger.log_error("This is an error log test.")
# Log critical
my_logger.log_critical("This is a critical log test.")

# Log exception
try:
    a = 5
    b = 0
    c = a / b
except Exception as e:
    my_logger.log_exception(e)
