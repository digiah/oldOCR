#!/bin/bash
#SBATCH --job-name=OCROPYrun
#SBATCH --partition=exclusive.q
## 3 day max run time for community.q, kill.q, exclusive.q, and htc.q. 1 Hour max run time for sb.q
#SBATCH --time=3-00:00:00         ## time format is DD-HH:MM:SS
## task-per-node x cpus-per-task should not typically exceed core count on an individual node
#SBATCH --nodes=1                 ## should not be greater than 1 unless you are utilizing MPI code
#SBATCH --tasks-per-node=1        ## should not be greater than 1 unless you are utilizing MPI code
#SBATCH --cpus-per-task=20        ## how you control how many cores on a node you are requesting
#SBATCH --error=hello-%A.err      ## %A - filled with jobid
#SBATCH --output=hello-%A.out     ## %A - filled with jobid

source ~/.bash_profile #if you want to use modules or need environment variables, source your bash profile

##export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}
##export I_MPI_FABRICS=shm:tmi
##export I_MPI_PMI_LIBRARY=/opt/local/slurm/default/lib64/libpmi.so

export SLURM_SUBMIT_DIR=/home/urao/lus/train_normal_italics2S
cd ${SLURM_SUBMIT_DIR}
export PYTHONIOENCODING="UTF-8"

## Normal over default
#stdbuf -o0 -e0 ocropus-rtrain --load en-default.pyrnn.gz -o hume-model-nod- *.png > result.log 2>&1 
# Normal by itself
#stdbuf -o0 -e0 ocropus-rtrain -o hume-model-noit- *.png > result.log 2>&1 
# Normal over italics over default
#stdbuf -o0 -e0 ocropus-rtrain --load hume-model-iSod.pyrnn.gz -o hume-model-noiSod- *.png > result.log 2>&1 
# Normal over default
#stdbuf -o0 -e0 ocropus-rtrain --load en-default.pyrnn.gz -o hume-model-niSod- *.png > result.log 2>&1 
stdbuf -o0 -e0 ocropus-rtrain --load hume-model-niSod--00134000.pyrnn.gz -o hume-model-niSod- *.png > result.log 2>&1 
