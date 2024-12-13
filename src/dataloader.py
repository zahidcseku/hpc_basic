import numpy as np
import pandas as pd
from typing import List, Tuple
from sklearn.model_selection import train_test_split


def get_feature_target_names() -> Tuple[List[str], str]:
    """
    Returns the feature names and target variable name.
    
    Returns:
        Tuple[List[str], str]: A tuple containing the list of feature names 
        and the target variable name.
    """
    features = [f'V{i}' for i in range(1, 29)] + ['Amount']
    target = "Class"
    return features, target


def load_and_split_data(data_path: str, 
                        test_size: float = 0.4, 
                        random_state: int = 42
                        ) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Loads data from a CSV file and splits it into training and testing sets.
    
    Args:
        data_path (str): Path to the CSV file.
        test_size (float): Proportion of the dataset to include in the test split. Default is 0.4.
        random_state (int): Random state for reproducibility. Default is 42.
    
    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: A tuple containing the training and testing DataFrames.
    
    Raises:
        FileNotFoundError: If the specified data file is not found.
        AssertionError: If the train data is not larger than the test data.
    """
    try:
        data = pd.read_csv(data_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {data_path} was not found. Please check the file path.")

    print(f"Shape of the dataset: {data.shape}")

    train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
    
    print(f"Train data shape: {train_data.shape}")
    print(f"Test data shape: {test_data.shape}")
    
    assert len(train_data) > len(test_data), "Train data should be larger than test data"

    return train_data, test_data

def main():
    data_path = "./datasets/creditcard_2023.csv"
    features, target = get_feature_target_names()
    train_data, test_data = load_and_split_data(data_path)
    
    # You can add more processing or model training steps here

if __name__ == "__main__":
    main()
