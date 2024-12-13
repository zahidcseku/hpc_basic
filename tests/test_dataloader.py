import pytest
import pandas as pd
import os
from hpc_run.dataloader import get_feature_target_names, load_and_split_data

@pytest.fixture
def sample_csv(tmp_path):
    # Create a sample CSV file for testing
    df = pd.DataFrame({
        'V1': range(100),
        'V2': range(100, 200),
        'Amount': range(200, 300),
        'Class': [0] * 80 + [1] * 20
    })
    file_path = tmp_path / "test_credit_card.csv"
    df.to_csv(file_path, index=False)
    return file_path


def test_get_feature_target_names():
    """
    Checks if the function returns the correct number of 
    features and the right target name
    """
    features, target = get_feature_target_names()
    assert len(features) == 29
    assert all(f'V{i}' in features for i in range(1, 29))
    assert 'Amount' in features
    assert target == 'Class'


def test_load_and_split_data(sample_csv):
    """
    Uses a fixture to create a sample CSV file, then tests if 
    the data is loaded and split correctly.
    """
    train_data, test_data = load_and_split_data(sample_csv, test_size=0.3, random_state=42)
    
    assert len(train_data) == 70
    assert len(test_data) == 30
    assert len(train_data) > len(test_data)
    
    # Check if all columns are present
    expected_columns = ['V1', 'V2', 'Amount', 'Class']
    assert all(col in train_data.columns for col in expected_columns)
    assert all(col in test_data.columns for col in expected_columns)


def test_load_and_split_data_file_not_found():
    """
     Checks if the function raises a FileNotFoundError when 
     given a non-existent file.
    """
    with pytest.raises(FileNotFoundError):
        load_and_split_data("non_existent_file.csv")


def test_load_and_split_data_invalid_split():
    """
     Ensures the function handles invalid test_size values correctly.
    """
    with pytest.raises(ValueError):
        load_and_split_data(sample_csv, test_size=1.5)  # Invalid test_size


