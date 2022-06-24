import sys 
sys.path.append('../')
import unittest
import time
import src.framequeue as Queue
import src.consumer as Consumer
from src.source import Source

class TestConsumer(unittest.TestCase):

    def test_ConsumerReshapeFrameBy_2(self):
        input = Source((1024,768,3)).get_data()

        consumer = Consumer.Consumer(Queue.FrameQueue(1),
                                        Queue.FrameQueue(1),
                                        None,
                                        2,
                                        (5,5))
        # check output frame shape 
        output = consumer.ReshapeFrame(input)
        self.assertEqual(output.shape,(512, 384, 3))
    
    def test_ConsumerReshapeFrameBy_0_Orless(self):
        with self.assertRaises(Consumer.ErrorConsumerShapeDivider):
            Consumer.Consumer(Queue.FrameQueue(1),
                                Queue.FrameQueue(1),
                                0,
                                0,
                                (5,5))
        
        with self.assertRaises(Consumer.ErrorConsumerShapeDivider):
            Consumer.Consumer(Queue.FrameQueue(1),
                                Queue.FrameQueue(1),
                                0,
                                -5,
                                (5,5))

    def test_MedianFilter(self):
        #input.shape == output.shape and input != ooutput 

        input = Source((1024,768,3)).get_data()

        consumer = Consumer.Consumer(Queue.FrameQueue(1),
                                        Queue.FrameQueue(1),
                                        0,
                                        2,
                                        (5,5))
        
        output = consumer.MedianFilter(input)

        self.assertEqual(output.shape,input.shape)
        self.assertNotEqual(output.all(),input.all())
    
    def test_ConsumerCanClearQueue(self):
        import producer 
        reciveQueue = Queue.FrameQueue(5)
        Producer = producer.Producer((1024,768,3),
                                        reciveQueue,
                                        5,
                                        50) 
        
        consumer = Consumer.Consumer(reciveQueue,
                                        Queue.FrameQueue(5),
                                        Producer.pid,
                                        2,
                                        (5,5))
        Producer.start()
        consumer.start()
        Producer.join()
        consumer.join()
        self.assertTrue(reciveQueue.get_empty())
    
    def test_SendPreprocesedFrameToSecondQueue(self):
        import producer 
        reciveQueue = Queue.FrameQueue(5)
        sendQueue = Queue.FrameQueue(5)
        Producer = producer.Producer((1024,768,3),
                                        reciveQueue,
                                        5,
                                        50) 
        
        consumer = Consumer.Consumer(reciveQueue,
                                        sendQueue,
                                        Producer.pid,
                                        2,
                                        (5,5))
        Producer.start()
        consumer.start()
        time.sleep(2)
        Producer.join()
        consumer.join()
        self.assertTrue(sendQueue.get_full())

if(__name__ == "__main__"):
    unittest.main(verbosity=2)