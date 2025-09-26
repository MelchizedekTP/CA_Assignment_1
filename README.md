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
