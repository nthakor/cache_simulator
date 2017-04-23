class cache(object):
	def __init__(self, sets,ways,size,a_type):
		self.sets = sets
		self.ways = ways
		self.size = size
		self.cache_block=np.empty([self.sets,self,ways,2])
		self.tag = np.empty(self.sets,self.ways)
		self.type = a_type
		self.hits= 0
		self.misses = 0
		self.time = 0

	def read(self,tagNum,indexNum,blockNum):
		if(self.type=='s'):
			if(np.isnan(tag_block[indexNum][0])):
				tag_block[indexNum][0]=tagNum
				self.cache_block[indexNum][0][0]=blockNum
				self.cache_block[indexNum][0][1]=time
				miss+=1
				print "miss because all NAN"
			else:
				ways_count=0
				while(ways_count<ways):
					if(np.isnan(tag_block[indexNum][ways_count])):
						miss+=1
						tag_block[indexNum][ways_count]=tagNum
						self.cache_block[indexNum][ways_count][0]=blockNum
						self.cache_block[indexNum][ways_count][1]=time
						print "miss because not in set and set in not empty"
						break
					elif(self.cache_block[indexNum][ways_count][0]==blockNum):
						hits+=1
						self.cache_block[indexNum][ways_count][1]=time
						print "Hit"
						break
					elif(ways_count==(ways-1) and not np.isnan(tag_block[indexNum][ways_count])):
						LUR=np.argmin(self.cache_block[indexNum,:,1])
						miss+=1
						tag_block[indexNum][LUR]=tagNum
						self.cache_block[indexNum][LUR][0]=blockNum
						self.cache_block[indexNum][LUR][1]=time
						print "miss because set is full and not found"
						break
					else:
						ways_count+=1


		