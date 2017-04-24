#!/usr/bin/python
#Page in frame existas as [identifier, timeadded, timelastused]

inputf = open("vminput.txt", 'r')

pframesize = 4
pagefaulttime = 10
count = 0
frame = []
queue = []
errorstate = False
totalpagefaults = 0
totalpages = 0

def process(time, total):

	total = total + time
	return total

def pagereplace(frame, page, count):

	frame[0] = [identifier, count]
	return frame

def FIFO(frame, page):

	print("Frame", frame)
	smallest = min([l[1] for l in frame])
	print("Smallest", smallest)
	#for row, i in enumerate(frame):
	#	try:
	#		column = i.index(smallest)
	#	except ValueError:
	#		continue
	toreplace = findframe(frame, smallest)
	frame[toreplace] = [page, count, count]
	print("After", frame)
	return(frame)
def findframe(frame, page):

	for row, i in enumerate(frame):
		try:
			column = i.index(page)
		except ValueError:
			continue
		print("tofindstuff", row)
		return(row)

while True:
	
	job = (inputf.readline()).split()
	if not job:
		break
	
	identifier = job[0]
	details = int(job[1])

	if identifier.isalpha():
		print("---------------------------------------------------")
		print("Job ", identifier, "added")
		jobdata = [identifier, count, 0, 0, 0, 0] # jobname, time in, time out, number of page faults
		totalpages = totalpages + details
		queue.append(identifier)
		errorstate = False
	elif not errorstate:
		print("---------------------------------------------------")
		if '-' not in identifier:

			if identifier not in [l[0] for l in frame]:

				print("Page fault for page", identifier,"at Tick", count)
				count = count + pagefaulttime;
				jobdata[5] = jobdata[5] + 1
				totalpagefaults = totalpagefaults + 1
				if len(frame) > pframesize -1:
					#frame = pagereplace(frame, identifier, count)
					frame = FIFO(frame, identifier)

				else:

					frame.append([identifier,count, count])

			else:
				print("before", frame) 
				print("Page", identifier, "in frame")
				update = findframe(frame, identifier)
				print(update)
				frame[update][2] = count
				print("after", frame) 
				


			count = process(details, count)


		elif '-1' in identifier:

			count = process(details, count)
			print("System Call at Tick:", count)

		elif '-2' in identifier:

			count = process(details, count)
			print("I/O interupt at Tick:", count)

		elif '-3' in identifier:
		
			print("job", queue.pop(),"finished with", jobdata[5], "page faults")
			print("Statistics--> Page faults:", jobdata[5], "Time in:", jobdata[1], "Time out:", count, "Elapsed time:", count - jobdata[1])

		elif '-4' in identifier:
			print("Run time error for Job", queue[0],"at Tick:", count)
			print("Statistics for",jobdata[0], "--> Page faults:", jobdata[5], "Time in:", jobdata[1], "Time out:", count, "Elapsed time:", count - jobdata[1])
			count = process(details, count)
			errorstate = True
			print("Due to error, job", queue.pop(),"removed")

print("End of Jobs")
print("Batch Statistics --> Total page faults:", totalpagefaults, "Page fault percentage:", (totalpagefaults/totalpages)*100,"%")