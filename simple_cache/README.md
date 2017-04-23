# Cache Simulator

This folder contains cache simulator deveoped for mutliway fully and set associate cache read and write. 

Following are input parameters

  - ``` -t trace file in .txt format ```
  - ``` -w number of ways integer```
  - ``` -s number of sets integer```
  - ```-size size of cache in kb integer```
  - ```-type  f or s for fully and set associative respectively```

# Demo Input
``` python main.py -t data.txt -w 8 -s 256 -size 64 -type f```

# Output

  - Print out hits and misses 
  - We are assuming that number of stall cycles are equal to number of missed

