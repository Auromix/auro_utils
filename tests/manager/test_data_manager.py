import os
import pytest
import json
import pickle
import toml
import h5py
import numpy as np

from auro_utils.manager.data_manager import (
    read_pickle,
    write_pickle,
    read_json,
    write_json,
    read_toml,
    write_toml,
    read_hdf5,
    write_hdf5,
    split_list_into_batches,
    get_list_segment,
)

# Sample data for testing
sample_data = {"key1": "value1", "key2": [1, 2, 3]}


# Test Pickle
def test_write_read_pickle(tmp_path):
    file_path = tmp_path / "test.pkl"
    write_pickle(sample_data, file_path)
    result = read_pickle(file_path)
    assert result == sample_data


# Test JSON
def test_write_read_json(tmp_path):
    file_path = tmp_path / "test.json"
    write_json(sample_data, file_path)
    result = read_json(file_path)
    assert result == sample_data


# Test TOML
def test_write_read_toml(tmp_path):
    file_path = tmp_path / "test.toml"
    write_toml(sample_data, file_path)
    result = read_toml(file_path)
    assert result == sample_data


# Test HDF5
def test_write_read_hdf5(tmp_path):
    file_path = tmp_path / "test.h5"
    write_hdf5({"dataset": np.array([1, 2, 3])}, file_path)
    result = read_hdf5(file_path)
    assert np.array_equal(result["dataset"], np.array([1, 2, 3]))


# Test splitting list into batches
def test_split_list_into_batches():
    data = list(range(10))
    result = split_list_into_batches(data, 3)
    assert result == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

    result = split_list_into_batches(data, 3, delete_last_one=True)
    assert result == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


# Test getting list segment
def test_get_list_segment():
    data = list(range(10))
    result = get_list_segment(data, 5, 2, 2)
    assert result == [3, 4, 5, 6, 7]

    result = get_list_segment(data, 0, 1, 1)
    assert result == [9, 0, 1]


# Test error handling for reading/writing files
def test_read_write_errors(tmp_path):
    invalid_file_path = tmp_path / "invalid.pkl"

    # Test that reading a non-existent file raises ValueError
    with pytest.raises(FileNotFoundError):
        read_pickle(invalid_file_path)


# Additional tests can be added as necessary

if __name__ == "__main__":
    pytest.main()
