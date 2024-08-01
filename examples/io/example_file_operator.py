# Get the project top level directory
from auro_utils.io.file_operator import get_project_top_level_dir
project_top_dir=get_project_top_level_dir()
print(project_top_dir)

# Read a toml file
from auro_utils.io.file_operator import read_toml
config = read_toml(project_top_dir+ "/config.toml")
print(config)
