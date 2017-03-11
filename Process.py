__author__ = "Paarth Bhasin"
__title__ = "Assignment-3 FIT2070: Operating Systems"
__tutor__ = "Hasanul Ferdaus"
__StartDate__ = '20/8/2016'
__studentID__ = 26356104
__LastModified__ = '24/10/2016'


class Process:
    def __init__(self, name="", start=0, duration=0):
        self.name = name
        self.start = start
        self.duration = duration
        self.waiting = 0
        self.turn = 0
        self.arrival = start
        assert isinstance(self.name, str)
        assert isinstance(self.turn, int)
        assert isinstance(self.start, int)
        assert isinstance(self.duration, int)
        assert isinstance(self.waiting, int)
        assert isinstance(self.arrival, int)
