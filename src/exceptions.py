
class ErrorQueue(Exception):
    pass

class ErrorConsumer(Exception):
    pass


##Queues##

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

##Consumer##

class ErrorConsumerShapeDivider(ErrorConsumer):
    def __init__(self, expression: str ="ErrorConsumerShapeDivider", msg: str = "") -> None:
        self.expression = expression
        self.msg = msg

class ErrorConsumerFilterKernelShape(ErrorConsumer):
    def __init__(self, expression: str ="ErrorConsumerFilterKernelShape", msg: str = "") -> None:
        self.expression = expression
        self.msg = msg