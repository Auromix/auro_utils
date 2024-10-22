import os
import pytest
import toml
import json
from auro_utils.manager.config_manager import (
    load_config,
    save_config,
)  # Replace 'your_module' with the actual module name

# Sample data for testing
sample_toml = """[settings]
key = "value"
"""
sample_json = '{"settings": {"key": "value"}}'


@pytest.fixture
def tmp_dir(tmp_path):
    """Fixture to create a temporary directory."""
    return tmp_path


def test_load_config_from_toml(tmp_dir):
    toml_path = tmp_dir / "config.toml"
    toml_path.write_text(sample_toml)

    config = load_config(toml_path.name, relative_to=str(tmp_dir), file_type="toml")
    assert config == {"settings": {"key": "value"}}


def test_load_config_from_json(tmp_dir):
    json_path = tmp_dir / "config.json"
    json_path.write_text(sample_json)

    config = load_config(json_path.name, relative_to=str(tmp_dir), file_type="json")
    assert config == {"settings": {"key": "value"}}


def test_load_config_invalid_file_type(tmp_dir):
    with pytest.raises(ValueError, match="Config file must be a toml file."):
        load_config("config.json", relative_to=str(tmp_dir), file_type="toml")


def test_load_config_file_not_exist(tmp_dir):
    with pytest.raises(ValueError, match="Config file does not exist"):
        load_config("non_existent.toml", relative_to=str(tmp_dir), file_type="toml")


def test_save_config_to_toml(tmp_dir):
    config_data = {"settings": {"key": "value"}}
    save_config(config_data, "config.toml", relative_to=str(tmp_dir), file_type="toml")

    loaded_config = load_config(
        "config.toml", relative_to=str(tmp_dir), file_type="toml"
    )
    assert loaded_config == config_data


def test_save_config_to_json(tmp_dir):
    config_data = {"settings": {"key": "value"}}
    save_config(config_data, "config.json", relative_to=str(tmp_dir), file_type="json")

    loaded_config = load_config(
        "config.json", relative_to=str(tmp_dir), file_type="json"
    )
    assert loaded_config == config_data


def test_save_config_invalid_type(tmp_dir):
    with pytest.raises(ValueError, match="Config must be a dictionary."):
        save_config(
            "invalid_config", "config.toml", relative_to=str(tmp_dir), file_type="toml"
        )
