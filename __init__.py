from subprocess import call
import os


class GIFV:

    def __init__(self,gif_filename,fps,dpi=100,loop=0):
        self.gif_filename = gif_filename
        self.fps = fps
        self.loop = loop
        self.wdir = '%s.tmp'%self.gif_filename
        try:
            os.stat(self.wdir)
        except:
            os.mkdir(self.wdir)

        command = ['rm','-v','%s/*.png']
        call(command)
        self.index = 0
        self.dpi = dpi
        
    def add(self,fig):
        outfn = os.path.join(self.wdir,'frame_%06d.png'%self.index)
        f.savefig(outfn,dpi=self.dpi)
        self.index = self.index + 1

    def make(self):
        delay = 1.0/float(self.fps)*100.0
        command = ['convert','-delay','%0.1f'%delay,'-loop','%d'%self.loop,'%s'%(os.path.join(self.wdir,'frame*.png')),'%s'%self.gif_filename]
        call(command)
        
        
if __name__=='__main__':

    from matplotlib import pyplot as plt
    import numpy as np

    f = plt.figure()

    mov = GIFV('temp.gif',10)
    
    for k in range(10):
        plt.cla()
        plt.imshow(np.random.rand(100,100))
        plt.pause(.000001)
        mov.add(f)

    mov.make()
