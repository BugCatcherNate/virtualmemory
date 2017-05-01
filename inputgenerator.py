import random, string
f = open('generatedinputfile.txt', 'w')
jobs = string.ascii_letters
pages = [1,2,3,4,5,6,7,8,9,10, -1, -2, -4 ]
numberofjobs = int(input("Inicate desired number of jobs to run"))

for i in range(numberofjobs):

	

	joblength = random.randint(10,25)

	s = str(jobs[i]) +' '+ '1'+'\n'

	f.write(s)

	for j in range(joblength):
		if j == joblength -1:
			
			s = '-3 0'+'\n'

			f.write(s)
		elif j == 1:
			s = '1 '+str(random.randint(1,30))+'\n'
		
		else:
			
			s = str(random.choice(pages))+ ' ' +str(random.randint(1,30)) +'\n'
			f.write(s)

