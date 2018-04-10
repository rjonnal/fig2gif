from matplotlib import pyplot as plt
import numpy as np
from fig2gif import GIF

# create a GIF object, specifying an output filename
mov = GIF('random.gif',fps=10,dpi=50,loop=0)

# create a matplotlib figure
f = plt.figure()

# plot something on it a few times:
for k in range(10):
    # clear the axes:
    plt.cla()
    # make the plot
    plt.plot(np.random.rand(100))
    # add it to the GIF
    mov.add(f)

# make the gif
mov.make()
