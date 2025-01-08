#!/bin/bash
#SBATCH --job-name=fraud_dection.job
#SBATCH --output=.out/fraud_detection.out
#SBATCH --error=.out/fraud_detection.err
#SBATCH --time=1-00:00
#SBATCH --mem=2gb
#SBATCH --ntasks=50
#SBATCH --nodes=1
#SBATCH --account=OD-235759

module load python/3.12.3

sh ./run.sh 0 100