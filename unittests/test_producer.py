import sys
import unittest
sys.path.append('../src/')
import producer as Producer
import framequeue as Queue

class TestProducer(unittest.TestCase):
    
    def test_ProducerIsRunAndTerminatedAfterSend_5_Data_Frame(self):
        queue = Queue.FrameQueue(numberOfElements=50) #to have enought queue size without geting data from queue
        producer = Producer.Producer((10,10,3),
                                        queue=queue,
                                        maxframeCount=5,
                                        timeBetweenFrames=50)
        producer.start()
        self.assertTrue(producer.is_alive())
        producer.join()
        self.assertFalse(producer.is_alive())
    



if(__name__ == "__main__"):
    unittest.main(verbosity=2)