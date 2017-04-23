import csv,argparse,math
import numpy as np
from utils import cache,split_add
parser = argparse.ArgumentParser(description='Simulate a cache')
parser.add_argument('-t', '--trace_file', help='Tracefile containing instructions', required=True)
parser.add_argument('-w', '--ways', help='Number of Ways', required=True,type=int)
parser.add_argument('-size', '--cache_size', help='Size of Cache in KB', required=True,type=int)
parser.add_argument('-s', '--set', help='Number of set', required=True,type=int)
parser.add_argument('-type', '--c_type', help='associativity type', required=True)
arguments = vars(parser.parse_args())


cache_1=cache(arguments['set'],arguments['ways'],arguments['cache_size'],str(arguments['c_type']))
with open(arguments['trace_file'], 'rb') as csvfile:
	param_read = csv.reader(csvfile, delimiter=' ', quotechar='|')
	time=0
	for row in param_read:
		optype=row[0] #typr of Operation
		add=str(row[1])[2:] #memory address of cache
		idx=row[2] #number of non-memory operation before this one
		blockNum,indexNum,tagNum=split_add(add,arguments['set'],arguments['ways'],arguments['cache_size'])
		cache_1.read_write(blockNum,indexNum,tagNum)

	print "miss: ",cache_1.misses,"Hits:",cache_1.hits
