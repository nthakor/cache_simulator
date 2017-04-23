import csv,argparse,math
import numpy as np
import itertools
parser = argparse.ArgumentParser(description='Simulate a cache')
parser.add_argument('-t', '--trace_file', help='Tracefile containing instructions', required=True)
parser.add_argument('-w', '--ways', help='Number of Ways', required=True,type=int)
parser.add_argument('-size', '--cache_size', help='Size of Cache in KB', required=True,type=int)
parser.add_argument('-s', '--set', help='Number of set', required=True,type=int)
arguments = vars(parser.parse_args())

cache=np.zeros(shape=[arguments['set'],arguments['ways'],2])
tag_block=np.zeros(shape=[arguments['set'],arguments['ways']])
cache[:]=np.NAN
tag_block[:]=np.NAN
miss=0
hits=0
with open(arguments['trace_file'], 'rb') as csvfile:
	param_read = csv.reader(csvfile, delimiter=' ', quotechar='|')
	time=0
	for row in param_read:
		time+=1
		optype=row[0] #typr of Operation
		cache_add=str(row[1])[2:] #memory address of cache
		address_size = len(cache_add) * 4 
		bin_add = bin(int(cache_add, 16))[2:].zfill(address_size)
		idx=row[2] #number of non-memory operation before this one
		index_bit=int(math.log(arguments['set'],2)) #size of index bit
		# block_size=(arguments['cache_size']*pow(2,10))/(arguments['set']*arguments['ways']) 
		block_size=(arguments['cache_size'])/(arguments['set']*arguments['ways']) 
		offset_bit=int(math.log(block_size,2)) #size of offset bits
		block_offset = bin_add[-offset_bit:] #offset bits points to memory location
		index = bin_add[-(offset_bit+index_bit):-offset_bit] #index bits points to set
		tag = bin_add[:-(offset_bit+index_bit)] #tag value
		indexNum=int(index,2) #decimal value of index
		blockNum=int(block_offset,2) #decimal value of block
		tagNum=int(tag,2) #decimal value of tag 
		ways=arguments['ways']
		nanInd=[0,0]
		nanExist=False
		hitOccur=False
		# minTime
		r=np.arange(arguments['set'])
		c=np.arange(arguments['ways'])
		for x,y in itertools.product(r,c):
			# print x,y
			if(cache[x,y,0]==blockNum):
				hits+=1
				print "hit"
				hitOccur=True
				cache[x,y,1]=time
				break
			elif(np.isnan(cache[x,y,0]) and nanExist==False):
				nanExist=True
				nanInd=[x,y]
				# print "nanChanged"
				# break
			else:
				pass
		if(hitOccur==False):
			if(nanExist):
				n1,n2=nanInd
				cache[n1,n2,0]=blockNum		
				cache[n1,n2,1]=time
				miss+=1
				# print "miss"
				print "bcz adding first time"
			else:
				idx=np.nanargmin(cache[:,:,1])
				shape1=cache[:,:,1].shape[1]
				r=int(idx%shape1)
				c=int((idx-r)/shape1)
				print "minTime Before replacing: %d"%(np.min(cache[:,:,1])),
				print "minTime accrd to calcul: %d"%(cache[c,r,1]),
				cache[r,c,0]=blockNum
				cache[r,c,1]=time
				miss+=1
				# print "miss"
				print "replacing"

		# break




# for x in cache:
# 	for i in range(len(x)):
# 		print "%.2f (%.2f) \t |"%(x[i][0],x[i][1]),

print "Hits: %d Miss: %d"%(hits,miss)
	# print "\n"



print miss
