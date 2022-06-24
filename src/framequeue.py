from multiprocessing import Queue
from queue import Full, Empty
from exceptions import ErrorQueueElementsCount, ErrorQueueTimeoutQueueEmpty, ErrorQueueTimeoutQueueFull

class FrameQueue():
    """
    
    @param numberofelements (int): numbers of frame to send by Queue, value greater then 0
    """
    def __init__(self, numberOfElements : int ) -> None:

        if(numberOfElements <= 0):
            raise ErrorQueueElementsCount
        self.__sizeofQueue = numberOfElements
        self.__Queue = Queue(maxsize=self.__sizeofQueue)

    def get_sizeofQueue(self):
        return self.__sizeofQueue

    def put_data(self, frame , timeout = 1.0):
        try:
            self.__Queue.put(frame,block=True, timeout=timeout)
        except Full:
            raise ErrorQueueTimeoutQueueFull

    def get_data(self, timeout : float = 1.0):
        try:
            data = self.__Queue.get(block=True, timeout=timeout)
        except Empty:
            raise ErrorQueueTimeoutQueueEmpty
        return data

    def get_empty(self)->bool:
        return self.__Queue.empty()

    def get_full(self)->bool:
        return self.__Queue.full()
    
    def close(self):
        self.__Queue.cancel_join_thread()