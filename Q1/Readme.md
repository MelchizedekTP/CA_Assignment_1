# Q1
## Part 1
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
|cache| |
