import sys
sys.path.append('../src/')
from multiprocessing import Process
from src.framequeue import FrameQueue
import numpy as np
from scipy import ndimage
from src.exceptions import *
import time

class Consumer(Process):
    """
    Customer Class
    is a thread which is receiving from reciveQueue queue and make conversions
    then send preprocessed data to sendQueue

    @param reciveQueue: (FrameQueue) - Reciving Queue Object
    @param sendQueue: (FrameQueue) - Transmiting Queue Object
    @param ProducerPid: (int) - Producent system PID
    @param shapeDivider: (int) - prescaler of frame -> value > 1 frame will be smaller 
                                    but if 0 > value > 1 frame will be greater
    @param filterKernel: (tuple) - median filter kernel ->(x,y)
    @param daemon: (bool) - daemon process -> default True

    """
    def __init__(self,
                    reciveQueue: FrameQueue,
                    sendQueue: FrameQueue,
                    ProducerPid: int,
                    shapeDivider: int,
                    filterKernel: tuple,
                    daemon: bool = True) -> None:

        Process.__init__(self)
        self.daemon = daemon
        
        if(shapeDivider<=0):
            raise ErrorConsumerShapeDivider
        self.__shapeDivider = shapeDivider

        if(len(filterKernel) !=2 ):
            raise ErrorConsumerFilterKernelShape
        
        x,y = filterKernel
        self.__filterKernel = (x,y,3)
        
        self.__reciveQueue = reciveQueue
        self.__sendQueue = sendQueue
        self.__producerrPid =  ProducerPid
    
    def __del__(self) -> None:
        try: #if raise exception in __init__
            self.__sendQueue.close()
        except AttributeError:
            pass
        
    def ReshapeFrame(self, input: np.ndarray) -> np.ndarray:
        
        return ndimage.zoom(input,
                            (1/self.__shapeDivider, 1/self.__shapeDivider, 1.0)) #set zoom value for eatch axis
    
    def MedianFilter(self, input: np.ndarray) -> np.ndarray:

        return ndimage.median_filter(input, 
                                        footprint=np.ones(self.__filterKernel))
    
    def run(self) -> None:
        
        while True: 
            try:
                frame = self.__reciveQueue.get_data()
            except ErrorQueueTimeoutQueueEmpty:
                if(self.__producerrPid == None):
                    break
            frame = self.ReshapeFrame(frame)
            frame = self.MedianFilter(frame)
            try:
                self.__sendQueue.put_data(frame)
            except ErrorQueueTimeoutQueueFull:
                time.sleep(1)
                if(self.__sendQueue.get_full != True):
                    self.__sendQueue.put_data(frame)
                else:
                    break   
        self.__del__()