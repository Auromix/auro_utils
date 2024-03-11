from auro_utils.loggers.logger import Logger


# Instantiate logger
# Example 1: Use default settings
my_logger = Logger()

# Example 2: Use file log
# Default log path is the top-level directory of your project
# my_logger=Logger(log_level="debug",use_file_log=True)

# Example 3: Use file log with custom log directory path
# my_logger=Logger(log_level="debug",use_file_log=True,log_path="your_log_path")

# Log trace
my_logger.log_trace("This is a trace log.")

# Log debug
my_logger.log_debug(
    "This is a debug log which is not shown if log level more than debug.")

# Log info
my_logger.log_info("This is an info log without custom tag.")

# Log success
my_logger.log_success(
    "This is a success log with custom tag.", tag="glad to see this line")

# Log warning
my_logger.log_warning("This is a warning log.")

# Log error
try:
    a = 233
    b = "Hello, World!"
    c = a + b
except Exception as e:
    my_logger.log_error("This is a error log with exception.", e)

# Log critical
my_logger.log_critical("This is an error log without exception.")

# Log exception
try:
    a = 5
    b = 0
    c = a / b
except Exception as e:
    my_logger.log_exception(e)
