import os
import pytest
from auro_utils.manager.file_manager import (
    check_file_exists,
    ensure_path_exists,
    get_project_top_level_dir,
    find_ros_package,
    get_current_system_time,
)


def test_check_file_exists_existing_file(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello, World!")
    check_file_exists(str(test_file))  # Should not raise an error


def test_check_file_exists_non_existing_file():
    with pytest.raises(FileNotFoundError):
        check_file_exists("non_existing_file.txt")


def test_ensure_path_exists_creates_directory(tmp_path):
    dir_path = tmp_path / "new_directory"
    ensure_path_exists(str(dir_path / "file.txt"))
    assert dir_path.is_dir()


def test_get_project_top_level_dir():
    top_level_dir = get_project_top_level_dir()
    assert os.path.isdir(top_level_dir)


@pytest.mark.parametrize("package_name", ["roscpp", "std_msgs"])
def test_find_ros_package(package_name):
    package_path = find_ros_package(package_name)
    assert os.path.exists(package_path)


def test_get_current_system_time_format():
    current_time = get_current_system_time()
    assert len(current_time) == 14  # YYYYMMDDHHMMSS
    assert current_time.isdigit()
