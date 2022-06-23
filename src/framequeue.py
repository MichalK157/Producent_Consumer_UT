from multiprocessing import Queue
from queue import Full, Empty


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
            self.__Queue.put(frame, timeout=timeout)
        except Full:
            raise ErrorQueueTimeoutQueueFull

    def get_data(self, timeout : float = 1.0):
        try:
            data = self.__Queue.get(timeout=timeout)
        except Empty:
            raise ErrorQueueTimeoutQueueEmpty
        return data

    def cancel(self):
        self.__Queue.cancel_join_thread()
        self.__Queue.close()

class ErrorQueue(Exception):
    pass

class ErrorQueueElementsCount(ErrorQueue):
    def __init__(self, expression: str ="ErrorQueueElementsCount", msg: str = "") -> None:
        self.expression = expression
        self.msg = msg

class ErrorQueueTimeoutQueueFull(ErrorQueue):
    def __init__(self, expression: str ="ErrorQueueTimeoutFullQueue", msg: str = "") -> None:
        self.expression = expression
        self.msg = msg

class ErrorQueueTimeoutQueueEmpty(ErrorQueue):
    def __init__(self, expression: str ="ErrorQueueTimeoutQueueEmpty", msg: str = "") -> None:
        self.expression = expression
        self.msg = msg
