from multiprocessing import Queue


class FrameQueue():
    """
    
    @param elementsize (tuple(int,int,int)): size of frame to send by Queue -> template (px:int,py:int,ch=3)
    @param elementsize (int): numbers of frame to send by Queue, value greater then 0
    """
    def __init__(self, elementsize: tuple , numberofelements : int ) -> None:
        row , column , chnnels = elementsize
        self.__sizeofQueue = numberofelements*row*column*chnnels
        self.Queue = Queue(maxsize=self.__sizeofQueue)
        
    def get_sizeofQueue(self):
        return self.__sizeofQueue

    def set_data(self, frame):
        self.Queue.put(frame)

    def get_data(self, timeout : float = 5.0):
        return self.Queue.get(timeout=timeout)



class ErrorQueue(Exception):
    pass

class ErrorQueueElementSize(ErrorQueue):
    def __init__(self, expression: str ="ErrorQueueElementSize", msg: str = "") -> None:
        self.expression = expression
        self.msg = msg

class ErrorQueueElementsCount(ErrorQueue):
    def __init__(self, expression: str ="ErrorQueueElementsCount", msg: str = "") -> None:
        self.expression = expression
        self.msg = msg