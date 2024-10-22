import auro_utils.manager as au


def example_check_file_exists():
    """Example for check_file_exists.

    This function checks if a specified file exists.
    If the file does not exist, it raises a FileNotFoundError.
    """
    try:
        au.check_file_exists("example.txt")
        print("File exists.")
    except FileNotFoundError as e:
        print(e)


def example_ensure_path_exists():
    """Example for ensure_path_exists.

    This function ensures that the specified directory exists.
    If it does not exist, it creates the directory.
    """
    au.ensure_path_exists("logs/output.log")
    print("Path ensured: logs/output.log")


def example_get_project_top_level_dir():
    """Example for get_project_top_level_dir.

    This function retrieves the top-level directory of the
    Python project containing the current file.
    """
    top_level_dir = au.get_project_top_level_dir()
    print(f"Top-level project directory: {top_level_dir}")


def example_find_ros_package():
    """Example for find_ros_package.

    This function finds and returns the path of a specified
    ROS package by its name.
    """
    package_name = "your_ros_package_name"  # Replace with your actual package name
    try:
        package_path = au.find_ros_package(package_name)
        print(f"ROS package path: {package_path}")
    except Exception as e:
        print(e)


def example_get_current_system_time():
    """Example for get_current_system_time.

    This function retrieves the current system time in the
    'YYYYMMDDHHMMSS' format.
    """
    current_time = au.get_current_system_time()
    print(f"Current system time: {current_time}")


if __name__ == "__main__":
    example_check_file_exists()
    example_ensure_path_exists()
    example_get_project_top_level_dir()
    example_find_ros_package()
    example_get_current_system_time()
