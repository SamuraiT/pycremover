"""
author: Yasukawa Tatsuro 
contactinfo: https://github.com/SamuraiT
"""
import os
class PycRemover(object):
    """
    PycRemover represents remover which removes all the pyc files
    including sub-directory's pyc files
    """
    def __call__(self):
        self.process()
    
    def process(self, cwd = os.getcwd() ):
        listdir = os.listdir( cwd )
        self.remove( cwd,listdir )
        for filename in listdir:
            abs_filename = os.path.join( cwd,filename )
            if os.path.isdir( abs_filename ):
                listdir = os.listdir( abs_filename )
                self.remove( abs_filename,listdir )
                self.process( abs_filename )
                

    def remove(self,cwd, listdir,extension='.pyc'):
        for filename in listdir:
            if filename.endswith( extension ):
                os.remove( os.path.join(cwd,filename) )
    
pycremover = PycRemover()
pycremover()
        
