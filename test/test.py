from matplotlib import pyplot as plt
import numpy as np
from mpl_gifv import GIF

f = plt.figure(figsize=(12,4))

mov = GIF('sum_of_sines.gif',fps=30,dpi=100,loop=0)

t = np.linspace(0,10*np.pi,1024)
sig1 = np.sin(t)
xlim = (t.min(),t.max())
ylim = (-2.1,2.1)

for k in range(100):
    
    sig2 = np.sin(t+float(k)/50.0*np.pi)
    sig3 = sig1+sig2

    plt.clf()
    plt.subplot(1,3,1)
    plt.cla()
    plt.plot(t,sig1)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.subplot(1,3,2)
    plt.cla()
    plt.plot(t,sig2)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.subplot(1,3,3)
    plt.cla()
    plt.plot(t,sig3)
    plt.xlim(xlim)
    plt.ylim(ylim)
    
    plt.pause(.000001)
    mov.add(f)

mov.make()
