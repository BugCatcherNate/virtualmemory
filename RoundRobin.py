
# Author: Nathan Thompson
# Date: 4/29/2017


from math import ceil
inputf = open("vminput.txt", 'r')  # input file
readyqueue, waiting, frame = ([], [], [])
framesize, multidegree, quantum = (1, 3, 200)  # default initialization
# Initializing time, pagefaults, pagereads
time, pagefaults, pagereads = (0, 0, 0)


def readinputfile():

    while True:

        job = (inputf.readline()).split()  # parse input

        if not job:
            break  # if no more lines in input file then break from while loop

        identifier = job[0]  # identifier is (a,-1,-3, etc.  )

        if identifier.isalpha():  # If identifier is job

            waiting.append([identifier, [], []])
            currenthread = len(readyqueue) - 1

        else:  # else add the process to the job page list
            waiting[currenthread][1].append([int(job[0]), int(job[1])])
            waiting[currenthread][2].extend((time, 0, 0, 0, int(job[1])))

    # define number of jobs in batch based on waiting queue size
    numberofjobs = len(waiting)

    # move jobs from waiting queue to ready queue based on muliprogramming
    # degree
    for i in range(multidegree):

        if(len(waiting) == 0):
            break
        else:
            toadd = waiting.pop(0)
            toadd[2][0] = time
            readyqueue.append(toadd)


def cpu():

    # removes job from ready queue for processing
    processing = readyqueue.pop(0)
    global time
    global pagereads

    for tick in range(0, quantum):

        processpage = processing[1][0]

        if(processpage[0] > 0):  # if taks requires page
            pagereads += 1  # increments total number of page reads for the batch
            processing[2][2] += 1
            if(framecheck(processpage[0]) == False):
                time += 7
                #print("--> Page fault for page", processpage[0], "at time", time)
                processing[2][1] += 1

        time += 1  # Increment cpu tick
        processpage[1] -= 1  # Decrement cpu time for process
        if(processpage[1] == 0):
            processing[1].pop(0)  # Page from job page list if completed

        if(processpage[0] == -3):

            print("--> Process:", processing[0], "completed at time", time, ", Process start time:", processing[2][0], ", Elapsed time:", time - processing[2][0], ", Cpu time:", processing[
                  2][2], ", Pages used:", processing[2][4], ", Number of page faults:", processing[2][1])
            print("--------------------------------------------------------")

            checkwaiting()  # Move process from waiting queue to ready queue

            break
        # If error state is encountered then remove job and print statistics
        # for the job
        if(processpage[0] == -4):

            print("--> Process:", processing[0], "error at time", time, ", Process start time:", processing[2][0], ", Elapsed time:", time - processing[2][0], ", Cpu time:", processing[
                  2][2], ", Pages used:", processing[2][4], ", Number of page faults:", processing[2][1])
            print("--------------------------------------------------------")

            checkwaiting()  # Move process from waiting queue to ready queue

            break

    # If process has not completed or encountered runtime error then put it
    # back in the ready queue
    if(processpage[0] != -3 and processpage[0] != -4):

        readyqueue.append(processing)


def findframe(page):  # Used to find page in frame table

    for row, i in enumerate(frame):
        try:
            column = i.index(page)
        except ValueError:
            continue

        return(row)


def checkwaiting():  # used to move waiting queue to ready queue

    if(len(waiting) > 0):
        toadd = waiting.pop(0)
        toadd[2][0] = time
        readyqueue.append(toadd)


def FIFO(page):

    # retrieves the page with the smallest time entering into frame table
    smallest = min([l[1] for l in frame])
    toreplace = findframe(smallest)
    # updates the page, time entered frame, and time used
    frame[toreplace] = [page, time, time]


def LRU(page):

    # retrieves the page with the smallest time last used
    smallest = min([l[2] for l in frame])
    toreplace = findframe(smallest)
    frame[toreplace] = [page, time, time]


def framecheck(page):

    # checks if page is in frame and implements the indicated replacement
    # algorithm if the page is not found
    if page not in [l[0] for l in frame]:
        global pagefaults
        pagefaults += 1
        if(len(frame) < framesize):
            frame.append([page, time, time])
        else:
            if(answer == "f"):

                FIFO(page)
            else:
                LRU(page)

        return False
    else:
        temp = findframe(page)
        frame[temp][2] = time
        return True

if __name__ == '__main__':  # main loop with user input

    framesize = int(input("--> Indicate frame size: "))
    quantum = int(input("--> Indicate time quantum: "))
    multidegree = int(input("--> Indicate degree of multiprogramming: "))
    answer = input("--> Indicate FIFO or LRU (f/l): ")
    readinputfile()
    while(len(readyqueue) > 0):  # Runs main cpu process while the ready queue is not empty
        cpu()

    print("--> Batch Finished at time:", time, ", Page Faults:",
          pagefaults, ", Page Fault Rate:", ceil((pagefaults / pagereads) * 100), "%")
