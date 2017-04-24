# virtualmemory

Example virtual memory page replacement algorithms from Masters OS (McQuire)

input file is vminput.txt

Each successive line will be a pair of integers.  This pair  will represent either
	 A page number in the range 1…maxPagesForJob, and the number of time units spent processing that page, or
	-1 to represent a system call, and the number of time units spent processing that call, or
	-2 to represent an i/o call, and the number of time units spent processing i/0, or
	-3 to represent job termination, with the second number being zero, or
	-4 to represent a run time error, with the second number being the amount of time to process that error and terminate the job.

