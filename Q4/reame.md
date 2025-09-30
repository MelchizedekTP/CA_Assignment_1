# CPI STACK CALCULATION

## RODINIA BENCHMARK

The data about L1-I cache miss,L1-D cache miss,L2 cache miss,L3 cache miss, Branch miss-prediction, I-TLB miss, D-TLB miss were collected by running the bfs program as it was done in the previous question.

````
perf stat -e L1-dcache-load-misses,L1-icache-load-misses,l2_rqsts.miss,dTLB-load-misses,iTLB-load-misses,br_misp_retired.all_branches_pebs,cycles,instructions -I 10 -x, -o rodinia_data.csv ./bfs graph33554432.txt 1
````

The python script data_processin.py is run to convert the data from rodinia_data.csv to a format X,Y which can be used for training the regression model.
(NOTE: The rodinia_data.csv should be in the same directory as the python script).
The processed data is stored in a new csv file rodinia_processed_data.csv where X is a list where each entry is a tuple with 7 values which were measured using perf and Y has the CPI values.

````
python data_processin.py
````

Now the model.py is run to train the regression model which takes the rodinia_processed_data.csv as input and output the parameters of the model.

````
python model.py
````


## GAPBS BENCHMARK

The data about L1-I cache miss,L1-D cache miss,L2 cache miss,L3 cache miss, Branch miss-prediction, I-TLB miss, D-TLB miss were collected by running the bfs program as it was done in the previous question.

````
perf stat -e L1-dcache-load-misses,L1-icache-load-misses,l2_rqsts.miss,dTLB-load-misses,iTLB-load-misses,br_misp_retired.all_branches_pebs,cycles,instructions -I 10 -x, -o rodinia_data.csv ./bfs -u 25 -n 1
````

The python script data_processin.py is run to convert the data from rodinia_data.csv to a format X,Y which can be used for training the regression model.
(NOTE: The gapbs_data.csv should be in the same directory as the python script).
The processed data is stored in a new csv file gapbs_processed_data.csv where X is a list where each entry is a tuple with 7 values which were measured using perf and Y has the CPI values.

````
python data_processin.py
````

Now the model.py is run to train the regression model which takes the gapbs_processed_data.csv as input and output the parameters of the model.

````
python model.py
````
