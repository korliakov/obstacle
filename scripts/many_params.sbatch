#!/bin/bash
node=$(srun -N 8 -p RT hostname | tail -n 1)  
#SBATCH -N 1
#SBATCH --ntasks-per-node=1 # MPI process
#SBATCH --partition=RT
#SBATCH --nodelist=$node


for i in {1..4}
do	
	cd ~/obstacle/obstacle/data/$i
	srun  ~/bin/lmp_mpi -in in.obstacle 
done

srun ~/obstacle/obstacle/scripts/get_plots.py

