#!/bin/bash

BRANCH="main"
MAIN_SCRIPT="main.py"
START_ID=0
END_ID=100


# Detect if we are on a local PC or HPC
if [[ "$(hostname)" == "hpc.petrichor.csiro.au" ]]; then
    PATH="/home/Leveraging HPC Clusters for Big Data ML Training"
    PYTHON_PATH="python3"
    module load python
else
    PATH="C:/zahids files/git_repos/Leveraging HPC Clusters for Big Data ML Training"    
    PYTHON_PATH="python"
fi

# Change to the repository directory
cd "$PATH"

# Fetch the latest changes from the remote repository
git fetch origin $BRANCH

# Check for unsynced changes
if ! git diff-index --quiet HEAD --; then
    echo "Warning: There are unsynced changes in the repository."
    exit 1
fi

# Pull the latest changes
git pull origin $BRANCH

# Check if the sync was successful
if [ $? -eq 0 ]; then
    echo "Repository synced successfully"
    
    # Run the Python script
    $PYTHON_PATH $MAIN_SCRIPT "$PATH" $START_ID $END_ID
else
    echo "Failed to sync repository"
    exit 1
fi

