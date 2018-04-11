from subprocess import call
import os,glob,random,sys
import logging
logging.basicConfig(level=logging.INFO)

class GIF:

    def __init__(self,gif_filename,fps=30,dpi=100,loop=0,autoclean=False):
        """Create a GIF object.

        Argument:
        gif_filename -- the name of the GIF file to output with GIF.make()
        Keyword arguments:
        fps -- frames per second, default 30
        dpi -- dots per inch, default 100
        loop -- how many times to loop, default 0 (infinite)
        autoclean -- clean up temporary files, default False
        """       
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
        self.autoclean = autoclean
        
    def __del__(self):
        if self.autoclean:
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
        """Add a frame to a GIF.

        Argument:
        fig -- the handle of a matplotlib figure
        """       
        # save the given figure to the working directory
        outfn = os.path.join(self.wdir,'frame_%020d.png'%self.index)
        self.logger.info('Saving figure to file %s.'%outfn)
        fig.savefig(outfn,dpi=self.dpi,facecolor=fig.get_facecolor(),edgecolor='none')
        self.index = self.index + 1
        
    def make(self,make_avi=False,verbose=False,make_script=False):
        """Make the GIF.
        """       

        # convert FPS into IM's delay parameter (expressed in 10 ms "ticks")
        delay = 1.0/float(self.fps)*100.0

        # run ImageMagick convert function to make the GIF
        self.logger.info('Running ImageMagick convert to create gif in %s.'%self.gif_filename)
        command = ['convert','-delay','%0.1f'%delay,'-loop','%d'%self.loop,'%s'%(os.path.join(self.wdir,'frame*.png')),'%s'%self.gif_filename]
        if verbose:
            command = command[0]+['-verbose']+command[1:]
        if make_script:
            folder,filename = os.path.split(self.gif_filename)
            script_fn = os.path.join(folder,'make_'+os.path.splitext(filename)[0]+'.sh')
            fid = open(script_fn,'w')
            fid.write('#! /bin/bash\n\n')
            fid.write(command)
            fid.close()
            
        
        call(command)

        if make_avi:
            avi_filename = os.path.splitext(self.gif_filename)[0]+'.avi'
            self.logger.info('Running ImageMagick convert to create gif in %s.'%avi_filename)
            command = ['mencoder','\"mf://%s/\"'%os.path.join(os.path.join('.',self.wdir),'frame*.png'), '-o', avi_filename, '-ovc', 'lavc', '-lavcopts', 'vcodec=mjpeg']
            call(command)
        
        if self.autoclean:
            self.logger.info('Cleaning up.')
            # clean up temporary png files
            png_list = glob.glob(os.path.join(self.wdir,'*.png'))
            for png_file in png_list:
                os.remove(png_file)

            # clean up working directory
            os.rmdir(self.wdir)
        
