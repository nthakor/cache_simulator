# Cache Simulator

This folder contains hierarchical cache simulator developed for multi-way fully and set associate cache read and write. 

Following are input parameters

  - ``` -t trace file in .txt format ```
  - ``` -w number of ways integer```
  - ``` -s number of sets integer```
  - ```-size size of cache in kb integer```
  - ```-type  f or s for fully and set associative respectively```

#Note
	Parameters for L1,L2 and L3 are separated by "_"
#Demo Input
``` python main.py -t data.txt -w 16_8_4 -s 256_128_64 -size 256_64_16 -type f_s_f```

#Writing Method

We are using no write allocate policy.
Suppose the data we are writing is already in L1,well and good.
-If it is L2, Update it’s value in L2 and write the same in L1
-If in L3, write in L2 as well as L1
-If it’s nowhere present write in L1.

# Output

  - Print out hits and misses for all caches
  - We are assuming that number of stall cycles are equal to number of missed

