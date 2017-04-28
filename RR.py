
# duplicates allowed
inputf = open("vminput.txt", 'r')

readyqueue = []
done = 0
tasks = []
count = 0
q = 2
while True:

    job = (inputf.readline()).split()
    if not job:
        break
    
    identifier = job[0]
   

    if identifier.isalpha():
        readyqueue.append([identifier, 10, []])
        currenthread = len(readyqueue)-1
    else:
        readyqueue[currenthread][1] = readyqueue[currenthread][1] + int(job[1])
        readyqueue[currenthread][2].append([job[0], int(job[1])])
              
numberofjobs = len(readyqueue)
while done < numberofjobs:

    for job in range(0,numberofjobs):

        for x in range(0,q):
            identity = int(readyqueue[job][2][0][0])
            print(identity)
            if identity != -3:
              


                temp = readyqueue[job][1] - 1
                
                readyqueue[job][2][0][1] = readyqueue[job][2][0][1] - 1
                protemp = readyqueue[job][0]
                readyqueue[job][0] = protemp
                readyqueue[job][1] = temp
                count = count +1 
                print('Time:',count,'Process:', readyqueue[job])
                if readyqueue[job][2][0][1] == 0:
                    readyqueue[job][2].pop(0)
                
           

                    
            else:
                print(readyqueue[job][0], "is done at time", count)
                readyqueue.pop(job)
                numberofjobs = len(readyqueue)
                done = done +1
                


print(readyqueue)
                 
            