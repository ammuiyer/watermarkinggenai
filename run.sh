#!/bin/bash
#SBATCH -c 4  # Number of Cores per Task
#SBATCH --mem=8192  # Requested Memory
#SBATCH -p gpu  # Partition
#SBATCH -G 2  # Number of GPUs
#SBATCH --constraint=vram23 #it will get a gpu with at least 24g of memory, up to 80g
#SBATCH -t 10:00:00  # Job time limit
#SBATCH -o test.out 
python3 generate.py