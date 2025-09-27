# Q1
## Part 1
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
|mem_load_retired.l3_miss| |
|fp_arith_inst_retired.scalar_single||
|User time||

graph
https://www.desmos.com/calculator/4vyvqpzaxl

## part 2
| Event | Count|
|-------|------|
|mem_load_retired.l3_miss| |
|fp_arith_inst_retired.scalar_single||
|User time||

## part 3
| Event | Count|
|-------|------|
|mem_load_retired.l3_miss| |
|fp_arith_inst_retired.scalar_single||
|User time||

## part 3
| Event | Count|
|-------|------|
|mem_load_retired.l3_miss| |
|fp_arith_inst_retired.scalar_single||
|User time||




#PLOTTING USING GNU

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

