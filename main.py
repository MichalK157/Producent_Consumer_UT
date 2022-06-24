import queue
from src.consumer import Consumer
from src.framequeue import FrameQueue
from src.producer import Producer
#from src.source import Source
import os

if (__name__ == "__mian__"):
    
    # queue_A = FrameQueue(100)
    # queue_B = FrameQueue(100)

    # producer = Producer(sourceShape = (1024,768,3),
    #                     queue = queue_A,
    #                     maxframeCount = 100,
    #                     timeBetweenFrames = 50)
    
    # consumer = Consumer(reciveQueue = queue_A,
    #                     sendQueue = queue_B,
    #                     ProducerPid = producer.pid,
    #                     shapeDivider =2,
    #                     filterKernel = (5,5))

    print(os.listdir())    