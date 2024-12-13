import pytest
import numpy as np
import faiss
from hpc_run.modeltrainer import find_neighbours


@pytest.fixture
def sample_data():
    np.random.seed(42)  # For reproducibility
    query = np.random.rand(1, 128).astype(np.float32)
    dataset = np.random.rand(1000, 128).astype(np.float32)
    return query, dataset


def test_basic_functionality(sample_data):
    """
    Checks if the function returns the expected shape and valid results.
    """
    query, dataset = sample_data
    distances, indices = find_neighbours(query, dataset, k=5)
    assert distances.shape == (1, 5)
    assert indices.shape == (1, 5)
    assert np.all(distances >= 0)  # Distances should be non-negative
    assert np.all(indices >= 0) and np.all(indices < 1000)  # Indices should be within range


def test_multiple_queries(sample_data):
    """
    Ensures the function works with multiple query vectors.
    """
    _, dataset = sample_data
    queries = np.random.rand(10, 128).astype(np.float32)
    distances, indices = find_neighbours(queries, dataset, k=3)
    assert distances.shape == (10, 3)
    assert indices.shape == (10, 3)


def test_k_equal_to_dataset_size(sample_data):
    """
    Tests when k is equal to the dataset size.
    """
    query, dataset = sample_data
    distances, indices = find_neighbours(query, dataset, k=1000)
    assert distances.shape == (1, 1000)
    assert indices.shape == (1, 1000)
    assert len(np.unique(indices)) == 1000  # All indices should be unique


def test_input_list(sample_data):
    """
    Verifies that the function accepts list inputs.
    """
    query, dataset = sample_data
    query_list = query.tolist()
    dataset_list = dataset.tolist()
    distances, indices = find_neighbours(query_list, dataset_list, k=5)
    assert distances.shape == (1, 5)
    assert indices.shape == (1, 5)


def test_1d_query(sample_data):
    """
    Checks if the function handles 1D query vectors correctly.
    """
    _, dataset = sample_data
    query_1d = np.random.rand(128).astype(np.float32)
    distances, indices = find_neighbours(query_1d, dataset, k=5)
    assert distances.shape == (1, 5)
    assert indices.shape == (1, 5)



def test_dimension_mismatch(sample_data):
    """
    Ensures the function raises an error when dimensions don't match.
    """
    query, dataset = sample_data
    mismatched_query = np.random.rand(1, 64).astype(np.float32)
    with pytest.raises(ValueError, match="Dimensions of query vector and target dataset must match"):
        find_neighbours(mismatched_query, dataset)


def test_empty_dataset():
    """    
    Verifies behavior with an empty dataset.
    """
    query = np.random.rand(1, 128).astype(np.float32)
    empty_dataset = np.empty((0, 128), dtype=np.float32)
    with pytest.raises(RuntimeError):
        find_neighbours(query, empty_dataset)


def test_k_greater_than_dataset_size(sample_data):
    """
    Checks behavior when k is larger than the dataset.
    """
    query, dataset = sample_data
    k = len(dataset) + 10
    distances, indices = find_neighbours(query, dataset, k=k)
    assert distances.shape != (1, len(dataset))
    assert indices.shape != (1, len(dataset))

