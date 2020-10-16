import noise
import numpy as np


class NoiseMap2:
    def __init__(self, seed=None, shape=(1024, 1024), octaves=6, persistence=0.5,
                 lacunarity=2, scale=100):
        assert len(shape) == 2

        if seed is None:
            seed = np.random.randint(0, scale)

        self.noise_map = np.zeros(shape)
        for x in range(shape[0]):
            for y in range(shape[1]):
                self.noise_map[x, y] = noise.pnoise2(x / scale, y / scale,
                                                     octaves=octaves,
                                                     persistence=persistence,
                                                     lacunarity=lacunarity,
                                                     repeatx=shape[0],
                                                     repeaty=shape[1],
                                                     base=seed)

    def __getitem__(self, item):
        return self.noise_map[tuple([int(x) for x in item])]

    def __setitem__(self, item, key):
        self.noise_map[tuple([int(x) for x in item])] = key

    def show(self):
        from matplotlib import pyplot as plt
        plt.imshow(self.noise_map, interpolation='nearest')
        plt.show()
