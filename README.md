# CA Assignment 1

## Isolate cpu core
go to:
```
cd /etc/default/grub
```
update grup file
```
GRUB_CMDLINE_LINUX="isolcpus=0"
```
update kernel
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
