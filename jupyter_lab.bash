#!/bin/bash

port=6593
node=$(srun -N 8 -p RT hostname | tail -n 1)


echo "The node is: $node"
echo "The port is: $port"

cd ~

#ssh-keyscan $node >>~/.ssh/known_hosts


result=$(sbatch -N 1 --ntasks-per-node=1 --partition=RT --nodelist=$node --wrap="srun jupyter lab --port $port --no-browser"  | grep "Submitted" | awk '{print $4}' )


echo "$node $port $result"



#sleep 2

#echo "The job ID is: $result" 






#mv ~/slurm-$result.out ~/obstacle/obstacle


#cd ~/obstacle/obstacle


#token=$(cat slurm-$result.out | tail -n 2 | head -n 1 | sed 's/.*token=//')


#rm -f slurm-$result.out  


#echo "The token is: $token"

#ssh -NL localhost:$port:localhost:$port $node 





