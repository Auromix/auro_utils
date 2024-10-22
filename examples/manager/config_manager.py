import os
import json
import toml

import auro_utils.manager as au

# Sample configuration data to be saved
config_data = {"settings": {"key": "value"}}

# Define the path for saving the configuration file
# This can be a relative path based on the current working directory
config_file_path = "example_config.toml"
# Get home directory path
home_dir = os.path.expanduser("~")


# Function to save the configuration to a TOML file
def example_save_config():
    """
    Example function to demonstrate saving a configuration to a TOML file.
    """
    # Save the configuration data to a TOML file
    au.save_config(
        config_data, config_file_path, relative_to=home_dir, file_type="toml"
    )
    print(f"Configuration saved to {config_file_path}")


# Function to load the configuration from a TOML file
def example_load_config():
    """
    Example function to demonstrate loading a configuration from a TOML file.
    """
    # Load the configuration from the specified TOML file
    loaded_config = au.load_config(
        config_file_path, relative_to=home_dir, file_type="toml"
    )

    # Print the loaded configuration data
    print("Loaded configuration:", loaded_config)


# Execute the example functions
if __name__ == "__main__":
    example_save_config()  # Save the configuration
    example_load_config()  # Load and display the configuration
