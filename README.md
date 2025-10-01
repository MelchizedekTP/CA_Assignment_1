# CA Assignment 1

## Isolate cpu core
go to directory:
```
cd /etc/default/grub
```
update grup file
```
GRUB_CMDLINE_LINUX="isolcpus=0"
```
This stops the kernel from assigning processes to core : 0

Next update kernel
```
sudo update-grub
```
reboot the system for this to take effect

## Run program on specific core
```
taskset -a --cpu-list 0 ./program
```

## Perf commands used
Events
```
L1-dcache-load-misses,L1-icache-load-misses,l2_rqsts.miss,dTLB-load-misses,iTLB-load-misses,br_misp_retired.all_branches_pebs
```
get data for programs q1
```
perf stat -e fp_arith_inst_retired.scalar_single,mem_inst_retired.all_loads,mem_inst_retired.all_stores
```

Get data for events
```
perf stat -e L1-dcache-load-misses,L1-icache-load-misses,l2_rqsts.miss,dTLB-load-misses,iTLB-load-misses,br_misp_retired.all_branches_pebs -I 10 -x, -o data.csv ./bfs -u 10 -n 1
```
IPC 
```
perf stat -e L1-dcache-load-misses,L1-icache-load-misses,l2_rqsts.miss,dTLB-load-misses,iTLB-load-misses,br_misp_retired.all_branches_pebs,cycles,instructions -I 10 -x, -o data.csv ./bfs -u 10 -n 1
```


## Likwid commands used
To get cache sizes
```
likwid-topology -c
```

LIKWID COMMAND FOR PEAK FLOSP
```
likwid-bench -t peakflops_sp -w S0:10KB:1
```

LIKWID COMMAND FOR PEAK BANDWIDTH
```
likwid-bench -t copy -w S0:10KB:1
```

## Command to set kernal paranoid level
```
sudo sysctl kernel.perf_event_paranoid=-1
```
# SETTING UP RODINIA

```
git clone https://github.com/yuhc/gpu-rodinia.git
```
Download the dataset from the following link https://www.dropbox.com/s/cc6cozpboht3mtu/rodinia-3.1-data.tar.gz
And extract it.
navigate to the rodinia-data/bfs and then copy graph1MW_6.txt
copy it to the gpu-rodinia\openmp\bfs
```
sudo likwid-perfctr -g CLOCK -C 0 -t 100ms -o bfs_CPI.csv ./bfs 1 graph1MW_6.txt
```
Output is saved to bfs_CPI.csv 



# SETTING UP GAPBS
```
git clone https://github.com/sbeamer/gapbs.git
```
execute the make file inside the gapbs.
Then run the foloowing 
```
sudo likwid-perfctr -g CLOCK -C 0 -t 100ms -o bfs_TABLE.csv ./bfs -g 20 -n 10
```
Output is saved to bfs_TABLE.csv 




## Installing icc

Add the Intel oneAPI repository and GPG key:
```
wget -qO - https://apt.repos.intel.com/oneapi/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB | sudo apt-key add -
echo "deb https://apt.repos.intel.com/oneapi all main" | sudo tee /etc/apt/sources.list.d/oneAPI.list
sudo apt update   
```
Install the Base Toolkit:
```
sudo apt install intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic
```
The installation directory is typically /opt/intel/oneapi.
after installation, you need to set up the environment variables to use the compiler. The most straightforward way is to source the setvars.sh script:
```
source /opt/intel/oneapi/setvars.sh
```
DATA
Cache Topology
********************************************************************************
Level:			1
Size:			32 kB
Type:			Data cache
Associativity:		8
Number of sets:		64
Cache line size:	64
Cache type:		Non Inclusive
Shared by threads:	2
Cache groups:		( 0 2 ) ( 1 3 )
--------------------------------------------------------------------------------
Level:			2
Size:			256 kB
Type:			Unified cache
Associativity:		4
Number of sets:		1024
Cache line size:	64
Cache type:		Non Inclusive
Shared by threads:	2
Cache groups:		( 0 2 ) ( 1 3 )
--------------------------------------------------------------------------------
Level:			3
Size:			3 MB
Type:			Unified cache
Associativity:		12
Number of sets:		4096
Cache line size:	64
Cache type:		Inclusive
Shared by threads:	4
Cache groups:		( 0 2 1 3 )


graph
https://www.desmos.com/calculator/4vyvqpzaxl

# PLOTTING USING GNU

````
set xlabel "x"
set ylabel "y"
# set key left top

# Control axis ranges and step size
set xtics 0.5
set ytics 0.5

# (Optional) force x and y ranges
set xrange [-5:5]
set yrange [0:4]

# Increase sampling density for smoother curves
# set samples 1000

plot \
    log10(34558.72) + x title "L1 CACHE", \
    log10(26874.7) + x title "L2 CACHE", \
    log10(23663.28) + x title "L3 CACHE", \
    log10(14092.25) + x title "DRAM", \
    log10(4519.81) title "PEAK-MFLOPS"

````
# DESMOS PLOT 
https://www.desmos.com/calculator/4vyvqpzaxl
