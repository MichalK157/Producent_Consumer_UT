import sys 
import unittest
sys.path.append('../')
import src.framequeue as Queue


class TestQueue(unittest.TestCase):

    def test_QueueSize(self):
        self.assertEqual(Queue.FrameQueue(elementsize=(10,10,3),
                                            numberofelements=5)
                                            .get_sizeofQueue(),
                            10*10*3*5)

    def test_QueueSizeRaisesExeptionQueueElementSize(self):
        with self.assertRaises(Queue.ErrorQueueElementSize):
            Queue.FrameQueue(elementsize=(10,10),numberofelements=1)

    def test_QueueSizeRaisesExeptionQueueElementCount(self):
        with self.assertRaises(Queue.ErrorQueueElementsCount):
            Queue.FrameQueue(elementsize=(10,10,3),numberofelements=0)

if(__name__ == "__main__"):
    unittest.main(verbosity=2)