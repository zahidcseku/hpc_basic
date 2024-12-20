#!/bin/bash

# Set variables
LOCAL_PATH="C:/zahids files/git_repos/Leveraging HPC Clusters for Big Data ML Training"
BRANCH="main"
MAIN_SCRIPT="main.py"
$PYTHON_PATH="python"

# Change to the repository directory
cd "$LOCAL_PATH"

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
    $PYTHON_PATH $MAIN_SCRIPT
else
    echo "Failed to sync repository"
    exit 1
fi

