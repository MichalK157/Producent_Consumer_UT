import numpy as np

class Source:
    """
    Data frame generator from given shape tuple (rows,cols,chanels)

    @source_shape: (tuple) - Frame shape (hiht, width, chanels(RGB))
                            examle: (768,1024,3)
    """
    def __init__(self, source_shape: tuple):
        self._source_shape: tuple = source_shape

    def get_data(self) -> np.ndarray:
        rows, cols, channels = self._source_shape
        return np.random.randint(
                256,
                size=rows * cols * channels,
                dtype=np.uint8,
                ).reshape(self._source_shape)