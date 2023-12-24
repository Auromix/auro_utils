#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright © 2023 Auromix.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Description: Logger class for console and file log.
# Author: Herman Ye

class Logger():
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        # If the class instance is not created, create one
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            return cls._instance
        # If the class instance is already created, return the created one
        else:
            cls._instance.log_warning(
                f"{cls._instance.logger_name} already exists!")
            cls._instance.log_info(
                f"Set [console_log_level] to [{cls._instance.console_log_level}]")
            cls._instance.log_info(
                f"Set [use_file_log] to [{cls._instance.use_file_log}]")

            return cls._instance

    def __init__(self, console_log_level="info", use_file_log=True):
        """Init logger.

        Args:
            console_log_level: console log level, should be one of [debug, info, warning, error, critical].
            use_file_log: whether to use file log.

        Returns:
            None
        """
        import logging
        import colorlog
        import time
        import os
        import inspect

        # If class is already initialized, skip the init
        if Logger._initialized:
            return

        # Get caller file name
        caller_frame = inspect.stack()[1]
        caller_module = inspect.getmodule(caller_frame[0])
        caller_file_name = os.path.splitext(
            os.path.basename(caller_module.__file__))[0]

        # Get parameters
        self.console_log_level = console_log_level
        self.use_file_log = use_file_log
        # Get logger
        self.logger_name = f"{caller_file_name}_{__name__}"
        self.logger = logging.getLogger(self.logger_name)
        # Set logger level to debug
        self.logger.setLevel(logging.DEBUG)
        # Set propagation to False to avoid duplicate log output
        self.logger.propagate = False

        # Create a console handler
        console_handler = logging.StreamHandler()
        # Create console formatter
        console_formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(levelname)s]  %(message)s',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red',
            })
        # Set console formatter
        console_handler.setFormatter(console_formatter)
        # Set console handler log level
        if self.console_log_level == "debug":
            console_handler.setLevel(logging.DEBUG)
        elif self.console_log_level == "info":
            console_handler.setLevel(logging.INFO)
        elif self.console_log_level == "warning":
            console_handler.setLevel(logging.WARNING)
        elif self.console_log_level == "error":
            console_handler.setLevel(logging.ERROR)
        elif self.console_log_level == "critical":
            console_handler.setLevel(logging.CRITICAL)
        else:
            raise ValueError(
                "Console log level should be one of [debug, info, warning, error, critical]")
        # Add console handler
        self.logger.addHandler(console_handler)

        if self.use_file_log:
            # Set file name format
            current_sys_time = time.strftime(
                "%Y_%m_%d_%H_%M_%S", time.localtime())
            script_directory = os.path.dirname(os.path.abspath(__file__))
            file_dir = f'{script_directory}/logs/{current_sys_time}'
            file_name = f'{file_dir}/{caller_file_name}_{__name__}.log'
            # Create file log directory
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            # Create file handler
            file_handler = logging.FileHandler(file_name)
            # Create file formatter
            file_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            # Set file formatter
            file_handler.setFormatter(file_formatter)
            # Set file handler level
            file_handler.setLevel(logging.DEBUG)
            # Add file handler
            self.logger.addHandler(file_handler)

        Logger._initialized = True
        self.log_info(f"{self.logger_name} initialized.")

    def __repr__(self):
        return f'Logger(name={self.logger_name}, console_log_level={self.console_log_level}, use_file_log={self.use_file_log})'

    def log_debug(self, txt: str, *args, **kwargs):
        self.logger.debug(txt, *args, **kwargs)

    def log_info(self, txt: str, *args, **kwargs):
        self.logger.info(txt, *args, **kwargs)

    def log_warning(self, txt: str, *args, **kwargs):
        self.logger.warning(txt, *args, **kwargs)

    def log_error(self, txt: str, exc_info=True, stack_info=True, *args, **kwargs):
        self.logger.error(txt, exc_info=exc_info,
                          stack_info=stack_info, *args, **kwargs)

    def log_critical(self, txt: str, exc_info=True, stack_info=True, *args, **kwargs):
        self.logger.critical(txt, exc_info=exc_info,
                             stack_info=stack_info, *args, **kwargs)


def main():
    # Test logger
    logger_test = Logger(console_log_level="debug")
    logger_test.log_debug("test_debug")
    logger_test.log_info("test_info")
    logger_test.log_warning("test_warning")
    logger_test.log_error("test_error")
    logger_test.log_critical("test_critical")

    # Test singleton pattern
    logger_singleton_pattern_test = Logger(
        console_log_level="warning", use_file_log=False)
    logger_singleton_pattern_test.log_debug("test_debug again")
    logger_singleton_pattern_test.log_info("test_info again")
    logger_singleton_pattern_test.log_warning("test_warning again")
    logger_singleton_pattern_test.log_error("test_error again")
    logger_singleton_pattern_test.log_critical("test_critical again")


if __name__ == "__main__":
    main()