if(np.isnan(tag_block[indexNum][0])):
	tag_block[indexNum][0]=tagNum
	cache[indexNum][0][0]=blockNum
	cache[indexNum][0][1]=time
	miss+=1
	print "miss because all NAN"
else:
	ways_count=0
	while(ways_count<ways):
		if(np.isnan(tag_block[indexNum][ways_count])):
			miss+=1
			tag_block[indexNum][ways_count]=tagNum
			cache[indexNum][ways_count][0]=blockNum
			cache[indexNum][ways_count][1]=time
			print "miss because not in set and set in not empty"
			break
		elif(cache[indexNum][ways_count][0]==blockNum):
			hits+=1
			cache[indexNum][ways_count][1]=time
			print "Hit"
			break
		elif(ways_count==(ways-1) and not np.isnan(tag_block[indexNum][ways_count])):
			LUR=np.argmin(cache[indexNum,:,1])
			miss+=1
			tag_block[indexNum][LUR]=tagNum
			cache[indexNum][LUR][0]=blockNum
			cache[indexNum][LUR][1]=time
			print "miss because set is full and not found"
			break
		else:
			ways_count+=1