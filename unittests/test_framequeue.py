import sys 
import unittest
sys.path.append('../')
import src.framequeue as Queue


class TestQueue(unittest.TestCase):

    def test_QueueSize(self):
        self.assertEqual(Queue.FrameQueue(numberOfElements=5)
                                            .get_sizeofQueue(), 5)
    
    def test_QueueSizeRaisesExeptionQueueElementCount(self):
        with self.assertRaises(Queue.ErrorQueueElementsCount):
            Queue.FrameQueue(numberOfElements=0)

    def test_QueuesIsFullExeption(self):
        queue = Queue.FrameQueue(numberOfElements=5)
        with self.assertRaises(Queue.ErrorQueueTimeoutQueueFull):
            for i in range(6):
                queue.put_data([i,i+1,i*i])

    def testQueueIfEmptyExeption(self):
        queue = Queue.FrameQueue(numberOfElements=5)
        for i in range(3):
                queue.put_data([i,i+1,i*i])

        with self.assertRaises(Queue.ErrorQueueTimeoutQueueEmpty):
            for i in range(5):
                queue.get_data()

if(__name__ == "__main__"):
    unittest.main(verbosity=2)