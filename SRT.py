__author__ = "Paarth Bhasin"
__title__ = "Assignment-3 FIT2070: Operating Systems"
__tutor__ = "Hasanul Ferdaus"
__StartDate__ = '20/10/2016'
__studentID__ = 26356104
__LastModified__ = '24/10/2016'

# Using priority queue to handle processes based on time remaining.
from PriorityQueue import PriorityQueue
from Process import Process

'''
Shortest Remaining Time Scheduler (SRT)
Uses a priority queue to implement this scheduling algorithm

OUTPUT:
    - Information about each finished process in sequence of completion
    - Average Turnaround Time
    - Average Waiting Time
    - Throughput
'''

class SRT:
    def __init__(self):
        # Initial Constructor of the Scheduler.
        self.lines = open('processes.txt', 'r').readlines()
        self.ready = PriorityQueue()
        self.all = []
        self.i = 0
        self.finished = 0
        self.program_counter = 0
        self.load_time = []
        self.load_var = 0
        self.averageT = 0
        self.averageW = 0
        self.throughput = 0

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
                self.ready.add(p)
                self.process()
                self.i += 1
            else:
                self.i += 1
    '''
    Processing each process in the ready queue following the SRT algorithm.
    '''

    def process(self):
        p = self.ready.serve()
        print(p.name)
        '''
        The following lines implement the SRT algorithm of choosing the process with the minimum time remaining from the
        the ready queue. This queue is a priority queue and always returns the minimum element in the list based on
        the remaining time.

        This list is populated by Processes listed in the processes.txt file.

        The algorithm also handles preemption when a new process with shorter remaining time than the currently
        executing process is found.
        '''
        if self.ready.count <= 0 < p.duration:
            print("PC: " + str(self.program_counter))
            if self.load_var <= (len(self.load_time) - 2) and self.program_counter < self.load_time[self.load_var + 1]:

                next_load = self.load_time[self.load_var + 1]
                p.duration -= next_load - self.program_counter
                self.program_counter += next_load
                p.start = self.program_counter
                self.load_var += 1

                if self.all[self.load_var].duration < p.duration:
                    print("Preempt")
                    p1 = self.all[self.load_var]
                    self.ready.add(p)
                    self.ready.add(p1)
                    self.process()
                else:
                    p1 = self.all[self.load_var]
                    self.ready.add(p1)
                    self.program_counter += p.duration
                    self.printProcess(p)
                    if self.finished == len(self.lines):
                        self.stats()
                        exit(0)
                    else:
                        self.process()

            elif self.load_var <= (len(self.load_time) - 2) and self.program_counter > self.load_time[
                        self.load_var + 1]:
                self.program_counter += p.duration
                self.printProcess(p)
                print("PC: " + str(self.program_counter))
                if self.finished == len(self.lines):
                    self.stats()
                    exit(0)
                else:
                    self.process()

            elif self.load_var > (len(self.load_time) - 2):
                self.program_counter += p.duration
                print("PC: " + str(self.program_counter))
                self.printProcess(p)
                self.load_var += 1
                if self.finished == len(self.lines):
                    self.stats()
                    exit(0)
                else:
                    self.process()

        elif self.ready.count > 0 and p.duration > 0:

            print("PC: " + str(self.program_counter))
            p1 = self.ready.serve()
            # self.ready.add(p1)
            print(self.load_var)
            if self.load_var <= (len(self.load_time) - 2) and self.program_counter < self.load_time[self.load_var + 1]:
                if p1.duration == p.duration:
                    if p1.arrival < p.arrival:
                        self.ready.add(p)
                        # next_load = self.load_time[self.load_var]
                        self.program_counter -= p1.duration
                        p1.duration = 0
                        p1.start = self.program_counter
                        self.process()
                        # self.load_var += 1
                        if self.all[self.load_var].duration < p1.duration:
                            p = self.all[self.load_var]
                            self.ready.add(p)
                            self.ready.add(p1)
                            self.process()

                        else:

                            p = self.all[self.load_var]
                            self.ready.add(p)
                            self.program_counter += p1.duration
                            self.printProcess(p1)
                            if self.finished == len(self.lines):
                                self.stats()
                                exit(0)
                            else:
                                self.process()

                    else:
                        self.ready.add(p1)
                        next_load = self.load_time[self.load_var + 1]
                        p.duration -= next_load - self.program_counter
                        self.program_counter += next_load - self.program_counter
                        p.start = self.program_counter
                        self.load_var += 1

                        if self.all[self.load_var].duration < p.duration:
                            p1 = self.all[self.load_var]
                            self.ready.add(p)
                            self.ready.add(p1)
                            self.process()

                        else:

                            p1 = self.all[self.load_var]
                            self.ready.add(p1)
                            self.program_counter += p.duration
                            self.printProcess(p)
                            if self.finished == len(self.lines):
                                self.stats()
                                exit(0)
                            else:
                                self.process()
                else:
                    # print("1234")
                    self.ready.add(p1)
                    # self.ready.add(p1)
                    next_load = self.load_time[self.load_var + 1]
                    p.duration -= next_load - self.program_counter
                    p.start = self.program_counter
                    self.program_counter += next_load - self.program_counter
                    self.load_var += 1

                    if self.all[self.load_var].duration < p.duration:
                        p1 = self.all[self.load_var]
                        self.ready.add(p)
                        self.ready.add(p1)
                        self.finished += 1
                        if self.finished == len(self.lines):
                            self.stats()
                            exit(0)
                        else:
                            self.process()

                    else:

                        p1 = self.all[self.load_var]
                        self.ready.add(p1)
                        self.program_counter += p.duration
                        self.printProcess(p)
                        if self.finished == len(self.lines):
                            self.stats()
                            exit(0)
                        else:
                            self.process()

            elif self.load_var <= (len(self.load_time) - 2) and self.program_counter == self.load_time[
                        self.load_var + 1]:
                p2 = self.all[self.load_var + 1]
                if p.duration == p1.duration:
                    if p1.arrival >= p.arrival:
                        self.ready.add(p1)
                        if p2.duration < p.duration:
                            self.ready.add(p)
                            p = p2
                            self.program_counter += p.duration
                            self.printProcess(p)
                            if self.finished == len(self.lines):
                                self.stats()
                                exit(0)
                            else:
                                self.process()
                        else:
                            self.ready.add(p2)
                            self.program_counter += p.duration
                            self.printProcess(p)
                            if self.finished == len(self.lines):
                                self.stats()
                                exit(0)
                            else:
                                self.process()
                    else:
                        self.ready.add(p)
                        if p2.duration < p1.duration:
                            self.ready.add(p1)
                            p = p2
                            self.program_counter += p.duration
                            self.printProcess(p)
                            if self.finished == len(self.lines):
                                self.stats()
                                exit(0)
                            else:
                                self.process()

                        else:
                            self.ready.add(p2)
                            p = p1
                            self.program_counter += p.duration
                            self.printProcess(p)
                            if self.finished == len(self.lines):
                                self.stats()
                                exit(0)
                            else:
                                self.process()

                else:
                    self.ready.add(p1)
                    if p2.duration < p.duration:
                        self.ready.add(p)
                        p = p2
                        self.program_counter += p.duration
                        self.printProcess(p)
                        if self.finished == len(self.lines):
                            self.stats()
                            exit(0)
                        else:
                            self.process()
                    else:
                        self.ready.add(p2)
                        self.program_counter += p.duration
                        self.printProcess(p)
                        if self.finished == len(self.lines):
                            self.stats()
                            exit(0)
                        else:
                            self.process()

            elif self.load_var <= (len(self.load_time) - 2) and self.program_counter > self.load_time[
                        self.load_var + 1]:

                if p.duration == p1.duration:
                    if p.arrival <= p1.arrival:
                        self.ready.add(p1)
                        p.arrival = self.load_time[self.load_var]
                        self.program_counter += p.duration
                        print("PC: " + str(self.program_counter))
                        self.printProcess(p)
                        if self.finished == len(self.lines):
                            self.stats()
                            exit(0)
                        else:
                            self.process()
                    else:
                        self.ready.add(p)
                        p1.start = self.program_counter
                        p1.arrival += p1.duration
                        self.program_counter += p1.duration
                        self.printProcess(p1)
                        if self.finished == len(self.lines):
                            self.stats()
                            exit(0)
                        else:
                            self.process()

                else:
                    # print("GM Holden")
                    self.ready.add(p1)
                    self.program_counter += p.duration
                    print("PC: " + str(self.program_counter))
                    p.arrival = self.load_time[self.load_var]
                    self.printProcess(p)
                    self.load_var += 1
                    if self.finished == len(self.lines):
                        self.stats()
                        exit(0)
                    else:
                        self.process()

            elif self.load_var > (len(self.load_time) - 2):
                if p.duration < p1.duration:
                    p.start = self.program_counter
                    self.ready.add(p1)
                    self.printProcess(p)
                    print("PC: " + str(self.program_counter))
                    if self.finished == len(self.lines):
                        self.stats()
                        exit(0)
                    else:
                        self.process()
                elif p.duration > p1.duration:
                    self.ready.add(p)
                    p = p1
                    p.start = self.program_counter
                    self.printProcess(p)
                    # print("PC: " + str(self.program_counter))
                    if self.finished == len(self.lines):
                        self.stats()
                        exit(0)
                    else:
                        self.process()

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

        p.waiting += p.start - p.arrival
        # self.program_counter += p.duration
        p.turn += self.program_counter - p.start
        p.duration = 0
        self.averageT += p.turn
        self.averageW += p.waiting
        print("Process ID: " + p.name)
        print("Waiting time: " + str(p.waiting))
        print("Turnaround Time: " + str(p.turn))
        self.finished += 1


def main():
    print("SRT Scheduler\n")
    SRT().run()


if __name__ == "__main__":
    main()
