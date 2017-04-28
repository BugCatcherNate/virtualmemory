inputf = open("vminput.txt", 'r')
readyqueue = []
waiting = []
frame = []
framesize = 3
multidegree = 2
quantum = 2
time = 0
pagefaults = 0

def readinputfile():
	
	while True:
		
		job = (inputf.readline()).split()
		
		if not job:
			break
    
		identifier = job[0]
		numberofpages = job[1]
   

		if identifier.isalpha():
    		
			waiting.append([identifier, [],[]])
			currenthread = len(readyqueue)-1
        	
		else:
			waiting[currenthread][1].append([int(job[0]), int(job[1])])
			waiting[currenthread][2].append(time)
			waiting[currenthread][2].append(0)
			waiting[currenthread][2].append(0)
			waiting[currenthread][2].append(0)
			waiting[currenthread][2].append(numberofpages)
              
	numberofjobs = len(waiting)
	print(waiting)
	for i in range(multidegree):
		if(len(waiting) == 0):
			break
		toadd = waiting.pop(0)
		toadd[2][0] = time
		readyqueue.append(toadd)
	
def cpu():
	
	processing = readyqueue.pop(0)
	global time

	for tick in range(0,quantum):
	
		processpage = processing[1][0]
		if(processpage[0] > 0):
			processing[2][2]+=1
			if(framecheck(processpage[0]) == False):
				time = time + 7
				print("Page fault for page", processpage[0], "at time", time)
				processing[2][1] += 1
			else:
				processing[2][2] += 1

		print("Processing",processing[0], " task:", processpage[0], "at time", time)
		time = time + 1
		processpage[1] = processpage[1] -1
		if(processpage[1] == 0):
			processing[1].pop(0)
		
		if(processpage[0] == -3):

			print(processing[0], "completed at time", time, ", Process start time:", processing[2][0], ", Elapsed time:", time - processing[2][0],", Cpu time:", processing[2][2], ", Pages used:", processing[2][3], ", Number of page faults:", processing[2][1], ", Page Fault Rate:", (processing[2][1]/processing[2][2])*100,"%")
			if(len(waiting) > 0):
				toadd = waiting.pop(0)
				toadd[2][0] = time
				readyqueue.append(toadd)

			break
		if(processpage[0] == -4):

			print(processing[0], "error at time", time, ", Process start time:", processing[2][0], ", Elapsed time:", time - processing[2][0],", Cpu time:", processing[2][2], ", Pages used:", processing[2][3], ", Number of page faults:", processing[2][1], ", Page Fault Rate:", (processing[2][1]/processing[2][2])*100,"%")
			if(len(waiting) > 0):
				toadd = waiting.pop(0)
				toadd[2][0] = time
				readyqueue.append(toadd)

			break

	if(processpage[0] != -3 and processpage[0] != -4):

		readyqueue.append(processing)

def findframe(page):

	for row, i in enumerate(frame):
		try:
			column = i.index(page)
		except ValueError:
			continue
		
		return(row)
def FIFO(page):

	smallest = min([l[1] for l in frame])
	toreplace = findframe(smallest)
	frame[toreplace] = [page, time, time]
	

def LRU(page):
	
	smallest = min([l[2] for l in frame])
	toreplace = findframe(smallest)
	frame[toreplace] = [page, time, time]
	

def framecheck(page):

	if page not in [l[0] for l in frame]:
		global pagefaults
		pagefaults += 1
		if(len(frame) < framesize):
			frame.append([page, time, time])
		else:
			LRU(page)
		return False
	else:
		temp = findframe(page)
		frame[temp][2] = time
		return True


readinputfile()

while(len(readyqueue) > 0):
	cpu()

print("Finished at time:", time, ", Page Faults:", pagefaults)

