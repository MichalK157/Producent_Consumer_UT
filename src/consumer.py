from multiprocessing import Process
import framequeue as Queue

class Consumer(Process):
    def __init__(self)->None:
        Process.__init__(self)