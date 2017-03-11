__author__ = "Paarth Bhasin"
__title__ = "Assignment-3 FIT2070: Operating Systems"
__tutor__ = "Hasanul Ferdaus"
__StartDate__ = '20/10/2016'
__studentID__ = 26356104
__LastModified__ = '24/10/2016'
'''
First Come First Serve Scheduler (FCFS)
Uses a queue to implement this scheduling algorithm

OUTPUT:
    - Information about each finished process in sequence of completion
    - Average Turnaround Time
    - Average Waiting Time
    - Throughput

'''
from Process import Process
import queue


class FCFS:
    def __init__(self):
        # Initial constructor of the Scheduler.
        self.lines = open('processes.txt', 'r').readlines()
        self.ready = queue.Queue(len(self.lines))
        self.averageT = 0
        self.count = 0
        self.averageW = 0
        self.throughput = 0

    def run(self):
        # Loading all the data into relevant data structures for later operation and use.

        for line in self.lines:
            words = line.split(' ')
            # print(words)
            p = Process(words[0], int(words[1]), int(words[2]))
            self.ready.append(p)

        self.process()

    '''
        Processing each process in the ready queue following the SRT algorithm.
    '''
    def process(self):
        '''
            The following lines implement the FCFS algorithm of executing processes on their relative entry time in
            the ready queue.

            This queue used is populated by Processes listed in the processes.txt file.
        '''
        while not self.ready.is_empty():
            p = self.ready.serve()
            self.printProcess(p)

        # print(self.count)
        self.stats()

    '''
        Displaying the statistics of this scheduling algorithm upon its completion.
    '''
    def stats(self):

        self.averageT /= len(self.lines)
        self.averageW /= len(self.lines)

        print("Average waiting time: " + str(self.averageW))
        print("Average Turnaround time: " + str(self.averageT))
        self.throughput = len(self.lines) / self.averageT
        print("Throughput: " + str(self.throughput))

    '''
        Displaying the data of the process upon its completion.
    '''
    def printProcess(self, p):
        p.waiting = self.count - p.arrival
        p.start = self.count
        self.count += p.duration
        p.turn = self.count - p.start
        print("Process ID: " + str(p.name))
        print("Waiting time: " + str(p.waiting))
        print("Turnaround time: " + str(p.turn) + "\n\n")
        self.averageT += p.turn
        self.averageW += p.waiting


def main():
    print("FCFS Scheduler")
    FCFS().run()


if __name__ == "__main__":
    main()
