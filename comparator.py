__author__ = "Paarth Bhasin"
__title__ = "Assignment-3 FIT2070: Operating Systems"
__tutor__ = "Hasanul Ferdaus"
__StartDate__ = '22/8/2016'
__studentID__ = 26356104
__LastModified__ = '31/8/2016'

from FCFS import FCFS
from RoundRobin import RoundRobin
from SRT import SRT


def main():
    fcfs = FCFS()
    rr = RoundRobin()
    srt = SRT()
    print("FCFS Scheduler")
    fcfs.run()
    print("Round Robin Scheduler")
    rr.run()
    print("Shortest Remaining Time Scheduler")
    srt.run()


if __name__ == "__main__":
    main()
