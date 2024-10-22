import os

import numpy as np

import auro_utils.manager as au


# Sample data for saving
pickle_data = {"name": "example", "value": 42}
json_data = {"settings": {"key": "value"}}
toml_data = {"settings": {"key": "value"}}
hdf5_data = {"array1": np.array([1, 2, 3]), "array2": np.array([4, 5, 6])}

# Define file paths
home_dir = os.path.expanduser("~")
pickle_file_path = os.path.join(home_dir, "example_data.pkl")
json_file_path = os.path.join(home_dir, "example_data.json")
toml_file_path = os.path.join(home_dir, "example_data.toml")
hdf5_file_path = os.path.join(home_dir, "example_data.h5")


# Example functions for file operations
def example_save_pickle():
    au.write_pickle(pickle_data, pickle_file_path)
    print(f"Pickle data saved to {pickle_file_path}")


def example_load_pickle():
    loaded_data = au.read_pickle(pickle_file_path)
    print("Loaded Pickle data:", loaded_data)


def example_save_json():
    au.write_json(json_data, json_file_path)
    print(f"JSON data saved to {json_file_path}")


def example_load_json():
    loaded_data = au.read_json(json_file_path)
    print("Loaded JSON data:", loaded_data)


def example_save_toml():
    au.write_toml(toml_data, toml_file_path)
    print(f"TOML data saved to {toml_file_path}")


def example_load_toml():
    loaded_data = au.read_toml(toml_file_path)
    print("Loaded TOML data:", loaded_data)


def example_save_hdf5():
    au.write_hdf5(hdf5_data, hdf5_file_path)
    print(f"HDF5 data saved to {hdf5_file_path}")


def example_load_hdf5():
    loaded_data = au.read_hdf5(hdf5_file_path)
    print("Loaded HDF5 data:", loaded_data)


def example_list_operations():
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    batches = au.split_list_into_batches(sample_list, 3, delete_last_one=True)
    print("Batches:", batches)
    segment = au.get_list_segment(sample_list, 5, 2, 2)
    print("Segment around index 5:", segment)


# Execute the example functions
if __name__ == "__main__":
    example_save_pickle()
    example_load_pickle()
    example_save_json()
    example_load_json()
    example_save_toml()
    example_load_toml()
    example_save_hdf5()
    example_load_hdf5()
    example_list_operations()
