# P1
## Common set-up for both B1,B2 problems
### Isolating cpu core
Note: These commands are specific to Linux distributions

go to directory '/etc/default/grub'
```
cd /etc/default/grub
```
update grup file in that directory
```
GRUB_CMDLINE_LINUX="isolcpus=0"
```
This stops the kernel from assigning processes to core : 0

Next update kernel
```
sudo update-grub
```
Reboot the system for this to take effect

### To run program on specific core
```
taskset -a --cpu-list 0 ./program
```

### Construction of roofline model
To get the specification of the CPU, Likwid was used

To install Likwid:
```
sudo apt install likwid
```

To get the specification
```
likwid-topology -c
```
To get peak flops
```
likwid-bench -t peakflops_sp -w S0:10KB:1
```
To get L1 cache bandwidth
```
likwid-bench -t copy -w S0:10KB:1
```
To get L2 cache bandwidth
```
likwid-bench -t copy -w S0:200KB:1
```
To get L3 cache bandwidth
```
likwid-bench -t copy -w S0:10MB:1
```
To get DRAM bandwidth
```
likwid-bench -t copy -w S0:100MB:1
```
Perf

To get performance counters perf was used. Perf comes as default in linux-tools. If your kernel doesnt have latest linux-tools, you can download the latest available version from https://www.kernel.org/. 

Note: To run perf commands its neccassry to set perf kernel paranoid level to -1. To do that 
```
sudo sysctl kernel.perf_event_paranoid=-1
```

## B1
### 1. Simple-i,j,k loop order
Compiling C program

```
gcc matmul1.c -o matmult1.out
```
perf command to get performance counters
```
taskset -a --cpu-list 0 perf stat -e mem_load_retired.l3_miss,fp_arith_inst_retired.scalar_single ./matmult1.out
```
Output:
| Event | Count|
|-------|------|
|mem_load_retired.l3_miss|2,356,412,522 |
|fp_arith_inst_retired.scalar_single|137,440,118,132|
|seconds time elapsed|1065.093355483|
|seconds user|1061.926462000|
|seconds sys|1.950318000|



### 2. Simple-k,i,j loop with permuted order
Compiling C program

```
gcc matmul2.c -o matmult2.out
```
perf command to get performance counters
```
taskset -a --cpu-list 0 perf stat -e mem_load_retired.l3_miss,fp_arith_inst_retired.scalar_single ./matmult2.out
```
output:
| Event | Count|
|-------|------|
|mem_load_retired.l3_miss|105,131,069 |
|fp_arith_inst_retired.scalar_single|137,439,424,834|
|seconds time elapsed|410.306275995|
|  seconds user| 409.474765000 |
|  seconds sys|  0.561660000|

### 3. Tiled-i,j,k loop order
Compiling C program

```
gcc matmul3.c -o matmult3.out
```
perf command to get performance counters
```
taskset -a --cpu-list 0 perf stat -e mem_load_retired.l3_miss,fp_arith_inst_retired.scalar_single ./matmult3.out
```
output:
| Event | Count|
|-------|------|
|mem_load_retired.l3_miss| 755,909,589|
|fp_arith_inst_retired.scalar_single| 137,439,620,596|
|seconds time elapsed|584.465883184|
|seconds user|582.176800000|
|seconds sys|1.096820000|

### 4. Tiled-k,i,j loop with permuted order
Compiling C program

```
gcc matmul4.c -o matmult4.out
```
perf command to get performance counters
```
taskset -a --cpu-list 0 perf stat -e mem_load_retired.l3_miss,fp_arith_inst_retired.scalar_single ./matmult4.out
```
Output:
| Event | Count|
|-------|------|
|mem_load_retired.l3_miss| 35,783,974|
|fp_arith_inst_retired.scalar_single| 137,439,499,837|
|seconds time elapsed|491.064807996|
|seconds user|490.673976000|
|seconds sys|0.151945000|

## B2
#### GAP Benchmark Suite (GAPS)
Note: Git should be installed (refer https://github.com/git-guides/install-git to install git)

Clone the repo from git:
```
git clone https://github.com/sbeamer/gapbs.git
```
goto folder gaps and run make
```
cd gaps
make
```
also see readme.md file for more details

### Roofline using TEPS

Run this command to get bytes and edges traversed
```
taskset -a --cpu-list 0 perf stat -e mem_load_retired.l3_miss ./bfs -u 25 -n 1
```
`taskset -a --cpu-list 0` set all the task on core 0.

`perf stat -e mem_load_retired.l3_miss` returns memory load instructions that missed L3 cache.

`./bfs -u 25 -n 1 ` creates a uniform graph with 2^25 vertices and runs a breadth first search on that graph , when executed gaps returns the number of edges traversed and perf gets the bytes used and time elapsed.