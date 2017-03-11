__author__ = "Paarth Bhasin"
__title__ = "Assignment-3 FIT2070: Operating Systems"
__tutor__ = "Hasanul Ferdaus"
__StartDate__ = '20/10/2016'
__studentID__ = 26356104
__LastModified__ = '24/10/2016'

from Process import Process
import queue
import os

'''
Round Robin Scheduler (RR)
Uses a queue to implement this scheduling algorithm

OUTPUT:
    - Information about each finished process in sequence of completion
    - Average Turnaround Time
    - Average Waiting Time
    - Throughput

'''


class RoundRobin:
    # Initial Constructor of the Scheduler.
    def __init__(self):
        self.lines = open('processes.txt', 'r').readlines()
        self.ready = queue.Queue(len(self.lines))
        self.i = 0
        self.load_var = 0
        self.program_counter = 0
        self.time_quantum = 2
        self.all = []
        self.load_time = []
        self.averageT = 0
        self.averageW = 0
        self.throughput = 0
        self.passed = 0

    def run(self):
        # Loading all the data into relevant data structures for later operation and use.
        for line in self.lines:
            words = line.split(' ')
            p = Process(words[0], int(words[1]), int(words[2]))
            self.load_time.append(int(words[1]))
            self.all.append(p)

        while self.i < len(self.lines):
            p = self.all[self.i]
            if p.start == self.program_counter:
                self.ready.append(p)
                self.process()
                self.i += 1
            else:
                self.program_counter += 1
                self.i += 1

    '''
       Processing each process in the ready queue following the SRT algorithm.
    '''
    def process(self):
        '''
            The following lines implement the Round Robin algorithm of executing processes based on a time quantum value
            set initially in the constructor.

            This queue used is populated by Processes listed in the processes.txt file.
        '''
        p = self.ready.serve()
        print(p.name)
        if p.duration <= 0:
            p.duration = 0

        if not self.ready.is_empty() and p.duration > 0:
            p.duration -= self.time_quantum
            if p.duration <= 0:
                # Displaying data upon its completion
                self.program_counter += self.time_quantum + p.duration
                # Process completed
                p.duration = 0
                p.turn = self.program_counter - p.start
                p.waiting += self.program_counter - p.start
                print("Process ID: " + str(p.name))
                print("Turnaround time: " + str(p.turn) + '\n')
                self.averageT += p.turn
                self.averageW += p.waiting
                self.process()
            else:
                p.waiting += self.program_counter - p.start
                self.ready.append(p)
                p.start = self.program_counter
                self.program_counter += self.time_quantum
                self.process()

        elif self.ready.is_empty() and p.duration > 0:
            print("PC: " + str(self.program_counter))
            if self.load_var <= (len(self.load_time) - 2) and self.program_counter <= self.load_time[self.load_var + 1]:
                print(p.duration)
                p.duration -= self.time_quantum
                self.program_counter += self.load_time[self.load_var] + self.time_quantum
                self.ready.append(p)
                self.process()
            else:
                self.load_var += 1
                # print("Load var " + str(self.load_var))
                if self.load_var < len(self.load_time):
                    p1 = self.all[self.load_var]
                    self.ready.append(p1)
                    self.ready.append(p)
                    self.process()
                else:
                    '''
                        Displaying the data of the process upon its completion.
                    '''
                    self.program_counter += p.duration
                    print("PC: " + str(self.program_counter))
                    p.duration = 0
                    p.turn = self.program_counter - p.arrival
                    p.waiting = self.program_counter - p.start
                    print("Process ID: " + str(p.name))
                    print("Turnaround time: " + str(p.turn) + '\n')
                    self.averageT += p.turn
                    self.averageW += p.waiting
                    self.stats()
                    os._exit(0)

        if p.duration <= 0:
            p.duration = 0
            p.turn = (p.arrival + self.program_counter) - p.start
            p.waiting += self.program_counter - p.start
            print("Process ID: " + str(p.name))
            print("Turnaround time: " + str(p.turn) + '\n')
            self.averageT += p.turn
            self.averageW += p.waiting

    '''
    Displaying the statistics of this scheduling algorithm upon its completion.
    '''
    def stats(self):
        print(self.program_counter)
        self.averageT /= len(self.lines)
        self.averageW /= len(self.lines)

        print("Average waiting time: " + str(self.averageW))
        print("Average Turnaround time: " + str(self.averageT))
        self.throughput = len(self.lines) / self.averageT
        print("Throughput: " + str(self.throughput))


def main():
    print("Round Robin Scheduler")
    RoundRobin().run()


if __name__ == "__main__":
    main()
