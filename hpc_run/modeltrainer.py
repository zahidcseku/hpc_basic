import numpy as np
import faiss
from typing import Tuple, Optional


def find_neighbours(query_vector: np.ndarray, 
                    target_dataset: np.ndarray, 
                    k: int = 30
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Perform a k-nearest neighbor search using FAISS.

    Args:
        query_vector (np.ndarray): The query vector(s) to search for. Shape should be (n_queries, n_dimensions).
        target_dataset (np.ndarray): The dataset to search in. Shape should be (n_samples, n_dimensions).
        k (int, optional): The number of nearest neighbors to return. Defaults to 30.

    Returns:
        Tuple[np.ndarray, np.ndarray]: A tuple containing two numpy arrays:
            - distances: The distances to the k-nearest neighbors. Shape: (n_queries, k)
            - indices: The indices of the k-nearest neighbors in the target dataset. Shape: (n_queries, k)

    Raises:
        ValueError: If the dimensions of query_vector and target_dataset don't match.
        RuntimeError: If FAISS encounters an error during index creation or search.
    """
    try:
        # Ensure inputs are numpy arrays and have correct shape
        query_vector = np.asarray(query_vector, dtype=np.float32)
        target_dataset = np.asarray(target_dataset, dtype=np.float32)

        # Check if the dataset is empty
        if target_dataset.size == 0:
            raise RuntimeError("The target dataset is empty.")

        if query_vector.ndim == 1:
            query_vector = query_vector.reshape(1, -1)

        if query_vector.shape[1] != target_dataset.shape[1]:
            raise ValueError("Dimensions of query vector and target dataset must match.")

        # Create and populate the index
        index = faiss.IndexFlatL2(target_dataset.shape[1])
        index.add(target_dataset)

        # Perform the search
        distances, indices = index.search(query_vector, k)

        return indices

    except RuntimeError as e:
        raise RuntimeError(f"FAISS error: {str(e)}")


if __name__ == "__main__":
    # Create sample data
    query = np.random.rand(1, 128).astype(np.float32)
    dataset = np.random.rand(1000, 128).astype(np.float32)

    # Find nearest neighbors
    distances, indices = find_neighbours(query, dataset, k=5)
    print("Distances:", distances)
    print("Indices:", indices)
