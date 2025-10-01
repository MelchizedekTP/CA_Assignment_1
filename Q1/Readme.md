# P1
## Common set up for both B1,B2 problems
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

To get performance counters perf was used. Perf comes as default in linux-tools. If your kernel doesnt have latest linux-tools, you can download the latest available version from https://www.kernel.org/. 

Note: To run perf commands its neccassry to set perf kernel paranoid level to -1. To do that 
```
sudo sysctl kernel.perf_event_paranoid=-1
```

## B1

### Compiling C program

Simple-i,j,k loop order
Events :
```
mem_load_retired.l3_miss
```
perf command
```
taskset -a --cpu-list 0 perf stat -e mem_load_retired.l3_miss,fp_arith_inst_retired.scalar_single ./test1.out
```
| Event | Count|
|-------|------|
|mem_load_retired.l3_miss|2,356,412,522 |
|fp_arith_inst_retired.scalar_single|137,440,118,132|
|seconds time elapsed|1065.093355483|
|seconds user|1061.926462000|
|seconds sys|1.950318000|

graph
https://www.desmos.com/calculator/4vyvqpzaxl

## part 2
| Event | Count|
|-------|------|
|mem_load_retired.l3_miss|105,131,069 |
|fp_arith_inst_retired.scalar_single|137,439,424,834|
|seconds time elapsed|410.306275995|
|  seconds user| 409.474765000 |
|  seconds sys|  0.561660000|

## part 3
| Event | Count|
|-------|------|
|mem_load_retired.l3_miss| 755,909,589|
|fp_arith_inst_retired.scalar_single| 137,439,620,596|
|seconds time elapsed|584.465883184|
|seconds user|582.176800000|
|seconds sys|1.096820000|

## part 4
| Event | Count|
|-------|------|
|mem_load_retired.l3_miss| 35,783,974|
|fp_arith_inst_retired.scalar_single| 137,439,499,837|
|seconds time elapsed|491.064807996|
|seconds user|490.673976000|
|seconds sys|0.151945000|




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
