#!/bin/bash

# Define the total number of tasks
NTASKS=50
# Define the total number of samples
NSAMPLES=568630 
# Set the directory for job files
JOB_DIR=$PWD/.jobs
# Calculate the size of each task (samples per task)
SIZE=$((NSAMPLES / NTASKS))
# Print the size of each task
echo "Size of each task: $SIZE"

# Create necessary directories
mkdir -p "$JOB_DIR"
mkdir -p .out

# Loop to create job files
for i in $(seq 1 $NTASKS); do 
    # Define the job file path
    job_file="${JOB_DIR}/job_$i.sh"
    # Calculate start and end indices for each task
    START=$(( (i-1) * SIZE ))
    END=$((START + SIZE))
    
    # Create job file using heredoc
    cat << EOF > "${job_file}"
#!/bin/bash
#SBATCH --job-name=fraud_detection${i}.job
#SBATCH --output=.out/fraud_detection${i}.out
#SBATCH --error=.out/fraud_detection${i}.err
#SBATCH --time=1-00:00
#SBATCH --mem=2gb
#SBATCH --ntasks=1
#SBATCH --nodes=1

# Load Python module
module load python/3.12.3
# Run the main script with start and end indices
sh ./run.sh ${START} ${END}
EOF

    # Make the job file executable
    chmod +x "${job_file}"

    # Submit the job
    sbatch $job_file
done

