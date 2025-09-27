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

