# Q1
## Part 1
Events :
```
mem_load_retired.l3_miss
```
perf command
```
taskset -a --cpu-list 0 perf stat -e mem_load_retired.l3_miss ./test1.out
```
| Event | Count|
|-------|------|
|cache| |
