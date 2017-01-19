# mpl_gifv

## Make a movie out of matplotlib plots (requires ImageMagick)

## Preliminaries

1. Install [ImageMagick](https://www.imagemagick.org). In Debian/Ubuntu run `apt-get install imagemagick`. For other distros and OSs, see [ImageMagick installation instructions](https://www.imagemagick.org/script/binary-releases.php).

2. To run test.py verify installation of [numpy](http://numpy.org) and [matplotlib](http://matplotlib.org).

## The basic idea:

1. Create a GIFV object.

2. Add frames to it by passing matplotlib figure handles to its add function.

3. Call its make function.

## Example

```python
from matplotlib import pyplot as plt
import numpy as np

f = plt.figure()

mov = GIFV('example.gif',10)

for k in range(10):
    plt.cla()
    plt.imshow(np.random.rand(100,100))
    plt.pause(.000001)
    mov.add(f)

mov.make()
```

