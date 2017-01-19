from subprocess import call
import os

class GIF:

    def __init__(self,gif_filename,fps=30,dpi=100,loop=0):
        self.gif_filename = gif_filename
        self.fps = fps
        self.loop = loop
        self.wdir = '%s.tmp'%self.gif_filename
        try:
            os.stat(self.wdir)
        except:
            os.mkdir(self.wdir)

        try:
            os.remove(os.path.join(self.wdir,'*.png'))
        except:
            print '%s created and empty.'%self.wdir
            
        self.index = 0
        self.dpi = dpi
        
    def add(self,fig):
        outfn = os.path.join(self.wdir,'frame_%06d.png'%self.index)
        fig.savefig(outfn,dpi=self.dpi)
        self.index = self.index + 1

    def make(self):
        delay = 1.0/float(self.fps)*100.0
        command = ['convert','-delay','%0.1f'%delay,'-loop','%d'%self.loop,'%s'%(os.path.join(self.wdir,'frame*.png')),'%s'%self.gif_filename]
        call(command)
        cleanup = ['rm','-rfv','%s'%self.wdir]
        call(cleanup)
        
