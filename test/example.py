from matplotlib import pyplot as plt
import numpy as np
from fig2gif import GIF

# create a GIF object, specifying an output filename,
# frames per second (fps), dots per inch (dpi), and
# number of loops (0 being infinite)
mov = GIF('sum_of_sines.gif',fps=10,dpi=100,loop=0)


# create a matplotlib figure on which to draw whatever
# you'd like to make a movie of, along with subplot
# axes
f = plt.figure(figsize=(12,4))
ax1 = f.add_subplot(131)
ax2 = f.add_subplot(132)
ax3 = f.add_subplot(133)

# in this example, we want a three-panel figure
# showing two phase-shifted sine waves and their
# sum
t = np.linspace(0,10*np.pi,1024)
sig1 = np.sin(t)

# set limits to the axes so that they're constant
# across frames
xlim = (t.min(),t.max())
ylim = (-2.1,2.1)
for ax in [ax1,ax2,ax3]:
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

# plot anything that doesn't change outside of the
# loop; the first sine wave has a constant phase of 0
line1, = ax1.plot(t,sig1)

# the loop needs to know whether the shifted and summed
# waves have ever been drawn before. if they haven't,
# they're plotted with ax.plot; if they have, they're
# updated with ax.set_ydata
started = False

N = 20
for k in range(N):

    # shift phase by k/N cycles:
    sig2 = np.sin(t+float(k)/float(N)*2.0*np.pi)
    sig3 = sig1+sig2

    if not started:
        line2, = ax2.plot(t,sig2)
        line3, = ax3.plot(t,sig3)
        started = True
    else:
        line2.set_ydata(sig2)
        line3.set_ydata(sig3)

    plt.pause(.000001)

    # add each new frame to the GIF object
    mov.add(f)

# make the GIF object
mov.make(make_gif=False,make_webm=True)
