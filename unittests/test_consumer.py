import sys 
import unittest
sys.path.append('../src/')

import framequeue as Queue
import consumer as Consumer
from source import Source

class TestConsumer(unittest.TestCase):

    def test_ConsumerReshapeFrameBy_2(self):
        input = Source((1024,768,3)).get_data()

        consumer = Consumer.Consumer(Queue.FrameQueue(1),
                                        Queue.FrameQueue(1),
                                        2,
                                        (5,5))
        # check output frame shape 
        self.assertEqual(consumer.ReshapeFrame(input).shape,(512, 384, 3))
    
    def test_ConsumerReshapeFrameBy_0_Orless(self):
        with self.assertRaises(Consumer.ErrorConsumerShapeDivider):
            Consumer.Consumer(Queue.FrameQueue(1),
                                Queue.FrameQueue(1),
                                0,
                                (5,5))
        
        with self.assertRaises(Consumer.ErrorConsumerShapeDivider):
            Consumer.Consumer(Queue.FrameQueue(1),
                                Queue.FrameQueue(1),
                                -5,
                                (5,5))

    def test_MedianFilter(self):
        #input.shape == output.shape and input != ooutput 

        input = Source((1024,768,3)).get_data()

        consumer = Consumer.Consumer(Queue.FrameQueue(1),
                                        Queue.FrameQueue(1),
                                        2,
                                        (5,5))
        
        output = consumer.MedianFilter(input)

        self.assertEqual(output.shape,input.shape)
        self.assertNotEqual(output.all(),input.all())

    def test_SendPreprocesedFrameToSecondQueue(self):
        self.assertFalse(True)

    def test_ConsumerCanClearQueue(self):
        self.assertFalse(True)

if(__name__ == "__main__"):
    unittest.main(verbosity=2)