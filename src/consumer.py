from multiprocessing import Process
from framequeue import FrameQueue
import numpy as np
from scipy import ndimage
from exceptions import ErrorConsumerShapeDivider,ErrorConsumerFilterKernelShape

class Consumer(Process):
    def __init__(self,
                    reciveQueue: FrameQueue,
                    sendQueue: FrameQueue,
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

    def ReshapeFrame(self, input: np.ndarray) -> np.ndarray:
        
        return ndimage.zoom(input,
                            (1/self.__shapeDivider, 1/self.__shapeDivider, 1.0)) #set zomm value for eatch axis
    
    def MedianFilter(self, input: np.ndarray) -> np.ndarray:

        return ndimage.median_filter(input, 
                                        footprint=np.ones(self.__filterKernel))
    
    def run(self) -> None:
        while True:
            pass

