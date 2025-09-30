# IPC CHARACTERSTICS

## SETTING UP RODINIA
Clone the rodinia benchmark repository

````
git clone https://github.com/yuhc/gpu-rodinia.git
````
Download the dataset from the following link https://www.dropbox.com/s/cc6cozpboht3mtu/rodinia-3.1-data.tar.gz
And extract it.
navigate to the rodinia-data/bfs/inputGen and run the graphgen program to generate a graph with 2^25 nodes

````
./graphgen 33554432 
````
a text file named graph33554432.txt will be generated.
copy it to the gpu-rodinia\openmp\bfs


## COLLECTING THE IPC DATA

Execute the following command to run the bfs code as follows.
./bfs <input_file> <no. of threads>

````
perf stat -e cycles,instructions -I 10 -x, -o rodinia_data.csv ./bfs graph33554432.txt 1
````

This would store the cycles, instructions and IPC values of every 10 ms interval in rodinia_data.csv file.




