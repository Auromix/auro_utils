# Import Logger
from auro_utils.loggers.logger_classic import Logger

# Instantiate logger
# Default console log level is "info"
# Console log level should be one of [debug, info, warning, error, critical]
# Default use_file_log is True
# If use_file_log is True, log file will be saved to "logs" folder
my_logger = Logger(log_level="debug",use_file_log=True)

# Log debug
my_logger.log_info("This is a debug log test.")
# Log info
my_logger.log_info("This is an info log test.")
# Log warning
my_logger.log_warning("This is a warning log test.")
# Log error
my_logger.log_error("This is an error log test.")
# Log critical
my_logger.log_critical("This is a critical log test.")

# Singleton pattern
# You can use logger in other modules
# without worrying about creating multiple instances
# because of the singleton pattern
# Logger will follow the same configuration as the first instance
my_singleton_pattern_logger = Logger(
    log_level="warning", use_file_log=False)
my_singleton_pattern_logger.log_debug("test_debug")
my_singleton_pattern_logger.log_info("test_info")
my_singleton_pattern_logger.log_warning("test_warning")
my_singleton_pattern_logger.log_error("test_error")
my_singleton_pattern_logger.log_critical("test_critical")

