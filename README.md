# auro_utils

Auro Utils is a utility package offering various practical supports for the Auromix application, such as enhanced logging capabilities and more.

## Install

```bash
git clone https://github.com/Auromix/auro_utils
cd auro_utils
pip install -e .
```

## Test

```bash
cd auro_utils
python3 -m pytest -v .
```

## Usage

Following are some simplified examples of utilities offered by this package.

You can also find detailed examples in the `examples` folder.

```bash
cd auro_utils/examples
```

## Logger

### logger

Logger is a class that can be used to log messages to the console and to a file. It is a wrapper around loguru.

```python
from auro_utils.loggers.logger import Logger
my_logger = Logger()
my_logger.log_info("This is a info log test.")
```

### classic logger

Classic logger is a class that can be used to log messages to the console and to a file. It is a wrapper around the standard python logging module.

```python
from auro_utils.loggers.logger_classic import Logger
my_logger = Logger()
my_logger.log_info("This is a info log test.")
```

## Troubleshooting

### ModuleNotFoundError

Make sure you have installed the package correctly. See [Install](#install) section.

### Want to uninstall

```bash
pip uninstall auro_utils
```

## Contribute

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## License

```text
 Copyright © 2023 Herman Ye@Auromix.

 Licensed under the Apache License, Version 2.0 (the "License");
 You may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
```
