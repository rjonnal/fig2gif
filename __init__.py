from subprocess import call
import os,glob,random,sys
import logging
logging.basicConfig(level=logging.INFO)

class GIF:

    def __init__(self,gif_filename,fps=30,dpi=100,loop=0):
        self.logger = logging.getLogger(__name__)
        self.gif_filename = gif_filename
        self.fps = fps
        self.loop = loop
        self.wdir = '%s_%d.tmp'%(self.gif_filename,random.randint(0,2**32))

        # generate a random working directory name; if it exists already, make
        # a new one.
        while os.path.exists(self.wdir):
            self.wdir = '%s_%d.tmp'%(self.gif_filename,random.randint(0,2**32))

        self.logger.info('Creating temporary directory %s.'%self.wdir)
        os.mkdir(self.wdir)
            
        self.index = 0
        self.dpi = dpi
        
    def __del__(self):
        if os.path.exists(self.wdir):
            try:
                self.logger.info('abnormal exit, deleting %s.'%self.wdir)
                png_list = glob.glob(os.path.join(self.wdir,'*.png'))
                for png_file in png_list:
                    os.remove(png_file)

                # clean up working directory
                os.rmdir(self.wdir)
                
            except Exception as e:
                print e
                
    def add(self,fig):
        # save the given figure to the working directory
        outfn = os.path.join(self.wdir,'frame_%020d.png'%self.index)
        self.logger.info('Saving figure to file %s.'%outfn)
        fig.savefig(outfn,dpi=self.dpi)
        self.index = self.index + 1

    def make(self):

        # convert FPS into IM's delay parameter (expressed in 10 ms "ticks")
        delay = 1.0/float(self.fps)*100.0

        # run ImageMagick convert function to make the GIF
        self.logger.info('Running ImageMagick convert to create gif in %s.'%self.gif_filename)
        command = ['convert','-delay','%0.1f'%delay,'-loop','%d'%self.loop,'%s'%(os.path.join(self.wdir,'frame*.png')),'%s'%self.gif_filename]
        call(command)

        self.logger.info('Cleaning up.')
        # clean up temporary png files
        png_list = glob.glob(os.path.join(self.wdir,'*.png'))
        for png_file in png_list:
            os.remove(png_file)

        # clean up working directory
        os.rmdir(self.wdir)
        
