# virtualmemory

Example virtual memory page replacement algorithms from Masters OS (McGuire)

input file is vminput.txt

Each successive line will be a pair of integers.  This pair  will represent either
	 A page number in the range 1…maxPagesForJob, and the number of time units spent processing that page, or
	-1 to represent a system call, and the number of time units spent processing that call, or
	-2 to represent an i/o call, and the number of time units spent processing i/0, or
	-3 to represent job termination, with the second number being zero, or
	-4 to represent a run time error, with the second number being the amount of time to process that error and terminate the job.
	
CPU scheduling is Round Robin with a variable time quantum
Page replacement can be set as LRU or FIFO
Maximum number of pages in frame can be set
Degree of multiprogramming can also be set

