# HPC Machine Learning Model Training

Check out the full article: 
- Linkedin:
- Medium:  

This repository contains code and instructions for training large-scale machine learning models using High Performance Computing (HPC) clusters.

## Overview

As machine learning models and datasets grow in size and complexity, training them on a single machine becomes impractical. This project demonstrates how to leverage HPC resources to train ML models on large datasets efficiently.

## Contents

- `hpc_run/`: main scripts for data processing
    - `dataloader.py`: splits the dataset into train and test sets.
    - `modeltrainer.py`: includes a function to find labels based on k neighbours.
- `tests/`: includes the unit tests.
- `main.py`: include the main loop that assigns a label to all the selected test instances.
- `hpc_jobmanager.py`: creates SLURM job submission scripts and submits the jobs.
- `hpc_run.sh`: a sample bash script for a single SLURM job. Note that `hpc_jobmanager.py` will create a set of SLURM jobs based on our specified tasks and automatically submit those jobs to the job queue.
- `run.sh`: a simple bash script to run the program on a local or remote machine. 



## Prerequisites

- Access to an HPC cluster with SLURM job scheduler
- Python 3.8+
- Required Python packages (see `requirements.txt`)

## Usage

1. Clone this repository to your local machine.
2. Transfer the necessary files to your HPC environment.
3. Modify the `job_submission.sh` script to fit your specific HPC environment and resource needs.
4. Adapt your ML model code using the patterns shown in `parallel_processing.py`.
5. Submit your job using: `sbatch job_submission.sh`

## Best Practices

- Always test your code on a small subset of data before submitting large jobs.
- Use appropriate file systems for different stages of your workflow (e.g., $SCRATCH for temporary data, $HOME for scripts).
- Monitor your job's resource usage and adjust the SLURM parameters as necessary.
- Remember to transfer your results to persistent storage after job completion.

## Contributing

Contributions to improve the code or documentation are welcome. Please submit a pull request or open an issue to discuss proposed changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.