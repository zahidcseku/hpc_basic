#!/bin/bash

# Log start time
echo "Job started at: $(date)"

BRANCH="main"
MAIN_SCRIPT="main.py"
START_ID=$1
END_ID=$2


# Get the hostname
HOSTNAME=$(hostname)
echo "Hostname: $HOSTNAME"

# Detect if we are on a local PC or HPC
if [[ "$(hostname)" != "<local hostname>" ]]; then
    REPO_PATH="$HOME/hpc_basic"
    DATA_PATH="$SCRATCH3DIR/hpc_basic"
    PYTHON_PATH="python3"
    module load python/3.11.0
else
    REPO_PATH="<local repo path>"    
    DATA_PATH="<local data path>"
    PYTHON_PATH="python"
fi

# Change to the repository directory
cd "$REPO_PATH"

# Check if there are any changes in the remote repository
if git remote update && git status -uno | grep -q 'Your branch is behind'; then
    # Fetch the latest changes from the remote repository
    git fetch origin $BRANCH
else
    echo "No changes detected in the remote repository."
fi

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
    $PYTHON_PATH $MAIN_SCRIPT "$DATA_PATH" $START_ID $END_ID
else
    echo "Failed to sync repository"
    exit 1
fi

# Log start time
echo "Job ended at: $(date)"