from multiprocessing import Process
import source as source
from framequeue import FrameQueue 
import time
from exceptions import *

class Producer(Process):
    """
    
    """
    def __init__(self,sourceShape: tuple,
                    queue: FrameQueue,
                    maxframeCount: int,
                    timeBetweenFrames: float,
                    daemon:bool = True )-> None:

        Process.__init__(self)
        self.daemon = daemon
        self.__queue = queue
        self.__maxframeCount = maxframeCount
        self.__timeBetweenFrames = timeBetweenFrames
        self.__framesource = source.Source(sourceShape)

    def __getWaitTime_ms(self) -> float:
        return self.__timeBetweenFrames*0.001

    def run(self):
        while(self.__maxframeCount > 0):
            try:
                self.__queue.put_data(self.__framesource.get_data())
            except ErrorQueue:
                print("Queue has too few empty space")
                break
            self.__maxframeCount -= 1 
            time.sleep(self.__getWaitTime_ms())
            