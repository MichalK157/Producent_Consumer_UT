import sys
sys.path.append('../src/')
from multiprocessing import Process
import src.source as source
from src.framequeue import FrameQueue 
import time
from src.exceptions import *

class Producer(Process):
    """
    Producer Class
    is a thread which is transmiting sourceShape by FrameQueue Object to Consumer

    @param sourceShape: (tuple) - Frame shape (hiht, width, chanels(RGB)) more in source.py
    @param queue: (FrameQueue) - Transmiting Queue Object
    @param maxframeCount: (int) - numbers of frames to generate and send
    @param timeBetweenFrames: (float) - time between frames in milliseconds
    @param daemon: (bool) - daemon process -> default True 
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

    def run(self) -> None:
        
        while(self.__maxframeCount > 0):
            try:
                self.__queue.put_data(self.__framesource.get_data())
            except ErrorQueue:
                print("Queue has too few empty space")
                break
            self.__maxframeCount -= 1 
            time.sleep(self.__getWaitTime_ms())
            