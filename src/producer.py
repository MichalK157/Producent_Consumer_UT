from multiprocessing import Process

class Producer(Process):
    """
    
    """
    def __init__(self,daemon = True )-> None:
        super().__init__(daemon=daemon)

    def run(self):
        pass


