from src.consumer import Consumer
from src.framequeue import FrameQueue
from src.producer import Producer
from src.exceptions import *
import os
from PIL import Image

if (__name__ == "__main__"):
    
    frame_dir = 'processed'
    frame_numbers = 100

    queue_A = FrameQueue(100) #queue to send sourceframe
    queue_B = FrameQueue(100) #queue to send preprocessed frame

    producer = Producer(sourceShape = (768,1024,3),
                        queue = queue_A,
                        maxframeCount = frame_numbers,
                        timeBetweenFrames = 50)
    
    consumer = Consumer(reciveQueue = queue_A,
                        sendQueue = queue_B,
                        ProducerPid = producer.pid,
                        shapeDivider = 2,
                        filterKernel = (5,5))
    
    if( frame_dir in os.listdir()):
        print("dir: "+frame_dir+" is exist")
    else:
        os.mkdir(frame_dir)

    os.chdir(frame_dir)
    
    producer.start()
    consumer.start()

    while(queue_B.get_empty()):
        pass
    frame_iter = 0 
    while(True):
        try:
            frame = queue_B.get_data()
            frame_iter +=1
            image = Image.fromarray(frame).convert('RGB')
            image.save("sample_"+str(frame_iter)+".png")
            
        except ErrorQueueTimeoutQueueEmpty:             
                if(consumer.is_alive() == False):
                    break
     
    producer.join()
    consumer.join()