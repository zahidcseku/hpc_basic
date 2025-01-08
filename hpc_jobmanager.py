import os
from time import time
from glob import glob
import pandas as pd


start_time = time()
# Define the total number of tasks
NTASKS=50

# Define the total number of samples
NSAMPLES=568630 

# Set the directory for job files
JOB_DIR=f"{os.getcwd()}/.jobs"

# Calculate the size of each task (samples per task)
SIZE=NSAMPLES//NTASKS

# Print the size of each task
print(f"Size of each task: {SIZE}")

# Create necessary directories
os.makedirs(JOB_DIR, exist_ok=True)
os.makedirs(".out", exist_ok=True)

job_queue = []
# Loop to create job files
for i in range(NTASKS):
    # Define the job file path
    job_filename=f"{JOB_DIR}/job_{i}.sh"
    # Calculate start and end indices for each task
    START = i * SIZE
    END = START + SIZE
    
    jobname = f"fraud_detection{i}.job"
    job_queue.append(jobname)
    # Create job files
    with open(job_filename, "w") as f:
        f.writelines(
f"""#!/bin/bash
#SBATCH --job-name=jobname
#SBATCH --output=.out/fraud_detection{i}.out
#SBATCH --error=.out/fraud_detection{i}.err
#SBATCH --time=1-00:00
#SBATCH --mem=2gb
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --account=OD-235759
 
# Load Python module
module load python/3.12.3
# Run the main script with start and end indices
sh ./run.sh {START} {END}

# Make the job file executable
chmod +x "${job_filename}"
"""
			)
 
    # Submit the job
    os.system(f"sbatch {job_filename}")