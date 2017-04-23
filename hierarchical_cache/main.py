import csv,argparse,math
import numpy as np
from utils import cache,split_add
parser = argparse.ArgumentParser(description='Simulate a cache')
parser.add_argument('-t', '--trace_file', help='Tracefile containing instructions', required=True)
parser.add_argument('-w', '--ways', help='Number of Ways', required=True)
parser.add_argument('-size', '--cache_size', help='Size of Cache in KB', required=True)
parser.add_argument('-s', '--sets', help='Number of set', required=True)
parser.add_argument('-type', '--c_type', help='associativity type', required=True)
arguments = vars(parser.parse_args())

sizes=arguments['cache_size']
sizes=sizes.split('_')
sizes=map(int,sizes)

ways=arguments['ways']
ways=ways.split('_')
ways=map(int,ways)

sets=arguments['sets']
sets=sets.split('_')
sets=map(int,sets)

a_type=arguments['c_type']
a_type=a_type.split('_')

L1=cache(sets[0],ways[0],sizes[0],a_type[0])
L2=cache(sets[1],ways[1],sizes[1],a_type[1])
L3=cache(sets[2],ways[2],sizes[2],a_type[2])


with open(arguments['trace_file'], 'rb') as csvfile:
	param_read = csv.reader(csvfile, delimiter=' ', quotechar='|')
	time=0
	for row in param_read:
		optype=row[0] #typr of Operation
		add=str(row[1])[2:] #memory address of cache
		idx=row[2] #number of non-memory operation before this one
		L1_ind=split_add(add,sets[0],ways[0],sizes[0])
		L2_ind=split_add(add,sets[1],ways[1],sizes[1])
		L3_ind=split_add(add,sets[2],ways[2],sizes[2])
		l1_hit=L1.hits
		L1.read_write(L1_ind[0],L1_ind[1],L1_ind[2])
		if(L1.hits>l1_hit):
			pass
		else:
			l2_hit=L2.hits
			L2.read_write(L2_ind[0],L2_ind[1],L2_ind[2])
			if(L2.hits>l2_hit):
				pass
			else:
				L3.read_write(L2_ind[0],L2_ind[1],L2_ind[2])


	print "miss: ",L1.missed,"Hits:",L1.hits,"time:",L1.time
	print "miss: ",L2.missed,"Hits:",L2.hits,"time:",L2.time
	print "miss: ",L3.missed,"Hits:",L3.hits,"time:",L3.time
