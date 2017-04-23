import math
import numpy as np
class cache(object):
	def __init__(self, sets,ways,size,a_type):
		self.sets = sets
		self.ways = ways
		self.size = size
		self.cache_block=np.empty(shape=[self.sets,self.ways,2])
		self.tag = np.empty([self.sets,self.ways])
		self.tag[:]=np.NAN
		self.cache_block[:]=np.NAN
		self.type = a_type
		self.hits = 0
		self.misses = 0
		self.time = 0

	def read_write(self,blockNum,indexNum,tagNum):
		self.time+=1
		if(self.type=='s' or self.type=='f'):
			if(np.isnan(self.tag[indexNum][0])):
				self.tag[indexNum][0]=tagNum
				self.cache_block[indexNum][0][0]=blockNum
				self.cache_block[indexNum][0][1]=self.time
				self.misses+=1
				# print "miss"
				# print "miss because all NAN"
			else:
				ways_count=0
				while(ways_count<self.ways):
					if(np.isnan(self.tag[indexNum][ways_count])):
						self.misses+=1
						# print "miss"
						self.tag[indexNum][ways_count]=tagNum
						self.cache_block[indexNum][ways_count][0]=blockNum
						self.cache_block[indexNum][ways_count][1]=self.time
						# print "miss because not in set and set in not empty"
						break
					elif(self.cache_block[indexNum][ways_count][0]==blockNum):
						self.hits+=1
						# print "Hit"
						self.cache_block[indexNum][ways_count][1]=self.time
						break
					elif(ways_count==(self.ways-1) and not np.isnan(self.tag[indexNum][ways_count])):
						LUR=np.argmin(self.cache_block[indexNum,:,1])
						self.misses+=1
						# print "miss"
						# print "miss because set is full and not found"
						self.tag[indexNum][LUR]=tagNum
						self.cache_block[indexNum][LUR][0]=blockNum
						self.cache_block[indexNum][LUR][1]=self.time
						break
					else:
						ways_count+=1


def split_add(add,sets,ways,cache_size):
	address_size = len(add) * 4 
	bin_add = bin(int(add, 16))[2:].zfill(address_size)
	index_bit=int(math.log(sets,2)) #size of index bit
	block_size=(cache_size)/(sets*ways) 
	offset_bit=int(math.log(block_size,2)) #size of offset bits
	block_offset = bin_add[-offset_bit:] #offset bits points to memory location
	index = bin_add[-(offset_bit+index_bit):-offset_bit] #index bits points to set
	tag = bin_add[:-(offset_bit+index_bit)] #tag value
	indexNum=int(index,2) #decimal value of index
	blockNum=int(block_offset,2) #decimal value of block
	tagNum=int(tag,2) #decimal value of tag 
	return blockNum,indexNum,tagNum